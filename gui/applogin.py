from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot

from views.ui_applogin import Ui_AppLogin

class AppLogin(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_AppLogin()
        self.__view.setupUi(self)

        self.__login = self.__view.login
        self.__loginButton = self.__view.loginButton
        self.__loginFailed = self.__view.loginFailed

        self.__twoFactorAuth = self.__view.twoFactorAuth
        self.__twoFactorAuthDefaultLabel = self.__view.authCodeLabel
        self.__twoFactorAuthEmailLabel = self.__view.emailCodeLabel
        self.__twoFactorAuthRecoveryLabel = self.__view.recoveryCodeLabel
        self.__twoFactorAuthDefaultVerifyButton = self.__view.authVerifyButton
        self.__twoFactorAuthEmailVerifyButton = self.__view.emailVerifyButton
        self.__twoFactorAuthRecoveryVerifyButton = self.__view.recoveryCodeVerifyButton
        self.__twoFactorAuthUseRecoveryCodeButton = self.__view.useRecoveryCodeButton
        self.__twoFactorAuthFailed = self.__view.twoFactorAuthFailed

        self.setup_connections()
        self.default_state()

    def setup_connections(self):
        
        # Placeholder until communication with backend is set up
        self.__loginButton.clicked.connect(self.two_factor_auth)

    # Sets the widget view to what it should look like when
    # launching the app for the first time
    def default_state(self):

        self.login_default_state()

        self.two_factor_auth_default_state()
        if not self.__twoFactorAuth.isHidden():
            self.__twoFactorAuth.hide()

    def login_default_state(self):
        if not self.__loginFailed.isHidden():
            self.__loginFailed.hide()

    # By default, all 2fa ui elements specific to a 2fa type will be hidden
    def two_factor_auth_default_state(self):
        if not self.__twoFactorAuthDefaultLabel.isHidden():
            self.__twoFactorAuthDefaultLabel.hide()

        if not self.__twoFactorAuthEmailLabel.isHidden():
            self.__twoFactorAuthEmailLabel.hide()

        if not self.__twoFactorAuthRecoveryLabel.isHidden():
            self.__twoFactorAuthRecoveryLabel.hide()

        if not self.__twoFactorAuthDefaultVerifyButton.isHidden():
            self.__twoFactorAuthDefaultVerifyButton.hide()

        if not self.__twoFactorAuthEmailVerifyButton.isHidden():
            self.__twoFactorAuthEmailVerifyButton.hide()

        if not self.__twoFactorAuthRecoveryVerifyButton.isHidden():
            self.__twoFactorAuthRecoveryVerifyButton.hide()
        
        if not self.__twoFactorAuthFailed.isHidden():
            self.__twoFactorAuthFailed.hide()

    # If auth credentials pass, and 2fa is required, switch login widget to show 2fa ui
    @Slot()
    def two_factor_auth(self):
        if not self.__login.isHidden():
            self.__login.hide()

        if self.__twoFactorAuth.isHidden():
            self.__twoFactorAuth.show()
            self.placeholder_set_2fa_type_ui()

    # placeholder method to show auth type ui, shows authenticator app auth type ui
    def placeholder_set_2fa_type_ui(self):
        self.two_factor_auth_default_state()

        if self.__twoFactorAuthDefaultLabel.isHidden():
            self.__twoFactorAuthDefaultLabel.show()

        if self.__twoFactorAuthDefaultVerifyButton.isHidden():
            self.__twoFactorAuthDefaultVerifyButton.show()