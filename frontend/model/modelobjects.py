timestamps = [f"{hour:02d}:00" for hour in range(0, 24)]

class OnlineCountTrackerData:

    def __init__(self, online: int, total: int, percent: int, timestamp: str):

        # Inst vars are public, since this class is just meant to be a
        # data container
        self.online_count = online
        self.total_count = total
        self.online_percent = percent
        self.timestamp = timestamp

class OnlineCrountsGraphData:

    graph_timestamps = timestamps # done this way, so future model objects can also use timestamps
    
    def __init__(self, graph_title, online_counts_data: OnlineCountTrackerData):
        self.show_member_counts = True
        self.show_online_percents = False
        self.set_mpl_graph_data(graph_title, online_counts_data)

    def set_mpl_graph_data(self, graph_title, online_counts_data: OnlineCountTrackerData):
        self.graph_title = graph_title

        # Initialize default graph data
        bar_not_found_label = "0"
        self.online_bar_labels = [bar_not_found_label for _hour in self.graph_timestamps]
        self.total_bar_labels = [bar_not_found_label for _hour in self.graph_timestamps]

        bar_not_found_label = "0%"
        self.percent_bar_labels = [bar_not_found_label for _hour in self.graph_timestamps]
        
        self.percents = [0 for _hour in self.graph_timestamps]
        self.online_counts = [0 for _hour in self.graph_timestamps]
        self.total_counts = [0 for _hour in self.graph_timestamps]

        # Change default values to their respective values in target_date_data
        for data_index in range(0, len(online_counts_data)):
            # Find index in graph timestamps of data point (log entry) timestamp
            data_point_timestamp = online_counts_data[data_index].timestamp

            # if for whatever reason, data_point timestamp isn't at the top of the hour
            # skip it
            data_point_timestamp_minutes = data_point_timestamp[3:] # 00:00
            if data_point_timestamp_minutes != "00":
                continue

            graph_index = timestamps.index(data_point_timestamp)

            # Update graph data values
            data_point_online_count = online_counts_data[data_index].online_count
            data_point_total_count = online_counts_data[data_index].total_count
            data_point_percent = online_counts_data[data_index].online_percent

            self.online_bar_labels[graph_index] = str(data_point_online_count)
            self.total_bar_labels[graph_index] = str(data_point_total_count)
            self.online_counts[graph_index] = data_point_online_count
            self.total_counts[graph_index] = data_point_total_count
            self.percent_bar_labels[graph_index] = str(data_point_percent) + "%"
            self.percents[graph_index] = data_point_percent       

class Day(object):
    
    def __init__(self, a_date, a_weekday, an_index):
        
        self.date: str = a_date
        self.weekday: str = a_weekday
        self.index: int = an_index