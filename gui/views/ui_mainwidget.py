# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

from applogin import AppLogin

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(800, 600)
        self.verticalLayout = QVBoxLayout(MainWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.appPages = QStackedWidget(MainWidget)
        self.appPages.setObjectName(u"appPages")
        self.login = AppLogin()
        self.login.setObjectName(u"login")
        self.appPages.addWidget(self.login)
        self.appMain = QWidget()
        self.appMain.setObjectName(u"appMain")
        self.appPages.addWidget(self.appMain)

        self.verticalLayout.addWidget(self.appPages)


        self.retranslateUi(MainWidget)

        self.appPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"VRChat Group Assistant", None))
    # retranslateUi

