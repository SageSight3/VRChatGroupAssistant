use tokio_cron_scheduler::{JobScheduler, Job};
use tokio;

mod modules;
use modules::auth;
use modules::group_info;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {

    let account_main = auth::login().await;

    //Print VRGroupAssistant version num
    let version_str = account_main.user_agent.clone().unwrap();
    let version_str = version_str.split(" ").collect::<Vec<&str>>()[0];
    println!("{}", version_str);

    //Get target group id. Panic, if error
    let target_group_id_search = group_info::get_target_group_id(&account_main.clone()).await;
    let target_group_id: String;
    match target_group_id_search  {
        Ok(id) => target_group_id = id,
        Err(err) => {
            eprintln!("Error: {:?}", err);
            panic!();
        }
    }

    //Initialize api query schedule
    let api_query_schedule = JobScheduler::new().await?;

    //Create job for logging member counts
    let log_member_counts_job = Job::new_async(
        "0 0 * * * *",
        move |_uuid, _locked| {
            Box::pin({
                //clone account and target group id to new variables to move into the closure
                let log_activity_account= account_main.clone();
                let log_activity_group_id = target_group_id.clone();
                async move {
                    group_info::log_group_member_counts(
                        &log_activity_account, 
                        &log_activity_group_id.as_str()
                    ).await;                
                }
            })
        }
    )?;

    api_query_schedule.add(log_member_counts_job).await?;

    api_query_schedule.start().await?;

    tokio::signal::ctrl_c().await?;

    Ok(())
}
