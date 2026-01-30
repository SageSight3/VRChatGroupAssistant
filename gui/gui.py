import data_parser
import grapher

def show_member_counts(date):
    target_date_member_counts_data = data_parser.get_activity_log_data(date, False, False)
    # check if there are logs for target_date
    if target_date_member_counts_data == -1:
        print("No member count logs found for " + date)
        return

    grapher.graph_member_counts(target_date_member_counts_data)

date = ""
while date != "quit":
    date = input("Enter a date in YYYY-MM-DD format or type quit to exit: ")

    # Exit if input is quit
    if date == "quit":
        break

    show_member_counts(date)