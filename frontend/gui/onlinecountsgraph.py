import matplotlib.pyplot as plt
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

        # Initialize Graph Attributes

        self.__title = ""

        self.__online_bar_labels: list[str] = []
        self.__total_bar_labels: list[str] = []

        self.__online_counts: list[int] = []
        self.__total_counts: list[int] = []

        # max height of the graph
        self.__y_lim: int = 0

    def update_graph(self, new_graph_data):
        self.graph_online_counts(new_graph_data)

    def graph_online_counts(self, new_graph_data):
        # Clear old graph
        self.__figure.clear()

        # Set graph style attributes
        axes = self.__figure.add_subplot(111)
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

        axes.set_title("A Random Graph", color=graph_font_color)
        axes.set_xlabel("x-axis", color=graph_font_color)
        axes.set_ylabel("y-axis", color=graph_font_color)
        axes.tick_params(labelcolor=graph_font_color)

        # Set graph data
        axes.set_title(new_graph_data.graph_title)
        axes.set_xlabel("Time")
        axes.set_ylabel("Member Count")

        bar_group_locations = np.arange(len(new_graph_data.graph_timestamps))
        bar_width = 0.3

        # Set labels and label positioning for each tick on the x-axis
        # tick labels should be centered between their respective bars
        axes.set_xticks(bar_group_locations + bar_width/2, new_graph_data.graph_timestamps)
        plt.xticks(rotation=70) # rotate x-tick labels to fit better

        # Create bars
        online_member_counts_bar = axes.bar(
            bar_group_locations,
            new_graph_data.online_counts,
            bar_width,
            label="Online"
        )

        offset = bar_group_locations + bar_width
        group_total_member_counts_bar = axes.bar(
            offset,
            new_graph_data.total_counts,
            bar_width,
            label="Total"
        )

        # Add a legend
        axes.legend(
            loc="upper left",
            ncols=2, 
            labelcolor=graph_font_color, 
            edgecolor=graph_font_color, 
            facecolor=graph_face_color,
        )

        # Make it so bar label will only appear when the bar is hovered over
        online_cursor = mplcursors.cursor(online_member_counts_bar, hover=mplcursors.HoverMode.Transient)

        @online_cursor.connect("add")
        def online_on_hover(selection):
            self.on_hover(selection, labels=new_graph_data.online_bar_labels)

        totals_cursor = mplcursors.cursor(group_total_member_counts_bar, hover=mplcursors.HoverMode.Transient)

        @totals_cursor.connect("add")
        def totals_on_hover(selection):
            self.on_hover(selection, labels=new_graph_data.total_bar_labels)

        axes.plot()
        self.draw()

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