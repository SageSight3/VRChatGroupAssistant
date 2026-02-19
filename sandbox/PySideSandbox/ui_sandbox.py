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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from custom_widgets import SearchableComboBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.testComboBox = SearchableComboBox(self.centralwidget)
        self.testComboBox.setObjectName(u"testComboBox")
        self.testComboBox.setEditable(True)

        self.verticalLayout.addWidget(self.testComboBox)

        self.graphButton = QPushButton(self.centralwidget)
        self.graphButton.setObjectName(u"graphButton")

        self.verticalLayout.addWidget(self.graphButton)

        self.testLabel = QLabel(self.centralwidget)
        self.testLabel.setObjectName(u"testLabel")

        self.verticalLayout.addWidget(self.testLabel)

        self.testWidget = QWidget(self.centralwidget)
        self.testWidget.setObjectName(u"testWidget")
        self.testWidgetMainLayout = QVBoxLayout(self.testWidget)
        self.testWidgetMainLayout.setObjectName(u"testWidgetMainLayout")
        self.testWidgetDashboardLayout = QHBoxLayout()
        self.testWidgetDashboardLayout.setObjectName(u"testWidgetDashboardLayout")
        self.graphLabel = QLabel(self.testWidget)
        self.graphLabel.setObjectName(u"graphLabel")

        self.testWidgetDashboardLayout.addWidget(self.graphLabel)

        self.newValsButton = QPushButton(self.testWidget)
        self.newValsButton.setObjectName(u"newValsButton")

        self.testWidgetDashboardLayout.addWidget(self.newValsButton)


        self.testWidgetMainLayout.addLayout(self.testWidgetDashboardLayout)


        self.verticalLayout.addWidget(self.testWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.graphButton.setText(QCoreApplication.translate("MainWindow", u"Graph Selected Option", None))
        self.testLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.graphLabel.setText(QCoreApplication.translate("MainWindow", u"Graph ", None))
        self.newValsButton.setText(QCoreApplication.translate("MainWindow", u"Generate New Options", None))
    # retranslateUi

