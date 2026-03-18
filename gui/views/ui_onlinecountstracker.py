# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'onlinecountstracker.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QHBoxLayout, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_OnlineCountsTracker(object):
    def setupUi(self, OnlineCountsTracker):
        if not OnlineCountsTracker.objectName():
            OnlineCountsTracker.setObjectName(u"OnlineCountsTracker")
        OnlineCountsTracker.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OnlineCountsTracker.sizePolicy().hasHeightForWidth())
        OnlineCountsTracker.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(OnlineCountsTracker)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.controlsLayout = QHBoxLayout()
        self.controlsLayout.setSpacing(1)
        self.controlsLayout.setObjectName(u"controlsLayout")
        self.refreshButton = QToolButton(OnlineCountsTracker)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setAutoFillBackground(False)
        self.refreshButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/images/images/RefreshIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refreshButton.setIcon(icon)

        self.controlsLayout.addWidget(self.refreshButton)

        self.dateSelectionBox = QComboBox(OnlineCountsTracker)
        self.dateSelectionBox.addItem("")
        self.dateSelectionBox.addItem("")
        self.dateSelectionBox.addItem("")
        self.dateSelectionBox.addItem("")
        self.dateSelectionBox.addItem("")
        self.dateSelectionBox.addItem("")
        self.dateSelectionBox.addItem("")
        self.dateSelectionBox.addItem("")
        self.dateSelectionBox.setObjectName(u"dateSelectionBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dateSelectionBox.sizePolicy().hasHeightForWidth())
        self.dateSelectionBox.setSizePolicy(sizePolicy1)

        self.controlsLayout.addWidget(self.dateSelectionBox)

        self.graphPercentsCheckbox = QCheckBox(OnlineCountsTracker)
        self.graphPercentsCheckbox.setObjectName(u"graphPercentsCheckbox")

        self.controlsLayout.addWidget(self.graphPercentsCheckbox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.controlsLayout.addItem(self.horizontalSpacer)

        self.prevDateButton = QToolButton(OnlineCountsTracker)
        self.prevDateButton.setObjectName(u"prevDateButton")
        self.prevDateButton.setArrowType(Qt.LeftArrow)

        self.controlsLayout.addWidget(self.prevDateButton)

        self.nextDateButton = QToolButton(OnlineCountsTracker)
        self.nextDateButton.setObjectName(u"nextDateButton")
        self.nextDateButton.setArrowType(Qt.RightArrow)

        self.controlsLayout.addWidget(self.nextDateButton)


        self.verticalLayout.addLayout(self.controlsLayout)

        self.graphContainer = QVBoxLayout()
        self.graphContainer.setObjectName(u"graphContainer")
        self._placeholder = QCalendarWidget(OnlineCountsTracker)
        self._placeholder.setObjectName(u"_placeholder")

        self.graphContainer.addWidget(self._placeholder)


        self.verticalLayout.addLayout(self.graphContainer)


        self.retranslateUi(OnlineCountsTracker)

        QMetaObject.connectSlotsByName(OnlineCountsTracker)
    # setupUi

    def retranslateUi(self, OnlineCountsTracker):
        OnlineCountsTracker.setWindowTitle(QCoreApplication.translate("OnlineCountsTracker", u"Form", None))
        self.refreshButton.setText(QCoreApplication.translate("OnlineCountsTracker", u"...", None))
        self.dateSelectionBox.setItemText(0, QCoreApplication.translate("OnlineCountsTracker", u"_YYYY-MM-DD Weekday", None))
        self.dateSelectionBox.setItemText(1, QCoreApplication.translate("OnlineCountsTracker", u"_YYYY-MM-DD Weekday", None))
        self.dateSelectionBox.setItemText(2, QCoreApplication.translate("OnlineCountsTracker", u"_YYYY-MM-DD Weekday", None))
        self.dateSelectionBox.setItemText(3, QCoreApplication.translate("OnlineCountsTracker", u"_YYYY-MM-DD Weekday", None))
        self.dateSelectionBox.setItemText(4, QCoreApplication.translate("OnlineCountsTracker", u"_YYYY-MM-DD Weekday", None))
        self.dateSelectionBox.setItemText(5, QCoreApplication.translate("OnlineCountsTracker", u"_YYYY-MM-DD Weekday", None))
        self.dateSelectionBox.setItemText(6, QCoreApplication.translate("OnlineCountsTracker", u"_YYYY-MM-DD Weekday", None))
        self.dateSelectionBox.setItemText(7, QCoreApplication.translate("OnlineCountsTracker", u"_YYYY-MM-DD Weekday", None))

        self.graphPercentsCheckbox.setText(QCoreApplication.translate("OnlineCountsTracker", u"Graph as percents?", None))
        self.prevDateButton.setText(QCoreApplication.translate("OnlineCountsTracker", u"...", None))
        self.nextDateButton.setText(QCoreApplication.translate("OnlineCountsTracker", u"...", None))
    # retranslateUi

