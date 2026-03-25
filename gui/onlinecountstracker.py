from PySide6.QtWidgets import QWidget

from views.ui_onlinecountstracker import Ui_OnlineCountsTracker

class OnlineCountsTracker(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_OnlineCountsTracker()
        self.__view.setupUi(self)