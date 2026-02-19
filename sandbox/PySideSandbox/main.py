import sys
from PySide6 import QtWidgets
from ui_sandbox import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Call the setupUi method to initialize the UI elements
        self.setupUi(self)

        self.fill_test_combo_box()
        self.testButton.clicked.connect(self.on_test_button_clicked)
        self.testButton.setText("Display Test Combo Box Selected Item")

    def on_test_button_clicked(self):
        self.testLabel.setText(
            f"index: {self.testComboBox.currentIndex()}, text: {self.testComboBox.currentText()}, data: {self.testComboBox.currentData()}"
        )

    def fill_test_combo_box(self):
        for i in range(10):
            self.testComboBox.addItem(f"Option {i}", i)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())