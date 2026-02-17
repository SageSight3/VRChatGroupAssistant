import matplotlib.pyplot as plt
import numpy as np
import matplotlib.widgets as widgets
import tkinter as tk

class GraphData:

    # Graph timestamps
    timestamps = [f"{hour:02d}:00" for hour in range(0, 24)]

    def __init__(self, graph_title, target_date_data):

        self.__title = graph_title
        
        # Initialize default graph data
        bar_not_found_label = "0"
        self.__online_bar_labels = [bar_not_found_label for _hour in GraphData.timestamps]
        self.__total_bar_labels = [bar_not_found_label for _hour in GraphData.timestamps]

        self.__online_counts = [0 for _hour in GraphData.timestamps]
        self.__total_counts = [0 for _hour in GraphData.timestamps]

        # Change default values to their respective values in target_date_data
        for data_index in range(0, len(target_date_data["Timestamps"])):
            # Find index in graph timestamps of data point (log entry) timestamp
            data_point_timestamp = target_date_data["Timestamps"][data_index]

            # if for whatever reason, data_point timestamp isn't at the top of the hour
            # skip it
            data_point_timestamp_minutes = data_point_timestamp[3:] # 00:00
            if data_point_timestamp_minutes != "00":
                continue

            graph_index = GraphData.timestamps.index(data_point_timestamp)

            # Update graph data values
            data_point_online_count = target_date_data["OnlineCounts"][data_index]
            data_point_total_count = target_date_data["TotalCounts"][data_index]

            self.__online_bar_labels[graph_index] = str(data_point_online_count)
            self.__total_bar_labels[graph_index] = str(data_point_total_count)
            self.__online_counts[graph_index] = data_point_online_count
            self.__total_counts[graph_index] = data_point_total_count

        self.__y_lim = max(self.__total_counts) + 50

    def get_online_counts(self):
        return self.__online_counts
    
    def get_total_counts(self):
        return self.__total_counts

    def get_online_bar_labels(self):
        return self.__online_bar_labels
    
    def get_total_bar_labels(self):
        return self.__total_bar_labels
    
    def get_title(self):
        return self.__title
    
    def get_timestamps(self):
        return self.timestamps

    def get_ylim(self):
        return self.__y_lim

class PercentsGraphData:

    # Graph timestamps
    timestamps = [f"{hour:02d}:00" for hour in range(0, 24)]

    def __init__(self, graph_title, target_date_data):

        self.__title = graph_title
        
        # Initialize default graph data
        bar_not_found_label = "0%"
        self.__percent_bar_labels = [bar_not_found_label for _hour in PercentsGraphData.timestamps]

        self.__percents = [0 for _hour in PercentsGraphData.timestamps]

        # Change default values to their respective values in target_date_data
        for data_index in range(0, len(target_date_data["Timestamps"])):
            # Find index in graph timestamps of data point (log entry) timestamp
            data_point_timestamp = target_date_data["Timestamps"][data_index]

            # if for whatever reason, data_point timestamp isn't at the top of the hour
            # skip it
            data_point_timestamp_minutes = data_point_timestamp[3:] # 00:00
            if data_point_timestamp_minutes != "00":
                continue

            graph_index = PercentsGraphData.timestamps.index(data_point_timestamp)

            # Update graph data values
            data_point_percent = target_date_data["Percents"][data_index]

            self.__percent_bar_labels[graph_index] = str(data_point_percent) + "%"
            self.__percents[graph_index] = data_point_percent

        self.__y_lim = max(self.__percents) + 5

    def get_percents(self):
        return self.__percents

    def get_percents_bar_labels(self):
        return self.__percent_bar_labels
    
    def get_title(self):
        return self.__title
    
    def get_timestamps(self):
        return self.timestamps

    def get_ylim(self):
        return self.__y_lim
# Creates and opens a matplotlib bar graph of member count data
# from the passed in log data.
# Make graph scrollable: https://www.geeksforgeeks.org/python/python-scroll-through-plots/
def graph_member_counts(graph_data: GraphData):

    # Setup window
    # Ensure fig size is large enough to show a graph of at least 24 entries
    window, axes = plt.subplots(figsize=(12, 5), layout='constrained')
    window.canvas.manager.set_window_title("Active Member Counts")

    # Set graph to open as a full screen window
    plt.get_current_fig_manager()

    # Set graph attributes
    graph_title = graph_data.get_title()
    axes.set_title(graph_title)

    axes.set_ylabel("Member Count")
    axes.set_xlabel("Time")

    bar_group_locations = np.arange(len(graph_data.get_timestamps()))
    bar_width = 0.35

    # Set labels and label positioning for each tick on the x-axis
    # tick labels should be centered between their respective bars
    axes.set_xticks(bar_group_locations + bar_width/2, graph_data.get_timestamps())
    plt.xticks(rotation=70) # rotate x-tick labels to fit better

    # Create bars
    online_member_counts_bar = axes.bar(
        bar_group_locations,
        graph_data.get_online_counts(),
        bar_width,
        label="Online"
    )

    offset = bar_group_locations + bar_width
    group_total_member_counts_bar = axes.bar(
        offset,
        graph_data.get_total_counts(),
        bar_width,
        label="Total"
    )

    # Add labels of each bar's exact value above them
    bar_label_font_size = 10
    axes.bar_label(online_member_counts_bar, labels=graph_data.get_online_bar_labels(), fontsize=bar_label_font_size, padding=3)
    axes.bar_label(group_total_member_counts_bar, labels=graph_data.get_total_bar_labels(), fontsize=bar_label_font_size, padding=3)

    # Increase y-axis limit to give more room
    axes.set_ylim(0, graph_data.get_ylim())

    # Add a legend
    axes.legend(loc="upper left", ncols=2)

    plt.show()

# Same as graph member counts, but displays data as percentage of group total
# member count, online, at every timestamp instead
def graph_percents(graph_data: PercentsGraphData):

    # Setup window
    # Ensure fig size is large enough to show a graph of at least 24 entries
    window, axes = plt.subplots(figsize=(12, 5), layout='constrained')
    window.canvas.manager.set_window_title("Active Member Counts As Percentages of Group Size")

    # Set graph to open as a full screen window
    plt.get_current_fig_manager()

    # Set graph attributes
    graph_title = graph_data.get_title()
    axes.set_title(graph_title)

    axes.set_ylabel("Percentage of Total Members Online")
    axes.set_xlabel("Time")

    bar_location = np.arange(len(graph_data.get_timestamps()))
    bar_width = 0.5

    # Set labels and label positioning for each tick on the x-axis
    # tick labels should be centered between their respective bars
    axes.set_xticks(bar_location, graph_data.get_timestamps())
    plt.xticks(rotation=70) # rotate x-tick labels to fit better

    # Create bar
    percents_bar = axes.bar(
        bar_location,
        graph_data.get_percents(),
        bar_width,
        label="Percents"
    )

    # Add labels of each bar's exact value above them
    bar_label_font_size = 10
    axes.bar_label(percents_bar, labels=graph_data.get_percents_bar_labels(), fontsize=bar_label_font_size, padding=3)

    # Increase y-axis limit to give more room
    axes.set_ylim(0, graph_data.get_ylim())

    plt.show()