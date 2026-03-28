from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot

from gui.views.ui_onlinecountstracker import Ui_OnlineCountsTracker

from gui.onlinecountsgraph import OnlineCountsGraph

class OnlineCountsTracker(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_OnlineCountsTracker()
        self.__view.setupUi(self)

        self.__dateSelectionBox = self.__view.dateSelectionBox
        self.__graphPercentsCheckbox = self.__view.graphPercentsCheckbox
        self.__nextDateButton = self.__view.nextDateButton
        self.__prevDateButton = self.__view.prevDateButton

        # Add graph to view
        self.__graph = OnlineCountsGraph()
        self.__view.graphContainer.addWidget(self.__graph)

    def refresh_dates_selection_box(self, new_days_list): 
        # Save data of current date selection
        selected_date = self.__dateSelectionBox.currentData()

        # Clear old dates list from selection box 
        self.__dateSelectionBox.clear()

        for day in new_days_list:
            # First arg is text, Second arg is data, assiging to both means
            # date formatting/label in selection box can be changed without
            # changing its data
            self.__dateSelectionBox.addItem(day.date, day.date)

        # Set dates selection box selected item to the selected date it was before refreshing
        selected_date_new_index = self.__dateSelectionBox.findData(selected_date)
        
        # If selected date data isn't in new dates list, set date selection box selected item to
        # the most recent date
        if selected_date_new_index == -1:
            selected_date_new_index = 0

        self.__dateSelectionBox.setCurrentIndex(selected_date_new_index)

    def refresh_graph(self, new_graph_data):
        pass