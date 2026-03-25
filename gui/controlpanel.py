from PySide6.QtWidgets import QWidget

from views.ui_controlpanel import Ui_ControlPanel

class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_ControlPanel()
        self.__view.setupUi(self)