# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stacked_widget_testjZjNQf.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QTextEdit, QToolBox,
    QToolButton, QVBoxLayout, QWidget)

from ui_widget_ui_test import Ui_WidgetUITest

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.textEdit = QTextEdit(self.page)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(90, 250, 104, 71))
        self.toolButton = QToolButton(self.page)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(230, 150, 21, 22))
        self.buttonBox = QDialogButtonBox(self.page)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(360, 280, 156, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.stackedWidget.addWidget(self.page)
        self.page_5 = Ui_WidgetUITest()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.toolBox = QToolBox(self.page_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(220, 350, 69, 129))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 98, 28))
        self.toolBox.addItem(self.page_3, u"Page 1")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 98, 28))
        self.toolBox.addItem(self.page_4, u"Page 2")
        self.pushButton = QPushButton(self.page_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 130, 75, 24))
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 220, 49, 16))
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

