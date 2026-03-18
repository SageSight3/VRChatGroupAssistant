from PySide6.QtWidgets import QWidget

from views.ui_mainwidget import Ui_MainWidget

class MainWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__appGui = Ui_MainWidget()
        self.__appGui.setupUi(self)

        self.__loginWidget = self.__appGui.login
        



