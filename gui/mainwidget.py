from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot
from PySide6.QtGui import QCloseEvent

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
    from vrcga_signals import loginCreds, twoFACode, logout

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

        # the stacked widget holding onto the login and main app views
        self.__appOuterWidgets = self.__appGui.appPages

        self.__loginWidget = self.__appGui.login
        self.__mainAppWidget = self.__appGui.appMain

        self.setup_connections()
        self.set_launch_state()

    # Set app and app subviews to their launch states
    def set_launch_state(self):
        self.__appOuterWidgets.setCurrentWidget(self.__loginWidget)
        self.__loginWidget.set_launch_state()
        self.__mainAppWidget.set_launch_state()

    def setup_connections(self):

        '''
        Login Widget Connections

        '''
        # FLCE connections
        self.__loginWidget.loginCreds.connect(self.submit_login_creds)
        self.__loginWidget.twoFACode.connect(self.submit_2fa_code)
        self.__loginWidget.logout.connect(self.log_out)
        
        self.logout.connect(self.__loginWidget.log_out)

        # MI connections
        self.authCredsDenied.connect(self.__loginWidget.login_failed)
        self.requiresTOTP2fa.connect(self.__loginWidget.two_fa_auth_app_controls_ui)
        self.requiresEmailOTP2fa.connect(self.__loginWidget.two_fa_email_controls_ui)
        self.twoFACodeDenied.connect(self.__loginWidget.two_fa_failed)

        '''
        Main App Widget Connections

        '''
        self.twoFACodeAccepted.connect(self.show_main_app)
        self.__mainAppWidget.logout.connect(self.log_out)



    '''
    Login Related Methods

    '''


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

    @Slot()
    def log_out(self):
        # emit logout signal, so other modules can do what they need to do
        # when the user logs out
        self.logout.emit()
        
        # return to app launch state
        self.set_launch_state()

    '''
    App Main Related Methods

    '''



    @Slot()
    def show_main_app(self):
        self.__appOuterWidgets.setCurrentWidget(self.__mainAppWidget)



    '''
    App Quit 

    '''

    @Slot()
    def app_quit_dialog(self):
        # VRCGA_GUI_TEST
        # Activates app close event
        self.close()

    # Override normal close event
    def closeEvent(self, event: QCloseEvent):
        # Accept close event and allow mainwidget to close
        event.accept()