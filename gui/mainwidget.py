from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal

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
    from vrcga_signals import loginCredentials, twoFactorAuthCode

    # MI signals
    from vrcga_signals import (
        authCredentialsAccepted, 
        authCredentialsDenied,
        twoFactorAuthCodeAccepted,
        twoFactorAuthCodeDenied
    )

    # VRCGA_GUI_TEST
    from vrcga_signals import devSignal

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__appGui = Ui_MainWidget()
        self.__appGui.setupUi(self)

        self.__loginWidget = self.__appGui.login

        self.setup_connections()

    def setup_connections(self):
        self.__loginWidget.loginCredentials.connect(self.submit_login_credentials)

        # VRCGA_GUI_TEST
        # temp implementation for GUI testing and development
        self.authCredentialsAccepted.connect(self.__loginWidget.two_factor_auth)

    # Placeholder explanation
    # While the frontend's controller will likely be main.py, still receiving login credentials
    # from loginWidget here, so controller only needs to receive signals from MainWidget, and not its
    # subviews
    @Slot(str, str)
    def submit_login_credentials(self, username, password):
        self.loginCredentials.emit(username, password)
        
        # VRCGA_GUI_TEST
        # Temp for GUI development - Move to own method
        self.authCredentialsAccepted.emit()

    @Slot(str)
    def submit_2fa_code(self, code):
        self.twoFactorAuthCode.emit(code)

        # VRCGA_GUI_TEST
        # Temp for GUI development - Move to own method
        self.twoFactorAuthCodeAccepted.emit()




        
