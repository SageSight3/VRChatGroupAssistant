import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import random

graph_face_color = "#1E1E1E"
graph_font_color = "white"

class Graph(FigureCanvas):
    def __init__(self):
        # self.figure, self.axes = plt.subplots(figsize=(6, 3), dpi=100)
        self.__figure = plt.figure(figsize=(6, 3), constrained_layout=True)
        self.__figure.set_facecolor(graph_face_color)
        self.__figure.set_edgecolor(graph_font_color)
        super().__init__(self.__figure)
        # self.setParent(parent)
        
        data = self.gen_random_data()

        self.plot(data)

    def change(self, new_data_range=100):
        data = self.gen_random_data(data_range=new_data_range)
        self.__figure.clear()
        self.plot(data)

    def plot(self, data):
        axes = self.__figure.add_subplot(111)
        axes.set_facecolor(graph_face_color)

        axes.spines['bottom'].set_color(graph_font_color)
        axes.spines['top'].set_color(graph_font_color)
        axes.spines['left'].set_color(graph_font_color)
        axes.spines['right'].set_color(graph_font_color)

        spine_linewidth = 0.25
        axes.spines['bottom'].set_linewidth(spine_linewidth)
        axes.spines['top'].set_linewidth(spine_linewidth)
        axes.spines['left'].set_linewidth(spine_linewidth)
        axes.spines['right'].set_linewidth(spine_linewidth)

        axes.set_title("A Random Graph", color=graph_font_color)
        axes.set_xlabel("x-axis", color=graph_font_color)
        axes.set_ylabel("y-axis", color=graph_font_color)
        axes.tick_params(labelcolor=graph_font_color)
        axes.plot(data)
        axes.grid()
        self.draw()

    def gen_random_data(self, data_range=100):
        return [random.random() * random.random() * data_range for _i in range(24)]