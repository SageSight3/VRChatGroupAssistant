from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot

from views.ui_mainwidget import Ui_MainWidget

'''
All code that's been written for GUI development and testing purposes
will be prefixed with the comment # VRCGA_TEST

This code is either meant to be compeletely temporary or still needs its real
functionality implemented

ex.

    # VRCGA_GUI_TEST
    from vrcga_signals import devSignal

'''

class MainWidget(QWidget):

    # FLCE signals
    from vrcga_signals import loginCreds, twoFACode

    # MI signals
    from vrcga_signals import (
        authCredsAccepted, 
        authCredsDenied,
        twoFACodeAccepted,
        twoFACodeDenied,
        requiresTOTP2fa,
        requiresEmailOTP2fa,
    )

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__appGui = Ui_MainWidget()
        self.__appGui.setupUi(self)

        self.__loginWidget = self.__appGui.login

        self.setup_connections()

    def setup_connections(self):
        self.__loginWidget.loginCreds.connect(self.submit_login_creds)
        self.__loginWidget.twoFACode.connect(self.submit_2fa_code)

        self.authCredsDenied.connect(self.__loginWidget.login_failed)
        self.requiresTOTP2fa.connect(self.__loginWidget.two_fa_auth_app_controls_ui)
        self.requiresEmailOTP2fa.connect(self.__loginWidget.two_fa_email_controls_ui)
        self.twoFACodeDenied.connect(self.__loginWidget.two_fa_failed)

    # Submit user entered login credentials
    # While the frontend's controller will likely be main.py, still receiving login credentials
    # from loginWidget here, so controller only needs to receive signals from MainWidget, and not its
    # subviews
    @Slot(str, str)
    def submit_login_creds(self, username, password):
        self.loginCreds.emit(username, password)

        # VRCGA_GUI_TEST
        # Temp for GUI development - Move to own method
        if username == "err":
            self.login_creds_denied()
            return

        # VRCGA_GUI_TEST
        # Temp for GUI development - Move to own method
        self.login_creds_accepted()
        
    @Slot()
    def login_creds_accepted(self):
        self.authCredsAccepted.emit()

        # VRCGA_GUI_TEST
        # Temp for GUI development - Move to own method
        self.requiresTOTP2fa.emit()

    @Slot()
    def login_creds_denied(self):
        self.authCredsDenied.emit()

    @Slot()
    def requires_2fa_auth_app(self):
        self.requiresTOTP2fa.emit()

    @Slot()
    def requires_2fa_email(self):
        self.requiresEmailOTP2fa.emit()

    @Slot(str)
    def submit_2fa_code(self, code):
        self.twoFACode.emit(code)

        # VRCGA_GUI_TEST
        # Temp for GUI development - Move to own method
        if code == "err":
            self.two_fa_code_denied()
            return

        # VRCGA_GUI_TEST
        # Temp for GUI development - Move to own method
        self.twoFACodeAccepted.emit()

    @Slot()
    def two_fa_code_accepted(self):
        self.twoFACodeAccepted.emit()

    @Slot()
    def two_fa_code_denied(self):
        self.twoFACodeDenied.emit()

        
