from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot

from views.ui_interactivepage import Ui_InteractivePage

class InteractivePage(QWidget):

    from appsignals import toggle_secret

    def __init__(self, parent=None):
        super().__init__(parent)

        self.view = Ui_InteractivePage()
        self.view.setupUi(self)

        self.setup_connections()

    def setup_connections(self):
        self.view.toggleSecretButton.clicked.connect(self.on_toggle_secret_button_clicked)

    @Slot()
    def on_toggle_secret_button_clicked(self):
        self.toggle_secret.emit()

    