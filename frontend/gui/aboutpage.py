from PySide6.QtWidgets import QWidget

from gui.views.ui_aboutpage import Ui_AboutPage

class AboutPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_AboutPage()
        self.__view.setupUi(self)