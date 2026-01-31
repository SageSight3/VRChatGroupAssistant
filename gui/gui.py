import data_parser
import grapher

def show_member_counts(date):
    target_date_member_counts_data = data_parser.get_activity_log_data(
        date, 
        ret_weekdays=True, 
        ret_dates=True,
        ret_log_entry_times=True,
        ret_online_member_counts=True,
        ret_group_total_member_counts=True
    )

    # check if there are logs for target_date
    if target_date_member_counts_data == -1:
        print("No member count logs found for " + date)
        return

    grapher.graph_member_counts(target_date_member_counts_data)

# Make buttons corresponding to each date in the activity log file
# Each button should contain the date it corresponds to that it can pass
# as an argument to show_member_counts()
def make_member_counts_date_buttons():
    dates = data_parser.get_activity_log_dates()

    # temp
    print(dates)

make_member_counts_date_buttons()

date = ""
while date != "quit":
    date = input("Enter a date in YYYY-MM-DD format or type quit to exit: ")

    # Exit if input is quit
    if date == "quit":
        break

    show_member_counts(date)