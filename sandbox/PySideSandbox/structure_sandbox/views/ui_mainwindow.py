# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowEzIXka.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

from appcontainer import AppContainer
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget {\n"
"	background-image: url(:/images/images/MainWindowBGLowOpacity.png);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dashboard = QHBoxLayout()
        self.dashboard.setObjectName(u"dashboard")
        self.changePageLabel = QLabel(self.centralwidget)
        self.changePageLabel.setObjectName(u"changePageLabel")

        self.dashboard.addWidget(self.changePageLabel)

        self.arrowButton = QToolButton(self.centralwidget)
        self.arrowButton.setObjectName(u"arrowButton")
        self.arrowButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/images/images/ArrowButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.arrowButton.setIcon(icon)
        self.arrowButton.setArrowType(Qt.NoArrow)

        self.dashboard.addWidget(self.arrowButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dashboard.addItem(self.horizontalSpacer)

        self.secretMessage = QLabel(self.centralwidget)
        self.secretMessage.setObjectName(u"secretMessage")

        self.dashboard.addWidget(self.secretMessage)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dashboard.addItem(self.horizontalSpacer_2)

        self.prevButton = QPushButton(self.centralwidget)
        self.prevButton.setObjectName(u"prevButton")

        self.dashboard.addWidget(self.prevButton)

        self.nextButton = QPushButton(self.centralwidget)
        self.nextButton.setObjectName(u"nextButton")

        self.dashboard.addWidget(self.nextButton)


        self.verticalLayout.addLayout(self.dashboard)

        self.appContainer = AppContainer(self.centralwidget)
        self.appContainer.setObjectName(u"appContainer")

        self.verticalLayout.addWidget(self.appContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.changePageLabel.setText(QCoreApplication.translate("MainWindow", u"Change Page", None))
        self.arrowButton.setText("")
        self.secretMessage.setText(QCoreApplication.translate("MainWindow", u"Secret Message", None))
        self.prevButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi

