from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtCore import Slot
from PySide6.QtGui import QCloseEvent

from views.ui_quitdialog import Ui_QuitDialog

class QuitDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_QuitDialog()
        self.__view.setupUi(self)

        self.__yesButton = self.__view.quitCancelButtonBox.button(QDialogButtonBox.Yes)
        self.__noButton = self.__view.quitCancelButtonBox.button(QDialogButtonBox.No)

        self.setup_connections()

    def setup_connections(self):
        self.__yesButton.clicked.connect(self.confirm_quit)
        self.__noButton.clicked.connect(self.cancel_quit)

    @Slot()
    def confirm_quit(self):
        self.accept()

    @Slot()
    def cancel_quit(self):
        self.reject()