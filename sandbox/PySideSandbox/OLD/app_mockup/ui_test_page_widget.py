# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_page_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

from custom_widgets import SearchableComboBox

class Ui_TestPageWidget(object):
    def setupUi(self, TestPageWidget):
        if not TestPageWidget.objectName():
            TestPageWidget.setObjectName(u"TestPageWidget")
        TestPageWidget.resize(800, 600)
        self.verticalLayout = QVBoxLayout(TestPageWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.testComboBox = SearchableComboBox(TestPageWidget)
        self.testComboBox.setObjectName(u"testComboBox")
        self.testComboBox.setEditable(True)

        self.verticalLayout.addWidget(self.testComboBox)

        self.graphButton = QPushButton(TestPageWidget)
        self.graphButton.setObjectName(u"graphButton")

        self.verticalLayout.addWidget(self.graphButton)

        self.testLabel = QLabel(TestPageWidget)
        self.testLabel.setObjectName(u"testLabel")

        self.verticalLayout.addWidget(self.testLabel)

        self.testWidget = QWidget(TestPageWidget)
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


        self.retranslateUi(TestPageWidget)

        QMetaObject.connectSlotsByName(TestPageWidget)
    # setupUi

    def retranslateUi(self, TestPageWidget):
        TestPageWidget.setWindowTitle(QCoreApplication.translate("TestPageWidget", u"TestPageWidget", None))
        self.graphButton.setText(QCoreApplication.translate("TestPageWidget", u"Graph Selected Option", None))
        self.testLabel.setText(QCoreApplication.translate("TestPageWidget", u"TextLabel", None))
        self.graphLabel.setText(QCoreApplication.translate("TestPageWidget", u"Graph ", None))
        self.newValsButton.setText(QCoreApplication.translate("TestPageWidget", u"Generate New Options", None))
    # retranslateUi

