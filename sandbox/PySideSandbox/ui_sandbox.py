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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.testComboBox = QComboBox(self.centralwidget)
        self.testComboBox.setObjectName(u"testComboBox")

        self.verticalLayout.addWidget(self.testComboBox)

        self.testButton = QPushButton(self.centralwidget)
        self.testButton.setObjectName(u"testButton")

        self.verticalLayout.addWidget(self.testButton)

        self.testLabel = QLabel(self.centralwidget)
        self.testLabel.setObjectName(u"testLabel")

        self.verticalLayout.addWidget(self.testLabel)

        self.testWidget = QWidget(self.centralwidget)
        self.testWidget.setObjectName(u"testWidget")
        self.verticalLayout_3 = QVBoxLayout(self.testWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphLabel = QLabel(self.testWidget)
        self.graphLabel.setObjectName(u"graphLabel")

        self.horizontalLayout.addWidget(self.graphLabel)

        self.graphButton = QPushButton(self.testWidget)
        self.graphButton.setObjectName(u"graphButton")

        self.horizontalLayout.addWidget(self.graphButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.testWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.testButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.testLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.graphLabel.setText(QCoreApplication.translate("MainWindow", u"Graph ", None))
        self.graphButton.setText(QCoreApplication.translate("MainWindow", u"ChangeGraph", None))
    # retranslateUi

