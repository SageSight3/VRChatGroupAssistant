from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal, Slot

from views.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):

    # Signal to be sent to app container to change it's page
    change_page = Signal(int)

    def __init__(self):
        super().__init__()

        self.__view = Ui_MainWindow()
        self.__view.setupUi(self)

        self.__app_container = self.__view.appContainer

        self.setup_connections()
        self.set_view_launch_state()
            
    def setup_connections(self):

        # for signals sent by MainWindow
        self.__view.prevButton.clicked.connect(self.on_prev_button_clicked)
        self.__view.nextButton.clicked.connect(self.on_next_button_clicked)
        self.change_page.connect(self.__app_container.on_change_page)

        # for signals received from other classes
        self.__app_container.toggle_secret.connect(self.toggle_secret_message)

    def set_view_launch_state(self):
        self.toggle_secret_message()

    @Slot()
    def toggle_secret_message(self):
        sender = self.sender()
        if sender == self.__app_container:
            print("app container")
            
        if self.__view.secretMessage.isHidden():
            self.__view.secretMessage.show()
        else:
            self.__view.secretMessage.hide()

    @Slot()
    def on_prev_button_clicked(self):
        new_current_page = self.__app_container.get_current_page() - 1
        self.change_page.emit(new_current_page)

    @Slot()
    def on_next_button_clicked(self):
        new_current_page = self.__app_container.get_current_page() + 1
        self.change_page.emit(new_current_page)