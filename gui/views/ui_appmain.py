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

from aboutpage import AboutPage
from analyticspage import AnalyticsPage
from controlpanel import ControlPanel
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

        self.refreshDataButtonWidget = QWidget(self.nav)
        self.refreshDataButtonWidget.setObjectName(u"refreshDataButtonWidget")
        self.refreshDataButtonLayout = QHBoxLayout(self.refreshDataButtonWidget)
        self.refreshDataButtonLayout.setSpacing(0)
        self.refreshDataButtonLayout.setObjectName(u"refreshDataButtonLayout")
        self.refreshDataButtonLayout.setContentsMargins(0, 1, 0, 20)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.refreshDataButtonLayout.addItem(self.horizontalSpacer_3)

        self.refreshDataButton = QPushButton(self.refreshDataButtonWidget)
        self.refreshDataButton.setObjectName(u"refreshDataButton")

        self.refreshDataButtonLayout.addWidget(self.refreshDataButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.refreshDataButtonLayout.addItem(self.horizontalSpacer_4)


        self.navLayout.addWidget(self.refreshDataButtonWidget)

        self.controlPanelButton = QPushButton(self.nav)
        self.appPageNavButtons.addButton(self.controlPanelButton)
        self.controlPanelButton.setObjectName(u"controlPanelButton")
        self.controlPanelButton.setCheckable(True)

        self.navLayout.addWidget(self.controlPanelButton)

        self.vrcgaServiceSubPanel = QWidget(self.nav)
        self.vrcgaServiceSubPanel.setObjectName(u"vrcgaServiceSubPanel")
        self.analyticsSubPanelLayout = QHBoxLayout(self.vrcgaServiceSubPanel)
        self.analyticsSubPanelLayout.setObjectName(u"analyticsSubPanelLayout")
        self.analyticsSubPanelLayout.setContentsMargins(9, 0, 9, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.analyticsSubPanelLayout.addItem(self.horizontalSpacer)

        self.vrcgaServiceSubPanelItemsLayout = QVBoxLayout()
        self.vrcgaServiceSubPanelItemsLayout.setSpacing(2)
        self.vrcgaServiceSubPanelItemsLayout.setObjectName(u"vrcgaServiceSubPanelItemsLayout")
        self.vrcgaServiceStatus = QLabel(self.vrcgaServiceSubPanel)
        self.vrcgaServiceStatus.setObjectName(u"vrcgaServiceStatus")
        self.vrcgaServiceStatus.setAlignment(Qt.AlignCenter)

        self.vrcgaServiceSubPanelItemsLayout.addWidget(self.vrcgaServiceStatus)

        self.startVRCGAServiceButton = QPushButton(self.vrcgaServiceSubPanel)
        self.startVRCGAServiceButton.setObjectName(u"startVRCGAServiceButton")

        self.vrcgaServiceSubPanelItemsLayout.addWidget(self.startVRCGAServiceButton)

        self.stopVRCGAServiceButton = QPushButton(self.vrcgaServiceSubPanel)
        self.stopVRCGAServiceButton.setObjectName(u"stopVRCGAServiceButton")

        self.vrcgaServiceSubPanelItemsLayout.addWidget(self.stopVRCGAServiceButton)

        self.restartVRCGAServiceButton = QPushButton(self.vrcgaServiceSubPanel)
        self.restartVRCGAServiceButton.setObjectName(u"restartVRCGAServiceButton")

        self.vrcgaServiceSubPanelItemsLayout.addWidget(self.restartVRCGAServiceButton)


        self.analyticsSubPanelLayout.addLayout(self.vrcgaServiceSubPanelItemsLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.analyticsSubPanelLayout.addItem(self.horizontalSpacer_2)


        self.navLayout.addWidget(self.vrcgaServiceSubPanel)

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
        self.aboutPage = AboutPage()
        self.aboutPage.setObjectName(u"aboutPage")
        self.content.addWidget(self.aboutPage)
        self.analyticsPage = AnalyticsPage()
        self.analyticsPage.setObjectName(u"analyticsPage")
        self.content.addWidget(self.analyticsPage)
        self.controlPanel = ControlPanel()
        self.controlPanel.setObjectName(u"controlPanel")
        self.content.addWidget(self.controlPanel)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.settingsWIPLabel = QLabel(self.settingsPage)
        self.settingsWIPLabel.setObjectName(u"settingsWIPLabel")
        self.settingsWIPLabel.setGeometry(QRect(280, 250, 101, 16))
        self.content.addWidget(self.settingsPage)
        self.navContentSplitter.addWidget(self.content)

        self.verticalLayout.addWidget(self.navContentSplitter)


        self.retranslateUi(AppMain)

        self.content.setCurrentIndex(2)

    # setupUi

    def retranslateUi(self, AppMain):
        AppMain.setWindowTitle(QCoreApplication.translate("AppMain", u"Form", None))
        self.aboutButton.setText(QCoreApplication.translate("AppMain", u"About", None))
        self.analyticsButton.setText(QCoreApplication.translate("AppMain", u"Analytics", None))
        self.refreshDataButton.setText(QCoreApplication.translate("AppMain", u"Refresh Data", None))
        self.controlPanelButton.setText(QCoreApplication.translate("AppMain", u"Control Panel", None))
        self.vrcgaServiceStatus.setText(QCoreApplication.translate("AppMain", u"VRCGA Service: [STATUS]", None))
        self.startVRCGAServiceButton.setText(QCoreApplication.translate("AppMain", u"Start", None))
        self.stopVRCGAServiceButton.setText(QCoreApplication.translate("AppMain", u"Stop", None))
        self.restartVRCGAServiceButton.setText(QCoreApplication.translate("AppMain", u"Restart", None))
        self.settingsButton.setText("")
        self.logoutButton.setText(QCoreApplication.translate("AppMain", u"Logout", None))
        self.quitButton.setText(QCoreApplication.translate("AppMain", u"Quit", None))
        self.settingsWIPLabel.setText(QCoreApplication.translate("AppMain", u"Settings WIP", None))
    # retranslateUi

