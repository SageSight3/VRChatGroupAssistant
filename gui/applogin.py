from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, QTimer

from views.ui_applogin import Ui_AppLogin

class AppLogin(QWidget):

    # FLCE signals
    from vrcga_signals import loginCreds, twoFACode

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_AppLogin()
        self.__view.setupUi(self)

        # easier access to widget elements
        self.__login = self.__view.login
        self.__loginButton = self.__view.loginButton
        self.__loginFailed = self.__view.loginFailed
        self.__usernameIn = self.__view.usernameIn
        self.__passwordIn = self.__view.passwordIn

        self.__twoFATitleLabel = self.__view.twoFactorAuthTitleLabel
        self.__twoFA = self.__view.twoFactorAuth
        self.__twoFAAuthAppLabel = self.__view.authCodeLabel
        self.__twoFAEmailLabel = self.__view.emailCodeLabel
        self.__twoFARecoveryLabel = self.__view.recoveryCodeLabel
        self.__twoFAAuthAppVerifyButton = self.__view.authVerifyButton
        self.__twoFAEmailVerifyButton = self.__view.emailVerifyButton
        self.__twoFARecoveryVerifyButton = self.__view.recoveryCodeVerifyButton
        self.__twoFAUseRecoveryCodeButton = self.__view.useRecoveryCodeButton
        self.__twoFAUseAuthCodeButton = self.__view.useAuthCodeButton
        self.__twoFAUseEmailCodeButton = self.__view.useEmailCodeButton
        self.__twoFAFailed = self.__view.twoFactorAuthFailed
        self.__twoFACodeIn = self.__view.twoFactorAuthIn

        # This will hold onto the button in twoFactorAuth to switch back
        # to the ui for the original auth type twoFactorAuth was set to
        # if the user switches to using a recovery code
        self.__twoFAUseOriginalTypeButton = None

        self.__logoutButton = self.__view.logoutButton

        self.setup_connections()
        self.default_state()

    def setup_connections(self):
        self.__loginButton.clicked.connect(self.submit_login_creds)

        self.__twoFAUseRecoveryCodeButton.clicked.connect(self.two_fa_recovery_code_controls_ui)
        self.__twoFAUseAuthCodeButton.clicked.connect(self.two_fa_auth_app_controls_ui)
        self.__twoFAUseEmailCodeButton.clicked.connect(self.two_fa_email_controls_ui)

        self.__twoFAAuthAppVerifyButton.clicked.connect(self.submit_2fa_code)
        self.__twoFAEmailVerifyButton.clicked.connect(self.submit_2fa_code)
        self.__twoFARecoveryVerifyButton.clicked.connect(self.submit_2fa_code)

        self.__logoutButton.clicked.connect(self.logout)

    # Sets the widget view to what it should look like when
    # launching the app for the first time
    def default_state(self):
        self.login_default_state()
        self.two_fa_default_state()

        self.hide_ui_element(self.__twoFA)

        # ensuring login widget is shown, in case user returns to login screen
        self.show_ui_element(self.__login)

    def login_default_state(self):
        # Make sure user input fields are clear
        self.clear_login_input_fields()

        self.hide_ui_element(self.__loginFailed)

    def clear_login_input_fields(self):
        self.__usernameIn.clear()
        self.__passwordIn.clear()

    # By default, all 2fa ui elements specific to a 2fa type will be hidden
    def two_fa_default_state(self):
        # Make sure code input field is clear
        self.__twoFACodeIn.clear()

        # twoFATitleLabel's text format is set to markdown
        self.__twoFATitleLabel.setText("## Two Factor Authentication")

       # self.__twoFAUseOriginalTypeButton = None

        self.hide_ui_element(self.__twoFAAuthAppLabel)
        self.hide_ui_element(self.__twoFAEmailLabel)
        self.hide_ui_element(self.__twoFARecoveryLabel)
        self.hide_ui_element(self.__twoFAAuthAppVerifyButton)
        self.hide_ui_element(self.__twoFAEmailVerifyButton)
        self.hide_ui_element(self.__twoFARecoveryVerifyButton)
        self.hide_ui_element(self.__twoFAUseRecoveryCodeButton)
        self.hide_ui_element(self.__twoFAUseAuthCodeButton)
        self.hide_ui_element(self.__twoFAUseEmailCodeButton)
        self.hide_ui_element(self.__twoFAFailed)

    # Submit user entered login credentials
    @Slot()
    def submit_login_creds(self):
        username = self.__usernameIn.text()
        password = self.__passwordIn.text()
        self.loginCreds.emit(username, password)

    @Slot()
    def login_failed(self):
        self.clear_login_input_fields()
        
        # have the error widget blink, so that if the user enters the wrong info more than once
        # the ui better indicates that the error was related to their most recent attrept
        self.hide_ui_element(self.__loginFailed)

        # QTimer.singleShot()'s second param can't be class instance method
        # See https://doc.qt.io/qt-6/qtimer.html#singleShot for info
        def show_login_failed():
            self.show_ui_element(self.__loginFailed)
        blink_duration = 75 # delay is in ms
        QTimer.singleShot(blink_duration, show_login_failed)

    @Slot()
    def two_fa_auth_app_controls_ui(self):
        self.prepare_2fa_ui("Authenticator App")

        self.__twoFAUseOriginalTypeButton = self.__twoFAUseAuthCodeButton

        self.show_ui_element(self.__twoFAAuthAppLabel)
        self.show_ui_element(self.__twoFAAuthAppVerifyButton)
        self.show_ui_element(self.__twoFAUseRecoveryCodeButton)

    @Slot()
    def two_fa_email_controls_ui(self):
        self.prepare_2fa_ui("Email")

        self.__twoFAUseOriginalTypeButton = self.__twoFAUseEmailCodeButton

        self.show_ui_element(self.__twoFAEmailLabel)
        self.show_ui_element(self.__twoFAEmailVerifyButton)
        self.show_ui_element(self.__twoFAUseRecoveryCodeButton)

    @Slot()
    def two_fa_recovery_code_controls_ui(self):
        self.prepare_2fa_ui("Recovery Code")

        self.show_ui_element(self.__twoFARecoveryLabel)
        self.show_ui_element(self.__twoFARecoveryVerifyButton)

        # switch auth type button will change to switch back to the original auth type
        # the two factor auth widget was set to
        self.show_ui_element(self.__twoFAUseOriginalTypeButton)

    # resets 2fa ui and sets the title to the right 2fa auth type
    def prepare_2fa_ui(self, title: str):
        # reset 2fa ui to default state to ensure ui behaves as intended
        # before switching to ui for auth type
        self.two_fa_default_state()

        self.hide_ui_element(self.__login)

        self.__twoFATitleLabel.setText(f"{self.__twoFATitleLabel.text()} - {title}")

        self.show_ui_element(self.__twoFA)

    @Slot()
    def logout(self):
        # clear the original auth type button, since the user is logging out
        self.__twoFAUseOriginalTypeButton = None

        # reset login screen to default state
        self.default_state()

    @Slot()
    def submit_2fa_code(self):
        code = self.__twoFACodeIn.text()
        self.twoFACode.emit(code)

    @Slot()
    def two_fa_failed(self):
        self.__twoFACodeIn.clear()

        # have the error widget blink, so that if the user enters the wrong info more than once
        # the ui better indicates that the error was related to their most recent attrept
        self.hide_ui_element(self.__twoFAFailed)

        # QTimer.singleShot()'s second param can't be class instance method
        # See https://doc.qt.io/qt-6/qtimer.html#singleShot for info
        def show_2fa_failed():
            self.show_ui_element(self.__twoFAFailed)
        blink_duration = 75 # delay is in ms
        QTimer.singleShot(blink_duration, show_2fa_failed)

    def hide_ui_element(self, uiElement):
        if not uiElement.isHidden():
            uiElement.hide()

    def show_ui_element(self, uiElement):
        if uiElement.isHidden():
            uiElement.show()