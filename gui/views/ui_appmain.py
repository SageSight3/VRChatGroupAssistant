# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appmain.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_AppMain(object):
    def setupUi(self, AppMain):
        if not AppMain.objectName():
            AppMain.setObjectName(u"AppMain")
        AppMain.resize(800, 600)
        self.verticalLayout = QVBoxLayout(AppMain)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.navContentSplitter = QSplitter(AppMain)
        self.navContentSplitter.setObjectName(u"navContentSplitter")
        self.navContentSplitter.setStyleSheet(u"QSplitter::handle {\n"
"    background-color: #000000; \n"
"}")
        self.navContentSplitter.setOrientation(Qt.Horizontal)
        self.navContentSplitter.setHandleWidth(2)
        self.navContentSplitter.setChildrenCollapsible(False)
        self.nav = QWidget(self.navContentSplitter)
        self.nav.setObjectName(u"nav")
        self.nav.setMinimumSize(QSize(140, 0))
        self.nav.setMaximumSize(QSize(200, 16777215))
        self.navLayout = QVBoxLayout(self.nav)
        self.navLayout.setSpacing(2)
        self.navLayout.setObjectName(u"navLayout")
        self.navLayout.setContentsMargins(2, 4, 2, 0)
        self.aboutButton = QPushButton(self.nav)
        self.appPageNavButtons = QButtonGroup(AppMain)
        self.appPageNavButtons.setObjectName(u"appPageNavButtons")
        self.appPageNavButtons.addButton(self.aboutButton)
        self.aboutButton.setObjectName(u"aboutButton")
        self.aboutButton.setCheckable(True)

        self.navLayout.addWidget(self.aboutButton)

        self.analyticsButton = QPushButton(self.nav)
        self.appPageNavButtons.addButton(self.analyticsButton)
        self.analyticsButton.setObjectName(u"analyticsButton")
        self.analyticsButton.setCheckable(True)

        self.navLayout.addWidget(self.analyticsButton)

        self.analyticsSubPanel = QWidget(self.nav)
        self.analyticsSubPanel.setObjectName(u"analyticsSubPanel")
        self.analyticsSubPanelLayout = QHBoxLayout(self.analyticsSubPanel)
        self.analyticsSubPanelLayout.setObjectName(u"analyticsSubPanelLayout")
        self.analyticsSubPanelLayout.setContentsMargins(9, 0, 9, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.analyticsSubPanelLayout.addItem(self.horizontalSpacer)

        self.analyticsSubPanelItemsLayout = QVBoxLayout()
        self.analyticsSubPanelItemsLayout.setSpacing(2)
        self.analyticsSubPanelItemsLayout.setObjectName(u"analyticsSubPanelItemsLayout")
        self.autologgerStatus = QLabel(self.analyticsSubPanel)
        self.autologgerStatus.setObjectName(u"autologgerStatus")
        self.autologgerStatus.setAlignment(Qt.AlignCenter)

        self.analyticsSubPanelItemsLayout.addWidget(self.autologgerStatus)

        self.refreshDataButton = QPushButton(self.analyticsSubPanel)
        self.refreshDataButton.setObjectName(u"refreshDataButton")

        self.analyticsSubPanelItemsLayout.addWidget(self.refreshDataButton)

        self.startAutologgerButton = QPushButton(self.analyticsSubPanel)
        self.startAutologgerButton.setObjectName(u"startAutologgerButton")

        self.analyticsSubPanelItemsLayout.addWidget(self.startAutologgerButton)

        self.stopAutologgerButton = QPushButton(self.analyticsSubPanel)
        self.stopAutologgerButton.setObjectName(u"stopAutologgerButton")

        self.analyticsSubPanelItemsLayout.addWidget(self.stopAutologgerButton)

        self.restartAutologgerButton = QPushButton(self.analyticsSubPanel)
        self.restartAutologgerButton.setObjectName(u"restartAutologgerButton")

        self.analyticsSubPanelItemsLayout.addWidget(self.restartAutologgerButton)

        self.autologgerControlPanelButton = QPushButton(self.analyticsSubPanel)
        self.appPageNavButtons.addButton(self.autologgerControlPanelButton)
        self.autologgerControlPanelButton.setObjectName(u"autologgerControlPanelButton")
        self.autologgerControlPanelButton.setCheckable(True)

        self.analyticsSubPanelItemsLayout.addWidget(self.autologgerControlPanelButton)


        self.analyticsSubPanelLayout.addLayout(self.analyticsSubPanelItemsLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.analyticsSubPanelLayout.addItem(self.horizontalSpacer_2)


        self.navLayout.addWidget(self.analyticsSubPanel)

        self.navSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.navLayout.addItem(self.navSpacer)

        self.optionsAndExitLayout = QHBoxLayout()
        self.optionsAndExitLayout.setSpacing(4)
        self.optionsAndExitLayout.setObjectName(u"optionsAndExitLayout")
        self.optionsAndExitLayout.setContentsMargins(8, -1, 6, 8)
        self.settingsButton = QToolButton(self.nav)
        self.appPageNavButtons.addButton(self.settingsButton)
        self.settingsButton.setObjectName(u"settingsButton")
        icon = QIcon()
        icon.addFile(u":/images/images/SettingsIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsButton.setIcon(icon)
        self.settingsButton.setIconSize(QSize(40, 40))
        self.settingsButton.setCheckable(True)

        self.optionsAndExitLayout.addWidget(self.settingsButton)

        self.exitLayout = QVBoxLayout()
        self.exitLayout.setSpacing(2)
        self.exitLayout.setObjectName(u"exitLayout")
        self.logoutButton = QPushButton(self.nav)
        self.logoutButton.setObjectName(u"logoutButton")

        self.exitLayout.addWidget(self.logoutButton)

        self.quitButton = QPushButton(self.nav)
        self.quitButton.setObjectName(u"quitButton")

        self.exitLayout.addWidget(self.quitButton)


        self.optionsAndExitLayout.addLayout(self.exitLayout)


        self.navLayout.addLayout(self.optionsAndExitLayout)

        self.navContentSplitter.addWidget(self.nav)
        self.content = QStackedWidget(self.navContentSplitter)
        self.content.setObjectName(u"content")
        self.content.setMinimumSize(QSize(1, 0))
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.aboutWIPLabel = QLabel(self.aboutPage)
        self.aboutWIPLabel.setObjectName(u"aboutWIPLabel")
        self.aboutWIPLabel.setGeometry(QRect(280, 260, 101, 16))
        self.content.addWidget(self.aboutPage)
        self.analyticsPage = QWidget()
        self.analyticsPage.setObjectName(u"analyticsPage")
        self.analyticsWIPLabel = QLabel(self.analyticsPage)
        self.analyticsWIPLabel.setObjectName(u"analyticsWIPLabel")
        self.analyticsWIPLabel.setGeometry(QRect(270, 280, 121, 16))
        self.content.addWidget(self.analyticsPage)
        self.analyticsControlPanel = QWidget()
        self.analyticsControlPanel.setObjectName(u"analyticsControlPanel")
        self.analyticsControlPanelWIPLabel = QLabel(self.analyticsControlPanel)
        self.analyticsControlPanelWIPLabel.setObjectName(u"analyticsControlPanelWIPLabel")
        self.analyticsControlPanelWIPLabel.setGeometry(QRect(260, 260, 151, 16))
        self.content.addWidget(self.analyticsControlPanel)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.settingsWIPLabel = QLabel(self.settingsPage)
        self.settingsWIPLabel.setObjectName(u"settingsWIPLabel")
        self.settingsWIPLabel.setGeometry(QRect(280, 250, 101, 16))
        self.content.addWidget(self.settingsPage)
        self.navContentSplitter.addWidget(self.content)

        self.verticalLayout.addWidget(self.navContentSplitter)


        self.retranslateUi(AppMain)

        self.content.setCurrentIndex(0)

    # setupUi

    def retranslateUi(self, AppMain):
        AppMain.setWindowTitle(QCoreApplication.translate("AppMain", u"Form", None))
        self.aboutButton.setText(QCoreApplication.translate("AppMain", u"About", None))
        self.analyticsButton.setText(QCoreApplication.translate("AppMain", u"Analytics", None))
        self.autologgerStatus.setText(QCoreApplication.translate("AppMain", u"Autologger: [STATUS]", None))
        self.refreshDataButton.setText(QCoreApplication.translate("AppMain", u"Refresh Data", None))
        self.startAutologgerButton.setText(QCoreApplication.translate("AppMain", u"Start", None))
        self.stopAutologgerButton.setText(QCoreApplication.translate("AppMain", u"Stop", None))
        self.restartAutologgerButton.setText(QCoreApplication.translate("AppMain", u"Restart", None))
        self.autologgerControlPanelButton.setText(QCoreApplication.translate("AppMain", u"Control Panel", None))
        self.settingsButton.setText("")
        self.logoutButton.setText(QCoreApplication.translate("AppMain", u"Logout", None))
        self.quitButton.setText(QCoreApplication.translate("AppMain", u"Quit", None))
        self.aboutWIPLabel.setText(QCoreApplication.translate("AppMain", u"About WIP", None))
        self.analyticsWIPLabel.setText(QCoreApplication.translate("AppMain", u"Analytics WIP", None))
        self.analyticsControlPanelWIPLabel.setText(QCoreApplication.translate("AppMain", u"Analytics Control Panel WIP", None))
        self.settingsWIPLabel.setText(QCoreApplication.translate("AppMain", u"Settings WIP", None))
    # retranslateUi

