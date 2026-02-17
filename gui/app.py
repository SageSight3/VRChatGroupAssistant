import data_parser
import grapher
import tkinter as tk

def on_refresh_dates_button_clicked():
    refresh_dates_listbox()

# Will refresh dates selection menu when a corresponding button is pushed
def refresh_dates_listbox():
    # get refreshed date_options
    date_options = data_parser.get_activity_log_days()

    # clear dates listbox
    dates_listbox.delete(0, tk.END)

    for option in date_options:
        dates_listbox.insert(tk.END, option)

def on_graph_dates_button_clicked():
    # get selected index
    selected_index = dates_listbox.curselection()

    # if no index is selected, return
    if not selected_index:
        return

    # parse the date from the selected date option label
    # refactor to have separate dates list in future?
    target_date = dates_listbox.get(selected_index).split(" ")[0]
    graph_member_counts(target_date)

def on_graph_percents_button_clicked():
        # get selected index
    selected_index = dates_listbox.curselection()

    # if no index is selected, return
    if not selected_index:
        return

    # parse the date from the selected date option label
    # refactor to have separate dates list in future?
    target_date = dates_listbox.get(selected_index).split(" ")[0]
    graph_member_counts(target_date, is_percents=True)

# Opens a graph of online and total member counts
def graph_member_counts(date, is_percents=False):
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

    if is_percents: # if showing percents graph
        graph_data: grapher.PercentsGraphData = generate_percents_graph_data(target_date_member_counts_data)
        grapher.graph_percents(graph_data)
    else:
        graph_data: grapher.GraphData = generate_graph_data(target_date_member_counts_data)
        grapher.graph_member_counts(graph_data)

# Instead of graphing activity log data directly from 
# passed in log entries, create a data point for the top
# of every hour in the day, and assign the corresponding log
# entry data to it's respective time slot. This will cause
# the graph to display bars for every hour, even if there isn't
# log data for that hour. Missing hours should have their
# member counts read "0" or "N/A"
def generate_graph_data(target_date_log_data) -> grapher.GraphData:

    weekday = target_date_log_data["Weekdays"][0]
    date = target_date_log_data["Dates"][0]
    graph_title = f"{weekday} {date}"

    target_date_data = {
        "Timestamps": [timestamp for timestamp in target_date_log_data["LogEntryTimes"]],
        "OnlineCounts": [online_count for online_count in target_date_log_data["OnlineMemberCounts"]],
        "TotalCounts": [total_count for total_count in target_date_log_data["GroupTotalMemberCounts"]]
    }

    graph_data = grapher.GraphData(graph_title, target_date_data)

    return graph_data

# Same as generate graphd data, but generates activity percets graph data instead
def generate_percents_graph_data(target_date_log_data) -> grapher.GraphData:

    weekday = target_date_log_data["Weekdays"][0]
    date = target_date_log_data["Dates"][0]
    graph_title = f"{weekday} {date}"

    percents = []
    for index in range(0, len(target_date_log_data["Dates"])):
        if target_date_log_data["GroupTotalMemberCounts"][index] == 0:
            percents.append(0)
            continue
        percent = target_date_log_data["OnlineMemberCounts"][index] / target_date_log_data["GroupTotalMemberCounts"][index]
        percent = int(round(percent, 2) * 100)
        percents.append(percent)

    target_date_data = {
        "Timestamps": [timestamp for timestamp in target_date_log_data["LogEntryTimes"]],
        "Percents": percents
    }

    graph_data = grapher.PercentsGraphData(graph_title, target_date_data)

    return graph_data

# Get app version num
def get_app_version():
    return data_parser.get_app_version()

# Get app name
def get_app_name():
    return data_parser.get_app_name()

# Initialize app window
window_root = tk.Tk()
window_root.title(get_app_name() + " " + get_app_version())
window_root.geometry("400x400")

# Dates Listbox Frame
dates_listbox_frame = tk.Frame(window_root)

dates_listbox = tk.Listbox(dates_listbox_frame, selectmode=tk.SINGLE)
refresh_dates_listbox()
dates_listbox_label = tk.Label(dates_listbox_frame, text="Select a Date")

dates_listbox_scrollbar = tk.Scrollbar(dates_listbox_frame)

dates_listbox.config(yscrollcommand=dates_listbox_scrollbar.set)
dates_listbox_scrollbar.config(command=dates_listbox.yview)

dates_listbox_label.pack(side=tk.TOP, anchor=tk.NW)
dates_listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
dates_listbox.pack(side=tk.TOP, anchor=tk.NW)

# Refresh Dates and Graph Member Counts Buttons
refresh_dates_button = tk.Button(window_root, text="Refresh Dates", command=on_refresh_dates_button_clicked)
graph_dates_button = tk.Button(window_root, text="Graph Member Counts", command=on_graph_dates_button_clicked)
graph_percents_button = tk.Button(window_root, text="Graph Member Counts as Percents", command=on_graph_percents_button_clicked)

dates_listbox_frame.pack(side=tk.TOP, anchor=tk.NW)
refresh_dates_button.pack(side=tk.TOP, anchor=tk.NW)
graph_dates_button.pack(side=tk.TOP, anchor=tk.NW)
graph_percents_button.pack(side=tk.TOP, anchor=tk.NW)

window_root.mainloop()