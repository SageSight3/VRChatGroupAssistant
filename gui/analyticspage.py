from PySide6.QtWidgets import QWidget

from views.ui_analyticspage import Ui_AnalyticsPage

class AnalyticsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_AnalyticsPage()
        self.__view.setupUi(self)