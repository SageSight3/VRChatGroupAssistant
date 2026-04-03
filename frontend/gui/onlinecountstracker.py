from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, QSignalBlocker

from gui.views.ui_onlinecountstracker import Ui_OnlineCountsTracker

from gui.onlinecountsgraph import OnlineCountsGraph

class OnlineCountsTracker(QWidget):

    from vrcga_signals import selectedDayChanged

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

        self.setup_connections()

    def setup_connections(self):
        self.__dateSelectionBox.currentIndexChanged.connect(self.change_selected_date)
    
    @Slot(int)
    def change_selected_date(self, _date_seletion_box_index):
        model_day_index = self.__dateSelectionBox.currentData()

        # If no item is selected or the selected item has no data, don't do anything
        if model_day_index == None:
            return
        
        self.selectedDayChanged.emit(model_day_index)

    def refresh_dates_selection_box(self, new_days_list): 
        # Block signals to prevent selection box refresh from attempting to signal a selection change
        # when it's cleared for updating
        with QSignalBlocker(self.__dateSelectionBox):
            # Clear old dates list from selection box
            self.__dateSelectionBox.clear()

            for day in new_days_list:
                # First arg is date text, Second arg is index of that date in the model's days list
                self.__dateSelectionBox.addItem(day.date + " " + day.weekday, day.index)

    def update_selected_day(self, new_day):
        # Find the item with the correct model day index in the date selection box
        # and update selected date to that item
        selected_date_new_index = self.__dateSelectionBox.findData(new_day.index)

        # Since when the date selection box refreshed, items may have ended up in different
        # positions, prevent it from signaling that its selected item has changed again, for
        # the same item
        with QSignalBlocker(self.__dateSelectionBox):
            self.__dateSelectionBox.setCurrentIndex(selected_date_new_index)

    def update_graph(self, new_graph_data):
        self.__graph.update_graph(new_graph_data)