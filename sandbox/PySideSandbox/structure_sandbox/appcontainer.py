from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal

from views.ui_appcontainer import Ui_AppContainer

class AppContainer(QWidget):

    from appsignals import toggle_secret

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_AppContainer()
        self.__view.setupUi(self)

        self.__interactivePage = self.__view.interactivePage

        self.__current_page = self.__view.appContent.currentIndex()

        self.setup_connections()
        self.set_view_launch_state()
        
    def setup_connections(self):
        self.__interactivePage.toggle_secret.connect(self.on_toggle_secret)

    @Slot()
    def on_toggle_secret(self):
        sender = self.sender()
        if sender == self.__interactivePage:
            print("interactive page")
        self.toggle_secret.emit()
    
    def set_view_launch_state(self):
        self.change_page(0)

    # Prefixing the slot method's name with on_ will cause Qt to attempt to auto connect
    # the slot to a matching signal via the QMetaObject.connectSlotsByName() call in the widget's
    # UI file. To stop this, don't prefix the slot name with on_, or remove the @Slot decorator
    # from the method.
    # This can be disabled via passing the -a or --no-auto-connection option to uic
    # https://doc.qt.io/qt-6/uic.html
    @Slot(int)
    def on_change_page(self, val):
        self.change_page(val)

    def get_current_page(self):
        return self.__current_page

    def change_page(self, val):
        if val < self.__view.appContent.count() and val > -1:
            self.__view.appContent.setCurrentIndex(val)
            self.__current_page = self.__view.appContent.currentIndex()