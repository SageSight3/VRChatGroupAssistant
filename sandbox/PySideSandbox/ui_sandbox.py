# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sandbox.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.testComboBox = QComboBox(self.centralwidget)
        self.testComboBox.setObjectName(u"testComboBox")
        self.testComboBox.setGeometry(QRect(50, 70, 361, 21))
        self.testButton = QPushButton(self.centralwidget)
        self.testButton.setObjectName(u"testButton")
        self.testButton.setGeometry(QRect(50, 180, 551, 24))
        self.testLabel = QLabel(self.centralwidget)
        self.testLabel.setObjectName(u"testLabel")
        self.testLabel.setGeometry(QRect(160, 270, 541, 51))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.testButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.testLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

