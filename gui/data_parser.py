import os.path
import re
import json

# Parses and returns activity log entry data, organized in a dictionary.
# The ret_<activity_log_entry_attr>=True params are optional that will default to True
# if no other value is provided
# If passing a date, it should be in the format: "YYYY-MM-DD"
def get_activity_log_data(
        date="", 
        ret_months=False, 
        ret_years=False, 
        ret_dates=False,
        ret_weekdays=False,
        ret_log_entry_times=False,
        ret_online_member_counts=False,
        ret_group_total_member_counts=False
):
    # Open activity log
    path = "/../data/activity_log"
    log_file = open(os.path.dirname(__file__) + path, 'r')

    # Parse log entries 
    # Map each entry to a list, with each entry split into its individual attributes
    log_file_entries = list(map(
        lambda log_entry: log_entry.strip().split(", "),
        log_file.readlines()
    ))

    log_file.close()

    # Adding this only for debug, for now, maybe can add full log graph feature later
    target_date_entries = []
    if date == "":
        # Data from all log entries will be organized and returned
        target_date_entries = log_file_entries
    else:
        # Only log entries from target date will be parsed
        target_date_entries = list(filter(
            lambda entry: entry[2] == date, log_file_entries
        ))

    # Make sure the target date is valid and has logs.
    if len(target_date_entries) < 1:
        # -1 means is being used as a generic error code here
        return -1

    # Create dictionary to hold log data to be returned
    target_date_log_data = {}

    if ret_months:
        months = list(map(lambda entry: entry[0], target_date_entries))
        target_date_log_data.update({"Months": months})

    if ret_years:
        years = list(map(lambda entry: entry[1], target_date_entries))
        target_date_log_data.update({"Years": years})

    if ret_dates:
        dates = list(map(lambda entry: entry[2], target_date_entries))
        target_date_log_data.update({"Dates": dates})
    
    if ret_weekdays:
        weekdays = list(map(lambda entry: entry[3], target_date_entries))
        target_date_log_data.update({"Weekdays": weekdays})

    if ret_log_entry_times:
        log_entry_times = list(map(lambda entry: entry[4], target_date_entries))
        target_date_log_data.update({"LogEntryTimes": log_entry_times})

    # For member counts will need to isolate and convert log entry values to ints
    # Will also converts error counts to 0s for graphing
    def format_member_count(a_member_count_str):
        member_count_vals_pattern = r"-?\d+" # match for all numbers, including negatives

        member_count = int(re.findall(member_count_vals_pattern, a_member_count_str)[0])
        if member_count == -1:
            return 0
        else:
            return member_count

    if ret_online_member_counts:
        online_member_counts = list(map(
            # regex match will only have one result
            lambda entry: format_member_count(entry[5]), 
            target_date_entries
        ))
        target_date_log_data.update({"OnlineMemberCounts": online_member_counts})

    if ret_group_total_member_counts:
        group_total_member_counts = list(map(
            # regex match will only have one result
            lambda entry: format_member_count(entry[6]),
            target_date_entries
        ))
        target_date_log_data.update({"GroupTotalMemberCounts": group_total_member_counts})

    return target_date_log_data

# Get a list of all the unique dates in ctivity log file
def get_activity_log_days():
    days = get_activity_log_data(ret_dates=True, ret_weekdays=True)

    # convert days to list of unique days from retrieved data
    # dates = list(set(dates["Dates"]))

    # list(set()) was returning the list out of order
    # so for now, doing it the old fashioned way

    sorted_days = []
    days_len = len(days["Dates"])
    for index in range(days_len):
        day = days["Dates"][index] + " " + days["Weekdays"][index]
        if day not in sorted_days:
            sorted_days.append(day)
    
    sorted_days.reverse() # have the most recent date at the top

    return sorted_days

# Get VRChat Group Assistant version number
def get_app_version():
    return get_app_config()["appVersion"]

def get_app_name():
    return get_app_config()["appName"]

# Opens and parses the app's config
def get_app_config():
    path = "/../config.json"
    app_config = open(os.path.dirname(__file__) + path, 'r')
    
    # Parse app config
    parsed_app_config = json.load(app_config)

    return parsed_app_config