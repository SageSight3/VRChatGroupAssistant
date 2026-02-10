use vrchatapi::apis::configuration::Configuration;
use reqwest::cookie::{CookieStore, Jar};
use std::str::FromStr;
use std::fs::File;
use std::io::prelude::*;
use vrchatapi::models::{RegisterUserAccount200Response, RequiresTwoFactorAuth};
use vrchatapi::apis::authentication_api;
use reqwest::header::HeaderValue;
use std::sync::Arc;
use serde_json;

use super::util;

use super::APP_CONFIG_PATH;

//Login to VRChat and return config for future API calls
pub async fn login() -> Configuration {

    //Initialize account config
    let mut config = make_account_config();

    //Attempt login from stored cookies
    let cookies = load_stored_cookies(&mut config).await;
    let login = authentication_api::get_current_user(&config)
        .await
        .unwrap();

    match login {
        RegisterUserAccount200Response::CurrentUser(user) => {
            println!("Welcome back, {}", user.display_name);
        },
        //if cookies failed to load
        RegisterUserAccount200Response::RequiresTwoFactorAuth(requires_2fa) => {
            println!("Two-factor authentication required");

            do_2fa(&mut config, requires_2fa).await;

            let login_2fa = authentication_api::get_current_user(&config)
                .await
                .unwrap();

            match login_2fa {
                RegisterUserAccount200Response::CurrentUser(user_2fa) => {
                    println!("Welcome, {}", user_2fa.display_name);

                    //write new cookies to file, unclear where new cookies are generated
                    store_cookies(cookies).await;
                },
                RegisterUserAccount200Response::RequiresTwoFactorAuth(_) => {
                    println!("Login Error: 2fa failed");
                    panic!();
                }
            }
        }
    }

    //return account config
    config
}

//Load cookies from cookie_info file to config.client
async fn load_stored_cookies(config: &mut Configuration) -> Arc<Jar> {
    //Get cookies from app config
    let app_config = util::parse_json(APP_CONFIG_PATH);

    let cookies_src = app_config["sessionConfig"]["cookies"].as_str()
        .expect("Failed to find cookies");

    //Create cookie stre from existing cookies
    let jar = reqwest::cookie::Jar::default();
    jar.set_cookies(
        &mut [HeaderValue::from_str(
            &cookies_src,
        )
        .expect("Cookie not okay")]
        .iter(),
        &url::Url::from_str("https://api.vrchat.cloud").expect("Url not okay"),
    );
    let jar = Arc::new(jar);

    //Set config client to have existing cookies
    config.client = reqwest::Client::builder()
        .cookie_provider(jar.clone())
        .build()
        .unwrap();

    jar
}

//Prompt user for 2fa code and verify
async fn do_2fa(config: &mut Configuration, requires_2fa: RequiresTwoFactorAuth) {

    if requires_2fa.requires_two_factor_auth
        .contains(&::vrchatapi::models::TwoFactorAuthType::EmailOtp) 
    {

        let code = util::read_user_input("Enter 2fa code from email here: ");

        if let Err(err) = 
            ::vrchatapi::apis::authentication_api::verify2_fa_email_code(
                &config, 
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
                &config, 
                ::vrchatapi::models::TwoFactorAuthCode::new(code)
            ).await 
        {
            println!("Error verfying 2fa code from authenticator app: {}", err);
            panic!();
        }
    }
}

//Write cookies to cookies file
async fn store_cookies(cookies: Arc<Jar>) {
    let current_cookies = cookies
        .cookies(&url::Url::from_str("https://api.vrchat.cloud").expect("Url not okay"))
        .expect("Cookies not found")
        .to_str()
        .expect("Cookies not valid string")
        .to_string();

    //Only way we're here is if app_config exists, is accessible, and is parseable
    let mut app_config =  util::parse_json(APP_CONFIG_PATH);

    //Update JSON
    app_config["sessionConfig"]["cookies"] = serde_json::Value::String(current_cookies);
    let app_config = serde_json::to_string_pretty(&app_config).unwrap();

    if let Ok(mut file) = File::create("storage/config.json") {
        file.write_all(app_config.as_bytes()).expect("failed to save cookies");
        println!("Cookies have been updated!");
    }
}

//Makes a Configuration from data in config_info file
fn make_account_config() -> Configuration {

    //https://doc.rust-lang.org/std/fs/fn.read_to_string.html
    let config_info = util::parse_json(APP_CONFIG_PATH);

    let username = config_info["sessionConfig"]["username"].as_str().unwrap();
    let password = String::from(config_info["sessionConfig"]["password"].as_str().unwrap());
    let user_agent = format!("{}/{} {}",
        config_info["appName"].as_str().unwrap(),
        config_info["appVersion"].as_str().unwrap(),
        config_info["sessionConfig"]["email"].as_str().unwrap()
    );

    let mut config = Configuration::default();
    config.basic_auth = 
        Some((String::from(username), Some(String::from(util::deobfuscate_text(&password)))));
    config.user_agent = Some(String::from(user_agent));

    config
}