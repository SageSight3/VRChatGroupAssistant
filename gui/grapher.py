import matplotlib.pyplot as plt
import numpy as np

# Creates and opens a matplotlib bar graph of member count data
# from the passed in log data
def graph_member_counts(target_date_log_data):

    # Setup window
    window, axes = plt.subplots(layout='constrained')
    window.canvas.manager.set_window_title("Active Member Counts")

    # Set graph attributes
    graph_title = target_date_log_data["Weekdays"][0] + " " + target_date_log_data["Dates"][0]
    axes.set_title(graph_title)

    axes.set_ylabel("Member Count")
    axes.set_xlabel("Time")

    bar_group_locations = np.arange(len(target_date_log_data["LogEntryTimes"]))
    bar_width = 0.3

    # Set labels and label positioning for each tick on the x-axis
    # tick labels should be centered between their respective bars
    axes.set_xticks(bar_group_locations + bar_width/2, target_date_log_data["LogEntryTimes"])

    # Create bars
    online_member_counts_bar = axes.bar(
        bar_group_locations,
        target_date_log_data["OnlineMemberCounts"],
        bar_width,
        label="Online"
    )

    offset = bar_group_locations + bar_width
    group_total_member_counts_bar = axes.bar(
        offset,
        target_date_log_data["GroupTotalMemberCounts"],
        bar_width,
        label="Total"
    )

    # Add labels of each bar's exact value above them
    axes.bar_label(online_member_counts_bar, padding=3)
    axes.bar_label(group_total_member_counts_bar, padding=3)

    # Increase y-axis limit to give more room
    axes.set_ylim(0, max(target_date_log_data["GroupTotalMemberCounts"]) + 50)

    # Add a legend
    axes.legend(loc="upper left", ncols=2)

    plt.show()