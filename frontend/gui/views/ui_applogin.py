# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'applogin.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_AppLogin(object):
    def setupUi(self, AppLogin):
        if not AppLogin.objectName():
            AppLogin.setObjectName(u"AppLogin")
        AppLogin.resize(914, 600)
        self.verticalLayout = QVBoxLayout(AppLogin)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.appTitle = QLabel(AppLogin)
        self.appTitle.setObjectName(u"appTitle")
        self.appTitle.setTextFormat(Qt.MarkdownText)
        self.appTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.appTitle)

        self.titleDivider = QFrame(AppLogin)
        self.titleDivider.setObjectName(u"titleDivider")
        self.titleDivider.setLineWidth(0)
        self.titleDivider.setMidLineWidth(5)
        self.titleDivider.setFrameShape(QFrame.Shape.HLine)
        self.titleDivider.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.titleDivider)

        self.loginContainer = QHBoxLayout()
        self.loginContainer.setObjectName(u"loginContainer")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.loginContainer.addItem(self.horizontalSpacer)

        self.login = QWidget(AppLogin)
        self.login.setObjectName(u"login")
        self.loginLayout = QVBoxLayout(self.login)
        self.loginLayout.setObjectName(u"loginLayout")
        self.loginTitleLabel = QLabel(self.login)
        self.loginTitleLabel.setObjectName(u"loginTitleLabel")
        self.loginTitleLabel.setTextFormat(Qt.MarkdownText)
        self.loginTitleLabel.setAlignment(Qt.AlignCenter)

        self.loginLayout.addWidget(self.loginTitleLabel)

        self.loginFailed = QWidget(self.login)
        self.loginFailed.setObjectName(u"loginFailed")
        self.loginFailedLayout = QHBoxLayout(self.loginFailed)
        self.loginFailedLayout.setObjectName(u"loginFailedLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.loginFailedLayout.addItem(self.horizontalSpacer_5)

        self.loginFailedIcon = QLabel(self.loginFailed)
        self.loginFailedIcon.setObjectName(u"loginFailedIcon")
        self.loginFailedIcon.setMinimumSize(QSize(32, 32))
        self.loginFailedIcon.setMaximumSize(QSize(32, 32))
        self.loginFailedIcon.setPixmap(QPixmap(u":/images/images/AuthErrorIconNoBG.png"))
        self.loginFailedIcon.setScaledContents(True)
        self.loginFailedIcon.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.loginFailedLayout.addWidget(self.loginFailedIcon)

        self.loginFailedText = QLabel(self.loginFailed)
        self.loginFailedText.setObjectName(u"loginFailedText")
        self.loginFailedText.setAlignment(Qt.AlignCenter)

        self.loginFailedLayout.addWidget(self.loginFailedText)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.loginFailedLayout.addItem(self.horizontalSpacer_6)


        self.loginLayout.addWidget(self.loginFailed)

        self.usernameInLayout = QHBoxLayout()
        self.usernameInLayout.setObjectName(u"usernameInLayout")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.usernameInLayout.addItem(self.horizontalSpacer_9)

        self.usernameIn = QLineEdit(self.login)
        self.usernameIn.setObjectName(u"usernameIn")
        self.usernameIn.setMinimumSize(QSize(200, 0))

        self.usernameInLayout.addWidget(self.usernameIn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.usernameInLayout.addItem(self.horizontalSpacer_10)


        self.loginLayout.addLayout(self.usernameInLayout)

        self.passwordInLayout = QHBoxLayout()
        self.passwordInLayout.setObjectName(u"passwordInLayout")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.passwordInLayout.addItem(self.horizontalSpacer_11)

        self.passwordIn = QLineEdit(self.login)
        self.passwordIn.setObjectName(u"passwordIn")
        self.passwordIn.setMinimumSize(QSize(200, 0))
        self.passwordIn.setEchoMode(QLineEdit.Password)

        self.passwordInLayout.addWidget(self.passwordIn)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.passwordInLayout.addItem(self.horizontalSpacer_12)


        self.loginLayout.addLayout(self.passwordInLayout)

        self.loginButton = QPushButton(self.login)
        self.loginButton.setObjectName(u"loginButton")

        self.loginLayout.addWidget(self.loginButton)


        self.loginContainer.addWidget(self.login)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.loginContainer.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.loginContainer)

        self.twoFactorAuthContainer = QHBoxLayout()
        self.twoFactorAuthContainer.setObjectName(u"twoFactorAuthContainer")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.twoFactorAuthContainer.addItem(self.horizontalSpacer_3)

        self.twoFactorAuth = QWidget(AppLogin)
        self.twoFactorAuth.setObjectName(u"twoFactorAuth")
        self.twoFactorAuthLayout = QVBoxLayout(self.twoFactorAuth)
        self.twoFactorAuthLayout.setSpacing(6)
        self.twoFactorAuthLayout.setObjectName(u"twoFactorAuthLayout")
        self.twoFactorAuthLayout.setContentsMargins(0, 0, 0, 0)
        self.twoFactorAuthTitleLabel = QLabel(self.twoFactorAuth)
        self.twoFactorAuthTitleLabel.setObjectName(u"twoFactorAuthTitleLabel")
        self.twoFactorAuthTitleLabel.setTextFormat(Qt.MarkdownText)
        self.twoFactorAuthTitleLabel.setAlignment(Qt.AlignCenter)

        self.twoFactorAuthLayout.addWidget(self.twoFactorAuthTitleLabel)

        self.emailCodeLabel = QLabel(self.twoFactorAuth)
        self.emailCodeLabel.setObjectName(u"emailCodeLabel")
        self.emailCodeLabel.setAlignment(Qt.AlignCenter)

        self.twoFactorAuthLayout.addWidget(self.emailCodeLabel)

        self.authCodeLabel = QLabel(self.twoFactorAuth)
        self.authCodeLabel.setObjectName(u"authCodeLabel")
        self.authCodeLabel.setAlignment(Qt.AlignCenter)

        self.twoFactorAuthLayout.addWidget(self.authCodeLabel)

        self.recoveryCodeLabel = QLabel(self.twoFactorAuth)
        self.recoveryCodeLabel.setObjectName(u"recoveryCodeLabel")
        self.recoveryCodeLabel.setAlignment(Qt.AlignCenter)

        self.twoFactorAuthLayout.addWidget(self.recoveryCodeLabel)

        self.twoFactorAuthFailed = QWidget(self.twoFactorAuth)
        self.twoFactorAuthFailed.setObjectName(u"twoFactorAuthFailed")
        self.twoFactorAuthFailedLayout = QHBoxLayout(self.twoFactorAuthFailed)
        self.twoFactorAuthFailedLayout.setObjectName(u"twoFactorAuthFailedLayout")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.twoFactorAuthFailedLayout.addItem(self.horizontalSpacer_7)

        self.twoFactorAuthFailedIcon = QLabel(self.twoFactorAuthFailed)
        self.twoFactorAuthFailedIcon.setObjectName(u"twoFactorAuthFailedIcon")
        self.twoFactorAuthFailedIcon.setMinimumSize(QSize(32, 32))
        self.twoFactorAuthFailedIcon.setMaximumSize(QSize(32, 32))
        self.twoFactorAuthFailedIcon.setPixmap(QPixmap(u":/images/images/AuthErrorIconNoBG.png"))
        self.twoFactorAuthFailedIcon.setScaledContents(True)
        self.twoFactorAuthFailedIcon.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.twoFactorAuthFailedLayout.addWidget(self.twoFactorAuthFailedIcon)

        self.twoFactorAuthFailedText = QLabel(self.twoFactorAuthFailed)
        self.twoFactorAuthFailedText.setObjectName(u"twoFactorAuthFailedText")
        self.twoFactorAuthFailedText.setAlignment(Qt.AlignCenter)

        self.twoFactorAuthFailedLayout.addWidget(self.twoFactorAuthFailedText)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.twoFactorAuthFailedLayout.addItem(self.horizontalSpacer_8)


        self.twoFactorAuthLayout.addWidget(self.twoFactorAuthFailed)

        self.twoFactorAuthInLayout = QHBoxLayout()
        self.twoFactorAuthInLayout.setObjectName(u"twoFactorAuthInLayout")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.twoFactorAuthInLayout.addItem(self.horizontalSpacer_13)

        self.twoFactorAuthIn = QLineEdit(self.twoFactorAuth)
        self.twoFactorAuthIn.setObjectName(u"twoFactorAuthIn")
        self.twoFactorAuthIn.setMinimumSize(QSize(200, 0))

        self.twoFactorAuthInLayout.addWidget(self.twoFactorAuthIn)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.twoFactorAuthInLayout.addItem(self.horizontalSpacer_14)


        self.twoFactorAuthLayout.addLayout(self.twoFactorAuthInLayout)

        self.twoFactorAuthButtonsLayout = QHBoxLayout()
        self.twoFactorAuthButtonsLayout.setObjectName(u"twoFactorAuthButtonsLayout")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.twoFactorAuthButtonsLayout.addItem(self.horizontalSpacer_15)

        self.useRecoveryCodeButton = QPushButton(self.twoFactorAuth)
        self.useRecoveryCodeButton.setObjectName(u"useRecoveryCodeButton")

        self.twoFactorAuthButtonsLayout.addWidget(self.useRecoveryCodeButton)

        self.useAuthCodeButton = QPushButton(self.twoFactorAuth)
        self.useAuthCodeButton.setObjectName(u"useAuthCodeButton")

        self.twoFactorAuthButtonsLayout.addWidget(self.useAuthCodeButton)

        self.useEmailCodeButton = QPushButton(self.twoFactorAuth)
        self.useEmailCodeButton.setObjectName(u"useEmailCodeButton")

        self.twoFactorAuthButtonsLayout.addWidget(self.useEmailCodeButton)

        self.emailVerifyButton = QPushButton(self.twoFactorAuth)
        self.emailVerifyButton.setObjectName(u"emailVerifyButton")
        self.emailVerifyButton.setEnabled(True)

        self.twoFactorAuthButtonsLayout.addWidget(self.emailVerifyButton)

        self.authVerifyButton = QPushButton(self.twoFactorAuth)
        self.authVerifyButton.setObjectName(u"authVerifyButton")

        self.twoFactorAuthButtonsLayout.addWidget(self.authVerifyButton)

        self.recoveryCodeVerifyButton = QPushButton(self.twoFactorAuth)
        self.recoveryCodeVerifyButton.setObjectName(u"recoveryCodeVerifyButton")

        self.twoFactorAuthButtonsLayout.addWidget(self.recoveryCodeVerifyButton)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.twoFactorAuthButtonsLayout.addItem(self.horizontalSpacer_16)


        self.twoFactorAuthLayout.addLayout(self.twoFactorAuthButtonsLayout)

        self.logoutButtonWidget = QWidget(self.twoFactorAuth)
        self.logoutButtonWidget.setObjectName(u"logoutButtonWidget")
        self.logoutButtonLayout = QHBoxLayout(self.logoutButtonWidget)
        self.logoutButtonLayout.setObjectName(u"logoutButtonLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.logoutButtonLayout.addLayout(self.horizontalLayout_2)

        self.logoutButton = QPushButton(self.logoutButtonWidget)
        self.logoutButton.setObjectName(u"logoutButton")

        self.logoutButtonLayout.addWidget(self.logoutButton)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.logoutButtonLayout.addLayout(self.horizontalLayout_3)


        self.twoFactorAuthLayout.addWidget(self.logoutButtonWidget)


        self.twoFactorAuthContainer.addWidget(self.twoFactorAuth)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.twoFactorAuthContainer.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.twoFactorAuthContainer)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(AppLogin)
    # setupUi

    def retranslateUi(self, AppLogin):
        AppLogin.setWindowTitle(QCoreApplication.translate("AppLogin", u"Form", None))
        self.appTitle.setText(QCoreApplication.translate("AppLogin", u"# VRChat Group Assistant", None))
        self.loginTitleLabel.setText(QCoreApplication.translate("AppLogin", u"## Login", None))
        self.loginFailedIcon.setText("")
        self.loginFailedText.setText(QCoreApplication.translate("AppLogin", u"Login failed.", None))
        self.usernameIn.setPlaceholderText(QCoreApplication.translate("AppLogin", u"Username/Email", None))
        self.passwordIn.setPlaceholderText(QCoreApplication.translate("AppLogin", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("AppLogin", u"Login", None))
        self.twoFactorAuthTitleLabel.setText(QCoreApplication.translate("AppLogin", u"## Two Factor Authentication", None))
        self.emailCodeLabel.setText(QCoreApplication.translate("AppLogin", u"Enter the verification code sent to your email.", None))
        self.authCodeLabel.setText(QCoreApplication.translate("AppLogin", u"Enter verification code from your authenticator app.", None))
        self.recoveryCodeLabel.setText(QCoreApplication.translate("AppLogin", u"Enter one of your saved and unused one-time recovery codes.", None))
        self.twoFactorAuthFailedIcon.setText("")
        self.twoFactorAuthFailedText.setText(QCoreApplication.translate("AppLogin", u"Two Factor Authentication Failed", None))
        self.twoFactorAuthIn.setPlaceholderText(QCoreApplication.translate("AppLogin", u"Verification Code", None))
        self.useRecoveryCodeButton.setText(QCoreApplication.translate("AppLogin", u"Use One-Time Recovery Code Instead", None))
        self.useAuthCodeButton.setText(QCoreApplication.translate("AppLogin", u"Use Authenticator App Instead", None))
        self.useEmailCodeButton.setText(QCoreApplication.translate("AppLogin", u"Use Email Code Instead", None))
        self.emailVerifyButton.setText(QCoreApplication.translate("AppLogin", u"Verify", None))
        self.authVerifyButton.setText(QCoreApplication.translate("AppLogin", u"Verify", None))
        self.recoveryCodeVerifyButton.setText(QCoreApplication.translate("AppLogin", u"Verify One-Time Recovery Code", None))
        self.logoutButton.setText(QCoreApplication.translate("AppLogin", u"Log out", None))
    # retranslateUi

