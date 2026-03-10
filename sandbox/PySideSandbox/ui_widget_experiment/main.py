import sys
from PySide6 import QtWidgets
from ui_stacked_widget_test import Ui_MainWindow

from widget_ui import WidgetUI

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Call the setupUi method to initialize the UI elements
        self.setupUi(self)

        self.__widget_ui = WidgetUI(self.page_5)

        self.stackedWidget.setCurrentIndex(1) # index 1 is page_5

        self.__widget_ui.change_page.connect(self.on_change_page)

        self.toolButton.clicked.connect(self.on_tool_button_clicked)
        self.pushButton.clicked.connect(self.on_push_button_clicked)


    def on_tool_button_clicked(self):
        self.stackedWidget.setCurrentIndex(2)

    def on_push_button_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def on_change_page(self, val):
        self.stackedWidget.setCurrentIndex(val)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())