import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Slot

from gui.mainwidget import MainWidget
from model.model import Model
from model.structs import Day

class Controller():

    # Initialize frontend app components
    def __init__(self, args):
        self.__qapp = QApplication(args)

        self.__gui = MainWidget()
        self.__model = Model()

        self.setup_connections()
        self.set_launch_state()
        
        # TEST
        for datapoint in self.__model.get_online_counts_data():
            print(f"online: {datapoint.online_count} total: {datapoint.total_count}, percent: {datapoint.online_percent}, timestamp: {datapoint.timestamp}")

    def setup_connections(self):

        # GUI Connections

        self.__gui.logout.connect(self.log_out)
        self.__gui.refreshAnalyticsData.connect(self.refresh_analytics_gui_data)
        
        # Model Connections
        self.__model.refreshedDaysList.connect(self.update_days_in_gui)

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

    @Slot(list)
    def update_days_in_gui(self, new_days_list: list[Day]):
        self.__gui.update_days_data(new_days_list)

    # Run method for full front end
    def run(self):
        self.__gui.show()
        sys.exit(self.__qapp.exec())

def main():
    app = Controller(sys.argv)

    sys.exit(app.run())

if __name__ == "__main__":
    main()