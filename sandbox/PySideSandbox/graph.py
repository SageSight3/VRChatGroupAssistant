import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import random

class Graph(FigureCanvas):
    def __init__(self):
        # self.figure, self.axes = plt.subplots(figsize=(6, 3), dpi=100)
        self.__figure = plt.figure(figsize=(6, 3), constrained_layout=True)
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
        axes.plot(data)
        axes.set(xlabel="X-Axis", ylabel="Y-Axis", title="A Random Graph")
        axes.grid()
        self.draw()

    def gen_random_data(self, data_range=100):
        return [random.random() * random.random() * data_range for _i in range(24)]