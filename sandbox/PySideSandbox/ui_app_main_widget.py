# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_main_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

from ui_about_page_widget.py import Ui_AboutPage
from ui_test_page_widget.py import Ui_TestPageWidget

class Ui_AppMainWidget(object):
    def setupUi(self, AppMainWidget):
        if not AppMainWidget.objectName():
            AppMainWidget.setObjectName(u"AppMainWidget")
        AppMainWidget.resize(800, 600)
        self.verticalLayout = QVBoxLayout(AppMainWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleBar = QHBoxLayout()
        self.titleBar.setObjectName(u"titleBar")
        self.appTitle = QLabel(AppMainWidget)
        self.appTitle.setObjectName(u"appTitle")

        self.titleBar.addWidget(self.appTitle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.titleBar.addItem(self.horizontalSpacer)

        self.logoutButton = QPushButton(AppMainWidget)
        self.logoutButton.setObjectName(u"logoutButton")

        self.titleBar.addWidget(self.logoutButton)


        self.verticalLayout.addLayout(self.titleBar)

        self.appNav = QTabWidget(AppMainWidget)
        self.appNav.setObjectName(u"appNav")
        self.customWidgetTestTab = Ui_TestPageWidget()
        self.customWidgetTestTab.setObjectName(u"customWidgetTestTab")
        self.appNav.addTab(self.customWidgetTestTab, "")
        self.testWidgetTab = QWidget()
        self.testWidgetTab.setObjectName(u"testWidgetTab")
        self.verticalLayout_2 = QVBoxLayout(self.testWidgetTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedCheckbox = QWidget(self.testWidgetTab)
        self.stackedCheckbox.setObjectName(u"stackedCheckbox")
        self.horizontalLayout = QHBoxLayout(self.stackedCheckbox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.stackedCheckbox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.line = QFrame(self.stackedCheckbox)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout.addWidget(self.line)

        self.checkBox = QCheckBox(self.stackedCheckbox)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)


        self.verticalLayout_2.addWidget(self.stackedCheckbox)

        self.tabCheckbox = QWidget(self.testWidgetTab)
        self.tabCheckbox.setObjectName(u"tabCheckbox")
        self.horizontalLayout_2 = QHBoxLayout(self.tabCheckbox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.tabCheckbox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.line_2 = QFrame(self.tabCheckbox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.checkBox_2 = QCheckBox(self.tabCheckbox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_2.addWidget(self.checkBox_2)


        self.verticalLayout_2.addWidget(self.tabCheckbox)

        self.customWidgetsCheckbox = QWidget(self.testWidgetTab)
        self.customWidgetsCheckbox.setObjectName(u"customWidgetsCheckbox")
        self.horizontalLayout_3 = QHBoxLayout(self.customWidgetsCheckbox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.customWidgetsCheckbox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.line_3 = QFrame(self.customWidgetsCheckbox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.checkBox_3 = QCheckBox(self.customWidgetsCheckbox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_3.addWidget(self.checkBox_3)


        self.verticalLayout_2.addWidget(self.customWidgetsCheckbox)

        self.appNav.addTab(self.testWidgetTab, "")
        self.aboutTab = Ui_AboutPage()
        self.aboutTab.setObjectName(u"aboutTab")
        self.appNav.addTab(self.aboutTab, "")

        self.verticalLayout.addWidget(self.appNav)


        self.retranslateUi(AppMainWidget)

        self.appNav.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AppMainWidget)
    # setupUi

    def retranslateUi(self, AppMainWidget):
        AppMainWidget.setWindowTitle(QCoreApplication.translate("AppMainWidget", u"VRChat Group Assistant", None))
        self.appTitle.setText(QCoreApplication.translate("AppMainWidget", u"VRCGA GUI Sandbox", None))
        self.logoutButton.setText(QCoreApplication.translate("AppMainWidget", u"Logout", None))
        self.appNav.setTabText(self.appNav.indexOf(self.customWidgetTestTab), QCoreApplication.translate("AppMainWidget", u"Custom Widget Test", None))
        self.label.setText(QCoreApplication.translate("AppMainWidget", u"Stacked Widget Working", None))
        self.checkBox.setText(QCoreApplication.translate("AppMainWidget", u"CheckBox", None))
        self.label_2.setText(QCoreApplication.translate("AppMainWidget", u"Tab Widget Working", None))
        self.checkBox_2.setText(QCoreApplication.translate("AppMainWidget", u"CheckBox", None))
        self.label_3.setText(QCoreApplication.translate("AppMainWidget", u"Custom Widgets Working", None))
        self.checkBox_3.setText(QCoreApplication.translate("AppMainWidget", u"CheckBox", None))
        self.appNav.setTabText(self.appNav.indexOf(self.testWidgetTab), QCoreApplication.translate("AppMainWidget", u"Test", None))
        self.appNav.setTabText(self.appNav.indexOf(self.aboutTab), QCoreApplication.translate("AppMainWidget", u"About", None))
    # retranslateUi

