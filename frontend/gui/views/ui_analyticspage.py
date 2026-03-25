# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analyticspage.ui'
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

from gui.onlinecountstracker import OnlineCountsTracker

class Ui_AnalyticsPage(object):
    def setupUi(self, AnalyticsPage):
        if not AnalyticsPage.objectName():
            AnalyticsPage.setObjectName(u"AnalyticsPage")
        AnalyticsPage.resize(800, 600)
        self.verticalLayout = QVBoxLayout(AnalyticsPage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabs = QTabWidget(AnalyticsPage)
        self.tabs.setObjectName(u"tabs")
        self.onlinePlayerCountsTracker = OnlineCountsTracker()
        self.onlinePlayerCountsTracker.setObjectName(u"onlinePlayerCountsTracker")
        self.tabs.addTab(self.onlinePlayerCountsTracker, "")
        self.placeholder = QWidget()
        self.placeholder.setObjectName(u"placeholder")
        self.placeholderLabel = QLabel(self.placeholder)
        self.placeholderLabel.setObjectName(u"placeholderLabel")
        self.placeholderLabel.setGeometry(QRect(320, 250, 141, 20))
        self.tabs.addTab(self.placeholder, "")

        self.verticalLayout.addWidget(self.tabs)


        self.retranslateUi(AnalyticsPage)

        self.tabs.setCurrentIndex(0)

    # setupUi

    def retranslateUi(self, AnalyticsPage):
        AnalyticsPage.setWindowTitle(QCoreApplication.translate("AnalyticsPage", u"Form", None))
        self.tabs.setTabText(self.tabs.indexOf(self.onlinePlayerCountsTracker), QCoreApplication.translate("AnalyticsPage", u"Online Player Counts", None))
        self.placeholderLabel.setText(QCoreApplication.translate("AnalyticsPage", u"Nothing to see here yet :(", None))
        self.tabs.setTabText(self.tabs.indexOf(self.placeholder), QCoreApplication.translate("AnalyticsPage", u"Placeholder", None))
    # retranslateUi

