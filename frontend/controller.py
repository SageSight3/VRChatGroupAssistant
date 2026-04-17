import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Slot

from gui.mainwidget import MainWidget
from model.model import Model
from model.modelobjects import *

class Controller():

    # Initialize frontend app components
    def __init__(self, args):
        self.__qapp = QApplication(args)

        self.__gui = MainWidget()
        self.__model = Model()

        self.setup_connections()
        self.set_launch_state()

    def setup_connections(self):

        # GUI Connections

        self.__gui.logout.connect(self.log_out)
        self.__gui.refreshAnalyticsData.connect(self.refresh_analytics_gui_data)
        self.__gui.selectedDayChanged.connect(self.change_selected_day)
        
        # Model Connections
        self.__model.refreshedDaysList.connect(self.update_days_in_gui)
        self.__model.refreshedOnlineCountsGraphData.connect(self.update_online_counts_graph)
        self.__model.updatedSelectedDay.connect(self.update_selected_day_in_gui)

    def set_launch_state(self):
        # Pass model data to GUI on launch
        self.refresh_analytics_gui_data()

    @Slot()
    def log_out(self):
        # reset the GUI back to launch state login screen
        self.__gui.set_launch_state()

        # TODO: Clear session data

    @Slot()
    def refresh_analytics_gui_data(self):
        self.__model.update_data()

    @Slot(int)
    def change_selected_day(self, model_day_index):
        self.__model.update_selected_day(model_day_index)
        self.__model.update_date_online_counts_data()

    @Slot(list, int)
    def update_days_in_gui(self, new_days_list: list[Day], new_selected_day_index):
        self.__gui.update_days_data(new_days_list)
        self.change_selected_day(new_selected_day_index)

    @Slot(object)
    def update_selected_day_in_gui(self, new_day: Day):
        self.__gui.update_selected_day(new_day)

    @Slot(object)
    def update_online_counts_graph(self, new_graph_data: OnlineCrountsGraphData):
        self.__gui.update_online_counts_graph(new_graph_data)

    # Run method for full front end
    def run(self):
        self.__gui.show()
        sys.exit(self.__qapp.exec())
