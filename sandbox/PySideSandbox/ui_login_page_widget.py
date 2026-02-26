# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_page_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import resources_rc

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(800, 600)
        self.gridLayout = QGridLayout(LoginPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.loginFailedWidget = QWidget(LoginPage)
        self.loginFailedWidget.setObjectName(u"loginFailedWidget")
        self.horizontalLayout = QHBoxLayout(self.loginFailedWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.errorImage = QLabel(self.loginFailedWidget)
        self.errorImage.setObjectName(u"errorImage")
        self.errorImage.setPixmap(QPixmap(u":/images/images/vrc_login_failed.png"))

        self.horizontalLayout.addWidget(self.errorImage)

        self.loginFailedDesc = QLabel(self.loginFailedWidget)
        self.loginFailedDesc.setObjectName(u"loginFailedDesc")

        self.horizontalLayout.addWidget(self.loginFailedDesc)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout.addWidget(self.loginFailedWidget, 1, 1, 1, 1)

        self.usernameIn = QLineEdit(LoginPage)
        self.usernameIn.setObjectName(u"usernameIn")

        self.gridLayout.addWidget(self.usernameIn, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.passwordIn = QLineEdit(LoginPage)
        self.passwordIn.setObjectName(u"passwordIn")

        self.gridLayout.addWidget(self.passwordIn, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.loginButton = QPushButton(LoginPage)
        self.loginButton.setObjectName(u"loginButton")

        self.gridLayout.addWidget(self.loginButton, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 1, 1, 1)


        self.retranslateUi(LoginPage)

        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setWindowTitle(QCoreApplication.translate("LoginPage", u"Login", None))
        self.errorImage.setText("")
        self.loginFailedDesc.setText(QCoreApplication.translate("LoginPage", u"Invalid Username/Email or Password", None))
        self.usernameIn.setPlaceholderText(QCoreApplication.translate("LoginPage", u"Username/Email", None))
        self.passwordIn.setPlaceholderText(QCoreApplication.translate("LoginPage", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("LoginPage", u"Login", None))
    # retranslateUi

