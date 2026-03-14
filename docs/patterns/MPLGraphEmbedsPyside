# Embedding a Matplotlib Graph in a PySide GUI Application

### Problem
Make a matplotlib graph more accessible and presentable in a PySide GUI application.

### Solution
To make matplotlib graphs more presentable in an application, matplotlib supports embedding their graphs in various GUI frameworks, including PySide.

To do so, add a Qt layout (any will work) to the GUI to be a container for the graph in the intended gui view.. This layout can be added in either QtDesigner or in the class directly. Then, write a class to create your graph that as a subclass of FigureCanvasQtAgg (from `matplotlib.backends.backend_qtagg`).

Lastly, create an object in the intended gui view's class to hold onto your matplotlib graph, and add it to the container layout.

**Example**
<br>
mainwindow.py
```python
from PySide6.QtWidgets import QMainWindow

from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.__view = Ui_MainWindow()
        self.__view.setupUi(self)

        # Create graph object
        self.__graph = graph.Graph()

        # Add the graph to a container layout in your GUI
        self.__view.testWidgetMainLayout.addWidget(self.__graph)
```
graph.py
```python
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import random

class Graph(FigureCanvas):
    def __init__(self):
        self.__figure = plt.figure(figsize=(6, 3), constrained_layout=True)
        super().__init__(self.__figure)
        
        data = self.gen_random_data()

        self.plot(data)

    def plot(self, data):
        axes = self.__figure.add_subplot(111)

        axes.plot(data)
        axes.grid()
        self.draw()

    def gen_random_data(self, data_range=100):
        return [random.random() * random.random() * data_range for _i in range(24)]
    ```