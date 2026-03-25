from PySide6.QtWidgets import QWidget

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