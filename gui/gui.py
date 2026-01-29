import data_parser
import grapher

def show_member_counts(date):
    target_date_member_counts_data = data_parser.get_activity_log_data(date, False, False)
    grapher.graph_member_counts(target_date_member_counts_data)

date = "2026-01-28"

show_member_counts(date)