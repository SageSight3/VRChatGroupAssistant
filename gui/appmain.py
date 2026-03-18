from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot

from views.ui_appmain import Ui_AppMain

class AppMain(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_AppMain()
        self.__view.setupUi(self)