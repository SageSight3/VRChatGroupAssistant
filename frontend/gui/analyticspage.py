from PySide6.QtWidgets import QWidget

from gui.views.ui_analyticspage import Ui_AnalyticsPage

class AnalyticsPage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_AnalyticsPage()
        self.__view.setupUi(self)

        self.__onlinePlayerCountsTracker = self.__view.onlinePlayerCountsTracker

    def update_days_data(self, new_days_list):
        self.__onlinePlayerCountsTracker.refresh_dates_selection_box(new_days_list)
        
