# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

from ui_app_main_widget import Ui_AppMainWidget
from ui_login_page_widget import Ui_LoginPage
from ui_two_factor_page_widget import Ui_TwoFactorAuthPage

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.appRootWidget = QStackedWidget(self.centralwidget)
        self.appRootWidget.setObjectName(u"appRootWidget")
        self.loginPageWidget = Ui_LoginPage()
        self.loginPageWidget.setObjectName(u"loginPageWidget")
        self.appRootWidget.addWidget(self.loginPageWidget)
        self.twoFactorAuthPageWidget = Ui_TwoFactorAuthPage()
        self.twoFactorAuthPageWidget.setObjectName(u"twoFactorAuthPageWidget")
        self.appRootWidget.addWidget(self.twoFactorAuthPageWidget)
        self.appMainWidget = Ui_AppMainWidget()
        self.appMainWidget.setObjectName(u"appMainWidget")
        self.appRootWidget.addWidget(self.appMainWidget)

        self.verticalLayout.addWidget(self.appRootWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.appRootWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VRChat Group Assistant", None))
    # retranslateUi

