# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'two_factor_page_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import resources_rc
import resources_rc

class Ui_TwoFactorAuthPage(object):
    def setupUi(self, TwoFactorAuthPage):
        if not TwoFactorAuthPage.objectName():
            TwoFactorAuthPage.setObjectName(u"TwoFactorAuthPage")
        TwoFactorAuthPage.resize(800, 600)
        self.gridLayout = QGridLayout(TwoFactorAuthPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.loginFailedWidget = QWidget(TwoFactorAuthPage)
        self.loginFailedWidget.setObjectName(u"loginFailedWidget")
        self.horizontalLayout = QHBoxLayout(self.loginFailedWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.errorImage = QLabel(self.loginFailedWidget)
        self.errorImage.setObjectName(u"errorImage")
        self.errorImage.setPixmap(QPixmap(u":/images/images/vrc_login_failed.png"))

        self.horizontalLayout.addWidget(self.errorImage)

        self.loginFailedDesc = QLabel(self.loginFailedWidget)
        self.loginFailedDesc.setObjectName(u"loginFailedDesc")

        self.horizontalLayout.addWidget(self.loginFailedDesc)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout.addWidget(self.loginFailedWidget, 1, 1, 1, 1)

        self.label = QLabel(TwoFactorAuthPage)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.twoFactorCodeIn = QLineEdit(TwoFactorAuthPage)
        self.twoFactorCodeIn.setObjectName(u"twoFactorCodeIn")
        self.twoFactorCodeIn.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.twoFactorCodeIn, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.pushButton = QPushButton(TwoFactorAuthPage)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 1, 1, 1)


        self.retranslateUi(TwoFactorAuthPage)

        QMetaObject.connectSlotsByName(TwoFactorAuthPage)
    # setupUi

    def retranslateUi(self, TwoFactorAuthPage):
        TwoFactorAuthPage.setWindowTitle(QCoreApplication.translate("TwoFactorAuthPage", u"Verify 2FA", None))
        self.errorImage.setText("")
        self.loginFailedDesc.setText(QCoreApplication.translate("TwoFactorAuthPage", u"Invalid Code", None))
        self.label.setText(QCoreApplication.translate("TwoFactorAuthPage", u"Two Factor Authentication", None))
        self.twoFactorCodeIn.setText("")
        self.twoFactorCodeIn.setPlaceholderText(QCoreApplication.translate("TwoFactorAuthPage", u"Enter 2fa Code from app or email", None))
        self.pushButton.setText(QCoreApplication.translate("TwoFactorAuthPage", u"Verify", None))
    # retranslateUi

