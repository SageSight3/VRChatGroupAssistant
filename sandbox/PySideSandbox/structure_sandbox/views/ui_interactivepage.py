# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interactivepage.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_InteractivePage(object):
    def setupUi(self, InteractivePage):
        if not InteractivePage.objectName():
            InteractivePage.setObjectName(u"InteractivePage")
        InteractivePage.resize(800, 600)
        self.gridLayout = QGridLayout(InteractivePage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.toggleSecretButton = QPushButton(InteractivePage)
        self.toggleSecretButton.setObjectName(u"toggleSecretButton")

        self.gridLayout.addWidget(self.toggleSecretButton, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)


        self.retranslateUi(InteractivePage)
    # setupUi

    def retranslateUi(self, InteractivePage):
        InteractivePage.setWindowTitle(QCoreApplication.translate("InteractivePage", u"Form", None))
        self.toggleSecretButton.setText(QCoreApplication.translate("InteractivePage", u"Shhhh... It's a secret!", None))
    # retranslateUi

