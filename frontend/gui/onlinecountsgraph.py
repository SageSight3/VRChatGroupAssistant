import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class OnlineCountsGraph(FigureCanvas):
    def __init__(self):
        self.__figure = plt.figure(figsize=(6, 3), constrained_layout=True)
        super().__init__(self.__figure)

        self.graph_online_counts()

    def graph_online_counts(self):
        # Clear old graph
        self.__figure.clear()

        # VRCGA_GUI_TEST
        axes = self.__figure.add_subplot(111)
        spine_linewidth = 0.25
        axes.spines['bottom'].set_linewidth(spine_linewidth)
        axes.spines['top'].set_linewidth(spine_linewidth)
        axes.spines['left'].set_linewidth(spine_linewidth)
        axes.spines['right'].set_linewidth(spine_linewidth)

        axes.set_title("A Random Graph")
        axes.set_xlabel("x-axis")
        axes.set_ylabel("y-axis")

        import random
        def gen_random_data(data_range=100):
            return [random.random() * random.random() * data_range for _i in range(24)]
        
        axes.plot(gen_random_data())
        axes.grid()
        self.draw()