import data_parser
import grapher
import tkinter as tk

def on_refresh_dates_button_clicked():
    refresh_dates_listbox()

# Will refresh dates selection menu when a corresponding button is pushed
def refresh_dates_listbox():
    # get refreshed date_options
    date_options = data_parser.get_activity_log_dates()

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

    target_date = dates_listbox.get(selected_index)
    show_member_counts(target_date)

# Opens a graph of online and total member counts
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

# Initialize app window
window_root = tk.Tk()
window_root.title("VRChat Group Assistant")
window_root.geometry("400x400")

dates_listbox = tk.Listbox(window_root, selectmode=tk.SINGLE)
refresh_dates_listbox()
dates_listbox_label = tk.Label(window_root, text="Select a Date")

refresh_dates_button = tk.Button(window_root, text="Refresh Dates", command=on_refresh_dates_button_clicked)

graph_dates_button = tk.Button(window_root, text="Show Member Counts Graph", command=on_graph_dates_button_clicked)

refresh_dates_button.pack(side=tk.TOP, anchor=tk.NW)
dates_listbox_label.pack(side=tk.TOP, anchor=tk.NW)
dates_listbox.pack(side=tk.TOP, anchor=tk.NW)
graph_dates_button.pack(side=tk.TOP, anchor=tk.NW)

window_root.mainloop()