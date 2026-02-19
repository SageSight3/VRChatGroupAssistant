import sys
from PySide6 import QtWidgets
from ui_sandbox import Ui_MainWindow

import graph
import random

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Call the setupUi method to initialize the UI elements
        self.setupUi(self)

        self.fill_test_combo_box()
        self.graphButton.clicked.connect(self.on_graph_button_clicked)
        self.newValsButton.clicked.connect(self.on_new_vals_button_clicked)
        self.testComboBox.currentIndexChanged.connect(self.display_selected_item_data)

        self.display_selected_item_data()

        self.__graph = graph.Graph()
        self.testWidgetMainLayout.addWidget(self.__graph)

    def on_new_vals_button_clicked(self):
        self.testComboBox.clear()
        self.fill_test_combo_box()
        self.display_selected_item_data()

    def on_graph_button_clicked(self):
        data_range = self.testComboBox.currentData()
        if data_range == None:
            return
        self.__graph.change(new_data_range=data_range)

    def display_selected_item_data(self):
        self.testLabel.setText(
            f"index: {self.testComboBox.currentIndex()}, text: {self.testComboBox.currentText()}, data: {self.testComboBox.currentData()}"
        )

    def fill_test_combo_box(self):
        for i in range(10):
            data = (i + 1) * random.random() * 100
            self.testComboBox.addItem(f"Option {i}", data)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())