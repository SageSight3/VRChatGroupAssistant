use vrchatapi::apis::groups_api;
use vrchatapi::apis::configuration::Configuration;
use vrchatapi::models::LimitedGroup;
use std::result::Result;
use chrono::{self, Datelike};
use std::fs::{OpenOptions};
use std::io::Write;

use super::util;
use super::constants::{APP_CONFIG_PATH};

#[derive(Debug, Clone)]
struct GroupInfo {
    name: String,
    short_code: String,
    discriminator: String,
}

#[derive(Debug)]
pub enum GroupSearchResultError {
    MultipleMatchesError,
    NoMatchesError,
    UnknownError
}

#[derive(Debug, Clone)]
struct MemberCounts {
    online: i32,
    total: i32
}

//Log the date and time, and online and total member counts of target group in activity_log file
pub async fn log_group_member_counts(account: &Configuration, target_group_id: &str) {
    
    let member_counts = get_group_member_counts(account, target_group_id).await;

    //Get time of log entry
    let now = chrono::Local::now();

    //Create log entry

    //Format time info
    let time = format!("{}", now.time().format("%H:%M"));
    let date = format!("{}", now.date_naive());
    let weekday = format!("{}", now.date_naive().weekday());

    //converts month from u32 to it's name
    //https://docs.rs/chrono/latest/chrono/enum.Month.html
    let month = chrono::Month::try_from(
            u8::try_from(now.date_naive().month())
            .unwrap()
    ).ok();
    let month = format!("{:?}", month.unwrap());
    let year = format!("{}", now.date_naive().year());

    //Format member counts
    let member_counts = format!("online: {}, total: {}", member_counts.online, member_counts.total);

    //Build log entry
    let log_entry = format!("{}, {}, {}, {}, {}, {}\n",
        month,
        year,
        date,
        weekday,
        time,
        member_counts
    );

    //write log entry to log file
    let mut log_file = OpenOptions::new()
        .create(true)
        .append(true)
        .open("data/activity_log")
        .expect("Failed to open activity log file");

    log_file.write_all(log_entry.as_bytes()).expect("Failed to write log entry to activity log file");
}

//Query the VRChat API and return the values for target group's online and total member counts
async fn get_group_member_counts(account: &Configuration, target_group_id: &str) -> MemberCounts {

    let target_group_full_info = groups_api::get_group(
        account, 
        target_group_id, 
        Some(false)
    ).await;

    //Get active member counts
    let online_member_count;
    let total_member_count;
    match target_group_full_info {
        Ok(info) => {
            online_member_count = info.online_member_count.unwrap();
            total_member_count = info.member_count.unwrap();
        },
        Err(_) => {
            let now = chrono::Local::now();
            let time = format!("{}", now.time().format("%H:%M"));
            eprintln!("{}: Bad response in getting target group full info. Function: get_group_member_counts()", time);
            online_member_count = -1;
            total_member_count = -1;          
        }
    }

    //let online_member_count = target_group_full_info.online_member_count.unwrap();
    //let total_member_count = target_group_full_info.member_count.unwrap();

    let member_counts = MemberCounts {
        online: online_member_count,
        total: total_member_count
    };

    member_counts
}

//Query the VRChat API and return the group id for the group in target_group file
pub async fn get_target_group_id(account: &Configuration) -> Result<String, GroupSearchResultError> {

    //Read and organize target group info for group search
    let target_group_info = get_group_info();

    //Search for target group, will return limited group
    //Search groups with or close to target group's name
    let query = target_group_info.name.as_str();
    let groups_search_result = groups_api::search_groups(
        account, 
        Some(query), 
        Some(0), 
        Some(100)
    ).await.expect("Bad response in group search. Function: get_target_group_id()");

    //Filter results for target group using the target group's short code and discriminator
    //Both group short code and discriminator are plainly visible in VRChat and on VRChat's website
    let filter_for_target_group: Vec<LimitedGroup> = groups_search_result.into_iter().filter(
        |group| 
            *group.short_code.as_ref().unwrap() == target_group_info.short_code 
            && *group.discriminator.as_ref().unwrap() == target_group_info.discriminator
            && *group.name.as_ref().unwrap() == target_group_info.name
    ).collect();

    /*Verify the target group's been found. There should only be one result
    * If we have, return the group's id.
    * If we don't, return one of three errors:
    * Multiple Matches Found
    * No Matches Found
    * Unknown Error */
    let filter_len = filter_for_target_group.len();
    if filter_len == 1 {

        let target_group = filter_for_target_group[0].to_owned();
        let target_group_id = target_group.id.to_owned().expect("Target group id not found");

        Ok(target_group_id)
    } else if filter_len == 0 {
        Err(GroupSearchResultError::NoMatchesError)
    } else if filter_len > 1 {
        Err(GroupSearchResultError::MultipleMatchesError)
    } else {
        Err(GroupSearchResultError::UnknownError)
    }
}

//Get group info from target_group file and return it in a GroupInfo struct
fn get_group_info() -> GroupInfo {
    let app_config = util::parse_json(APP_CONFIG_PATH);

    let target_group_info =  GroupInfo {
        name: app_config["basicGroupInfo"]["name"].as_str().unwrap().to_string(),
        short_code: app_config["basicGroupInfo"]["shortCode"].as_str().unwrap().to_string(),
        discriminator: app_config["basicGroupInfo"]["discriminator"].as_str().unwrap().to_string(),
    };

    target_group_info
}