# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controlpanel.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_ControlPanel(object):
    def setupUi(self, ControlPanel):
        if not ControlPanel.objectName():
            ControlPanel.setObjectName(u"ControlPanel")
        ControlPanel.resize(800, 600)
        self.verticalLayout = QVBoxLayout(ControlPanel)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabs = QTabWidget(ControlPanel)
        self.tabs.setObjectName(u"tabs")
        self.groupControls = QWidget()
        self.groupControls.setObjectName(u"groupControls")
        self.groupControlsWIPLabel = QLabel(self.groupControls)
        self.groupControlsWIPLabel.setObjectName(u"groupControlsWIPLabel")
        self.groupControlsWIPLabel.setGeometry(QRect(340, 270, 49, 16))
        self.tabs.addTab(self.groupControls, "")
        self.errorLogs = QWidget()
        self.errorLogs.setObjectName(u"errorLogs")
        self.logsWIPLabel = QLabel(self.errorLogs)
        self.logsWIPLabel.setObjectName(u"logsWIPLabel")
        self.logsWIPLabel.setGeometry(QRect(310, 270, 131, 20))
        self.tabs.addTab(self.errorLogs, "")

        self.verticalLayout.addWidget(self.tabs)


        self.retranslateUi(ControlPanel)

        self.tabs.setCurrentIndex(0)

    # setupUi

    def retranslateUi(self, ControlPanel):
        ControlPanel.setWindowTitle(QCoreApplication.translate("ControlPanel", u"Form", None))
        self.groupControlsWIPLabel.setText(QCoreApplication.translate("ControlPanel", u"WIP", None))
        self.tabs.setTabText(self.tabs.indexOf(self.groupControls), QCoreApplication.translate("ControlPanel", u"Add/Remove Groups", None))
        self.logsWIPLabel.setText(QCoreApplication.translate("ControlPanel", u"WIP", None))
        self.tabs.setTabText(self.tabs.indexOf(self.errorLogs), QCoreApplication.translate("ControlPanel", u"Error Logs", None))
    # retranslateUi

