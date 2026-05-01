import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import mplcursors

graph_face_color = "#1E1E1E"
graph_font_color = "white"

class OnlineCountsGraph(FigureCanvas):

    __timestampLabels = [f"{hour:02d}:00" for hour in range(0, 24)]

    def __init__(self):
        self.__figure = plt.figure(figsize=(6, 3), constrained_layout=True)
        self.__figure.set_facecolor(graph_face_color)
        self.__figure.set_edgecolor(graph_font_color)
        super().__init__(self.__figure)

    def update_graph(self, new_graph_data, show_percents=True, show_member_counts=True):

        show_all_bars = show_percents and show_member_counts

        self.__figure.clear()
        axes = self.__figure.add_subplot(111)
        self.style_graph(axes)
        axes.set_title(new_graph_data.graph_title, color=graph_font_color)

        # Setup x axis
        axes.set_xlabel("Time", color=graph_font_color)
        bar_group_locations = np.arange(len(new_graph_data.graph_timestamps))
        bar_width = 0.3

        # center x tick labels relative to their respective bar groups
        xtick_label_offset = 0
        if show_all_bars: 
            xtick_label_offset = (bar_width/2) * (3/2) # centers label between 3 bars
        elif show_member_counts:
            xtick_label_offset = bar_width/2 # centers label between 2 bars

        axes.set_xticks(bar_group_locations + xtick_label_offset, new_graph_data.graph_timestamps)

        # Add bars
        if show_member_counts:
            self.graph_member_counts(axes, bar_group_locations, bar_width, new_graph_data)

        if show_percents:
            if show_all_bars:
                self.graph_online_percents(axes, bar_group_locations, bar_width, new_graph_data)
            else:
                bar_width = bar_width * 2 # since this means we're only showing 1 bar, make it thicker
                self.graph_online_percents(axes, bar_group_locations, bar_width, new_graph_data, member_counts_bars=False)

        # Add a legend
        self.__figure.legend(
            loc="upper left",
            ncols=2, 
            labelcolor=graph_font_color, 
            edgecolor=graph_font_color, 
            facecolor=graph_face_color
        )
        
        # Redraw the graph
        self.draw()

    def style_graph(self, axes):
        axes.set_facecolor(graph_face_color)

        spine_linewidth = 0.25
        axes.spines['bottom'].set_linewidth(spine_linewidth)
        axes.spines['top'].set_linewidth(spine_linewidth)
        axes.spines['left'].set_linewidth(spine_linewidth)
        axes.spines['right'].set_linewidth(spine_linewidth)
        
        axes.spines['bottom'].set_color(graph_font_color)
        axes.spines['top'].set_color(graph_font_color)
        axes.spines['left'].set_color(graph_font_color)
        axes.spines['right'].set_color(graph_font_color)

        axes.tick_params(labelcolor=graph_font_color)
        plt.xticks(rotation=70) # rotate x-tick labels to fit better
        
    def graph_member_counts(self, axes, bar_group_locations, bar_width, graph_data):

        # Member Counts bars will always be first, so we can just use axes y-axis, as their y-axis, to simplify styling
        member_counts_axes = axes
        member_counts_axes.set_ylabel("Member Count", color=graph_font_color)
        member_counts_axes.tick_params(labelcolor=graph_font_color) # for y-axis labels

        online_count_bar_locations = bar_group_locations
        online_member_counts_bar = axes.bar(
            online_count_bar_locations,
            graph_data.online_counts,
            bar_width,
            label="Online"
        )

        total_count_bar_locations = bar_group_locations + bar_width
        group_total_member_counts_bar = axes.bar(
            total_count_bar_locations,
            graph_data.total_counts,
            bar_width,
            label="Total"
        )

        # Make it so bar label will only appear when the bar is hovered over
        online_cursor = mplcursors.cursor(online_member_counts_bar, hover=mplcursors.HoverMode.Transient)

        @online_cursor.connect("add")
        def online_on_hover(selection):
            self.on_hover(selection, labels=graph_data.online_bar_labels)

        totals_cursor = mplcursors.cursor(group_total_member_counts_bar, hover=mplcursors.HoverMode.Transient)

        @totals_cursor.connect("add")
        def totals_on_hover(selection):
            self.on_hover(selection, labels=graph_data.total_bar_labels)

        member_counts_axes.plot()

    def graph_online_percents(self, axes, bar_group_locations, bar_width, graph_data, member_counts_bars=True):
        # If the percents bar is the only one being graphed, its y-axis can just be the main axes' y-axis.
        # If the member counts bars are also being graphed, though, the percents bar will need a seperate y-axis, even
        # if its still using the same x-axis.
        percents_axes = axes
        if member_counts_bars:
            percents_axes = axes.twinx()

        percents_axes.set_ylabel("Percentage of Members Online", color=graph_font_color)
        percents_axes.tick_params(labelcolor=graph_font_color)
        percents_axes.yaxis.set_major_formatter(PercentFormatter(decimals=0))

        percent_bar_locations = bar_group_locations
        # If member counts bars are also in graph, shift percent bar locations to be next to them on the right
        if member_counts_bars: percent_bar_locations = percent_bar_locations + bar_width * 2

        group_online_percents_bar = percents_axes.bar(
            percent_bar_locations,
            graph_data.percents,
            bar_width,
            label="Percents",
            color="green"
        )

        online_percents_cursor = mplcursors.cursor(group_online_percents_bar, hover=mplcursors.HoverMode.Transient)

        @online_percents_cursor.connect("add")
        def online_percents_on_hover(selection):
            self.on_hover(selection, labels=graph_data.percent_bar_labels)

        percents_axes.plot()

    # Make it so bars will show their value when hovered over with cursor
    def on_hover(self, selection, labels):
        index = selection.index
        artist = selection.artist
        height = selection.artist[index].get_height()
        sel_annotation = selection.annotation
        sel_annotation.set(text=f"{labels[index]}", position=(0, 2), anncoords="offset points", color=graph_font_color)
        sel_annotation.xy = (artist[index].get_x() + artist[index].get_width() / 2, height)

        # remove annotation arrow and bounding box
        if sel_annotation.arrow_patch:
            sel_annotation.arrow_patch.set_visible(False)

        sel_bbox_patch = selection.annotation.get_bbox_patch()
        sel_bbox_patch.set_edgecolor(graph_font_color)
        sel_bbox_patch.set_facecolor(graph_face_color)
        sel_bbox_patch.set_linewidth(0.5)
        sel_bbox_patch.set(alpha=1.0)