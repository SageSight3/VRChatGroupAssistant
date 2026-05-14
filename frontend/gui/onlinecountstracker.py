from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, QSignalBlocker, Qt

from gui.views.ui_onlinecountstracker import Ui_OnlineCountsTracker

from gui.onlinecountsgraph import OnlineCountsGraph

class OnlineCountsTracker(QWidget):

    from vrcga_signals import (
        selectedDayChanged, 
        showMemberCountsChanged, 
        showOnlinePercentsChanged
    )

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_OnlineCountsTracker()
        self.__view.setupUi(self)

        self.__dateSelectionBox = self.__view.dateSelectionBox
        self.__showPercentsCheckbox = self.__view.showPercentsCheckbox
        self.__showMemberCountsCheckbox = self.__view.showMemberCountsCheckbox
        self.__nextDateButton = self.__view.nextDateButton
        self.__prevDateButton = self.__view.prevDateButton

        # Add graph to view
        self.__graph = OnlineCountsGraph()
        self.__view.graphContainer.addWidget(self.__graph)

        self.setup_connections()

    def setup_connections(self):
        self.__dateSelectionBox.currentIndexChanged.connect(self.change_selected_date)
        self.__showMemberCountsCheckbox.checkStateChanged.connect(self.change_show_member_counts)
        self.__showPercentsCheckbox.checkStateChanged.connect(self.change_show_online_percents)
        self.__nextDateButton.clicked.connect(self.next_date)
        self.__prevDateButton.clicked.connect(self.prev_date)
    
    @Slot(int)
    def change_selected_date(self, _date_seletion_box_index):
        model_day_index = self.__dateSelectionBox.currentData()

        # If no item is selected or the selected item has no data, don't do anything
        if model_day_index == None:
            return
        
        self.selectedDayChanged.emit(model_day_index)

    @Slot()
    def next_date(self):
        # Since each arrow button wull be disabled, if at the beginning or end of the dates list, and pushing
        # the next date button would mean there's valid dates before the selected one again, make sure the prev
        # date button is reenabled
        self.__prevDateButton.setEnabled(True)

        # For the date buttons, don't forget that the dates list starts at the most recent date and goes backwards
        # So, the next button should go towards the beginning of the list
        new_selected_date_index = self.__dateSelectionBox.currentIndex() - 1
        if new_selected_date_index <= 0:
            self.__dateSelectionBox.setCurrentIndex(0)
            self.__nextDateButton.setEnabled(False)
        else:
            self.__dateSelectionBox.setCurrentIndex(new_selected_date_index)

    @Slot()
    def prev_date(self):
        # Since each arrow button wull be disabled, if at the beginning or end of the dates list, and pushing
        # the prev date button would mean there's valid dates after the selected one again, make sure the next
        # date button is reenabled
        self.__nextDateButton.setEnabled(True)

        # For the date buttons, don't forget that the dates list starts at the most recent date and goes backwards
        # So, the prev button should go towards the end of the list
        new_selected_date_index = self.__dateSelectionBox.currentIndex() + 1
        if new_selected_date_index >= self.__dateSelectionBox.count() - 1:
            self.__dateSelectionBox.setCurrentIndex(self.__dateSelectionBox.count() - 1)
            self.__prevDateButton.setEnabled(False)
        else:
            self.__dateSelectionBox.setCurrentIndex(new_selected_date_index)

    @Slot(object)
    def change_show_member_counts(self, check_state):
        self.showMemberCountsChanged.emit(check_state)

    @Slot(object)
    def change_show_online_percents(self, check_state):
        self.showOnlinePercentsChanged.emit(check_state)

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
        self.__graph.update_graph(new_graph_data, new_graph_data.show_online_percents, new_graph_data.show_member_counts)

    def set_show_member_counts(self, is_shown):
        if is_shown:
            self.__showMemberCountsCheckbox.setCheckState(Qt.Checked)
        else:
            self.__showMemberCountsCheckbox.setCheckState(Qt.Unchecked)

    def set_show_online_percents(self, is_shown):
        if is_shown:
            self.__showPercentsCheckbox.setCheckState(Qt.Checked)
        else:
            self.__showPercentsCheckbox.setCheckState(Qt.Unchecked)