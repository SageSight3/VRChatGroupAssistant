# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_ui_testxNPYKU.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDial, QLabel,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_WidgetUITest(QWidget): # swapped inheritance from object to QWidget manually

    # __init__() added manually
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, WidgetUITest):
        if not WidgetUITest.objectName():
            WidgetUITest.setObjectName(u"WidgetUITest")
        WidgetUITest.resize(780, 631)
        self.label = QLabel(WidgetUITest)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 60, 49, 16))
        self.textBrowser = QTextBrowser(WidgetUITest)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(320, 40, 256, 192))
        self.calendarWidget = QCalendarWidget(WidgetUITest)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(80, 330, 256, 190))
        self.dial = QDial(WidgetUITest)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(550, 370, 50, 64))
        self.pushButton = QPushButton(WidgetUITest)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 220, 75, 24))

        self.retranslateUi(WidgetUITest)

        QMetaObject.connectSlotsByName(WidgetUITest)
    # setupUi

    def retranslateUi(self, WidgetUITest):
        WidgetUITest.setWindowTitle(QCoreApplication.translate("WidgetUITest", u"Form", None))
        self.label.setText(QCoreApplication.translate("WidgetUITest", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("WidgetUITest", u"PushButton", None))
    # retranslateUi

