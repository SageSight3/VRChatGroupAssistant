use vrchatapi::apis::configuration::Configuration;
use reqwest::cookie::{CookieStore, Jar};
use std::str::FromStr;
use std::fs::File;
use std::io::prelude::*;
use vrchatapi::models::{RegisterUserAccount200Response, RequiresTwoFactorAuth};
use vrchatapi::apis::Error;
use vrchatapi::apis::authentication_api;
use vrchatapi::apis::authentication_api::{GetCurrentUserError};
use reqwest::header::HeaderValue;
use std::sync::Arc;
use serde_json;
use regex::Regex;

use super::util;
use super::constants::{APP_CONFIG_PATH, USER_AGENT};

//Login to VRChat and return config for future API calls
pub async fn login() -> Configuration {

    let mut session_config = make_session_config();

    //Attempt login from stored cookies
    let cookies = load_stored_cookies(&mut session_config).await;

    //If this is the first time the user's logged in, or the existing session has expired
    //prompt
    let mut session_login = check_login(&session_config).await;
    match session_login {
        Ok(_) => {
        },
        Err(_) => {
            prompt_auth_credentials(&mut session_config);
            session_login = check_login(&session_config).await;
        }
    }

    let login = session_login.unwrap();

    match login {
        RegisterUserAccount200Response::CurrentUser(user) => {
            println!("Welcome back, {}", user.display_name);
        },
        //if cookies failed to load
        RegisterUserAccount200Response::RequiresTwoFactorAuth(requires_2fa) => {
            println!("Two-factor authentication required");

            do_2fa(&mut session_config, requires_2fa).await;

            let login_2fa = authentication_api::get_current_user(&session_config)
                .await
                .unwrap();

            match login_2fa {
                RegisterUserAccount200Response::CurrentUser(user_2fa) => {
                    println!("Welcome, {}", user_2fa.display_name);

                    //write new cookies to file, unclear where new cookies are generated
                    store_auth_cookies(cookies).await;
                },
                RegisterUserAccount200Response::RequiresTwoFactorAuth(_) => {
                    println!("Login Error: 2fa failed");
                    panic!();
                }
            }
        }
    }

    //return session config
    session_config
}

//Load cookies from cookie_info file to config.client
async fn load_stored_cookies(session_config: &mut Configuration) -> Arc<Jar> {
    //Get cookies from app config
    let app_config = util::parse_json(APP_CONFIG_PATH);

    let cookies_src = app_config["sessionAuthCookies"].as_str()
        .expect("load_stored_cookies(): Failed to find cookies");

    //Create cookie stre from existing cookies
    let jar = reqwest::cookie::Jar::default();
    jar.set_cookies(
        &mut [HeaderValue::from_str(
            &cookies_src,
        )
        .expect("load_stored_cookies(): Cookie not okay")]
        .iter(),
        &url::Url::from_str("https://api.vrchat.cloud").expect("load_stored_cookies: Url not okay"),
    );
    let jar = Arc::new(jar);

    //Set config client to have existing cookies
    session_config.client = reqwest::Client::builder()
        .cookie_provider(jar.clone())
        .build()
        .unwrap();

    jar
}

//Prompts user for their account credentials and put them in the session config
fn prompt_auth_credentials(session_config: &mut Configuration) {
    let username = util::read_user_input("Enter username: ");
    let password = util::read_user_input("Enter password: ");

    session_config.basic_auth = Some((String::from(username), Some(String::from(password))));
}

//Prompt user for 2fa code and verify
async fn do_2fa(session_config: &mut Configuration, requires_2fa: RequiresTwoFactorAuth) {

    if requires_2fa.requires_two_factor_auth
        .contains(&::vrchatapi::models::TwoFactorAuthType::EmailOtp) 
    {

        let code = util::read_user_input("Enter 2fa code from email here: ");

        if let Err(err) = 
            ::vrchatapi::apis::authentication_api::verify2_fa_email_code(
                &session_config, 
                ::vrchatapi::models::TwoFactorEmailCode::new(code)
            ).await 
        {
            println!("Error verfying email 2fa code: {}", err);
            panic!();
        }
    } else {
        let code = util::read_user_input("Enter 2fa code from authenticator app here: ");

        if let Err(err) = 
            ::vrchatapi::apis::authentication_api::verify2_fa(
                &session_config, 
                ::vrchatapi::models::TwoFactorAuthCode::new(code)
            ).await 
        {
            println!("Error verfying 2fa code from authenticator app: {}", err);
            panic!();
        }
    }
}

//Write cookies to cookies file
async fn store_auth_cookies(cookies: Arc<Jar>) {
    let current_cookies = cookies
        .cookies(&url::Url::from_str("https://api.vrchat.cloud").expect("Url not okay"))
        .expect("store_cookies(): Cookies not found")
        .to_str()
        .expect("store_cookies(): Cookies not valid string")
        .to_string();

    //auth cookies must be in the right order when trying to log in to the VRC API via loaded cookies 
    let ordered_auth_cookies = order_auth_cookies(&current_cookies);

    //Only way we're here is if app_config exists, is accessible, and is parseable
    let mut app_config =  util::parse_json(APP_CONFIG_PATH);

    //Update JSON
    app_config["sessionAuthCookies"] = serde_json::Value::String(ordered_auth_cookies);
    let app_config = serde_json::to_string_pretty(&app_config).unwrap();

    if let Ok(mut file) = File::create(APP_CONFIG_PATH) {
        file.write_all(app_config.as_bytes()).expect("failed to save cookies");
        println!("Cookies have been updated!");
    }
}

//Reorder auth cookies, so they are stored as auth=<cookie>; twoFactorAuth=<cookie>
fn order_auth_cookies(cookies_str: &String) -> String {
    let auth_cookie_pattern = 
        Regex::new(r"(?P<Auth1st>auth=.+); (?P<TwoFA2nd>twoFactorAuth=.+)|(?P<TwoFA1st>twoFactorAuth=.+); (?P<Auth2nd>auth=.+)")
        .unwrap();

    let auth_cookies = auth_cookie_pattern.captures(cookies_str.as_str())
        .expect("order_auth_cookies(): Failed to match cookies");

    let auth_cookie ;
    let two_factor_cookie;

    if let Some(a_match) = auth_cookies.name("Auth1st") {
        auth_cookie = a_match.as_str().to_string();
        two_factor_cookie = format!("{}", auth_cookies.name("TwoFA2nd").expect("Failed to match 2fa cookie").as_str());
    } else {
        auth_cookie = format!("{}", auth_cookies.name("Auth2nd").expect("Failed to match auth cookie").as_str());
        two_factor_cookie = format!("{}", auth_cookies.name("TwoFA1st").expect("Failed to match 2fa cookie").as_str());
    }

    let ordered_auth_cookies = format!("{}; {}", auth_cookie, two_factor_cookie);

    ordered_auth_cookies
}

//Makes session config
fn make_session_config() -> Configuration {

    let mut session_config = Configuration::default();
    session_config.user_agent = Some(String::from(USER_AGENT));

    session_config
}

//Query API to see if session is already logged in
async fn check_login(session_config: &Configuration) -> 
    Result<RegisterUserAccount200Response, Error<GetCurrentUserError>> 
{
    authentication_api::get_current_user(&session_config).await
}