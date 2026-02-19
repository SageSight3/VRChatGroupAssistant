import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class Graph(FigureCanvas):
    def __init__(self, parent, amplitude=1):
        figure, self.axes = plt.subplots(figsize=(6, 3), dpi=100)
        super().__init__(figure)
        self.setParent(parent)

        range = np.arange(0.0, 2.0, 0.01)
        fn = 1 + amplitude * np.sin(2 * np.pi * range)

        self.axes.plot(range, fn)
        self.axes.set(xlabel="x-axis", ylabel="y-axis", title="Graph")
        self.axes.grid()