from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot

from gui.views.ui_analyticspage import Ui_AnalyticsPage

class AnalyticsPage(QWidget):
    
    from vrcga_signals import (
        selectedDayChanged,
        showOnlinePercentsChanged,
        showMemberCountsChanged
    )

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_AnalyticsPage()
        self.__view.setupUi(self)

        self.__onlinePlayerCountsTracker = self.__view.onlinePlayerCountsTracker

        self.setup_connections()

    def setup_connections(self):
        self.__onlinePlayerCountsTracker.selectedDayChanged.connect(self.change_selected_day)
        self.__onlinePlayerCountsTracker.showMemberCountsChanged.connect(self.change_show_member_counts)
        self.__onlinePlayerCountsTracker.showOnlinePercentsChanged.connect(self.change_show_online_percents)
    
    @Slot(int)
    def change_selected_day(self, model_day_index):
        self.selectedDayChanged.emit(model_day_index)
        
    @Slot(object)
    def change_show_member_counts(self, check_state):
        self.showMemberCountsChanged.emit(check_state)

    @Slot(object)
    def change_show_online_percents(self, check_state):
        self.showOnlinePercentsChanged.emit(check_state)

    def update_days_data(self, new_days_list):
        self.__onlinePlayerCountsTracker.refresh_dates_selection_box(new_days_list)

    def update_selected_day(self, new_day):
        self.__onlinePlayerCountsTracker.update_selected_day(new_day)

    def update_online_counts_graph(self, new_data):
        self.__onlinePlayerCountsTracker.update_graph(new_data)
        
