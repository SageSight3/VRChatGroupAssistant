# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quitdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_QuitDialog(object):
    def setupUi(self, QuitDialog):
        if not QuitDialog.objectName():
            QuitDialog.setObjectName(u"QuitDialog")
        QuitDialog.resize(500, 250)
        QuitDialog.setMinimumSize(QSize(500, 250))
        QuitDialog.setMaximumSize(QSize(500, 250))
        self.verticalLayout = QVBoxLayout(QuitDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.quitDialogIcon = QLabel(QuitDialog)
        self.quitDialogIcon.setObjectName(u"quitDialogIcon")
        self.quitDialogIcon.setMinimumSize(QSize(96, 96))
        self.quitDialogIcon.setMaximumSize(QSize(96, 96))
        self.quitDialogIcon.setPixmap(QPixmap(u":/images/images/QuitDialogIcon.png"))
        self.quitDialogIcon.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.quitDialogIcon)

        self.quitTextBrowser = QTextBrowser(QuitDialog)
        self.quitTextBrowser.setObjectName(u"quitTextBrowser")
        self.quitTextBrowser.setMaximumSize(QSize(16777215, 130))

        self.horizontalLayout_2.addWidget(self.quitTextBrowser)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.showAgainCheckboxLayout = QHBoxLayout()
        self.showAgainCheckboxLayout.setObjectName(u"showAgainCheckboxLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.showAgainCheckboxLayout.addItem(self.horizontalSpacer_5)

        self.showAgainCheckbox = QCheckBox(QuitDialog)
        self.showAgainCheckbox.setObjectName(u"showAgainCheckbox")

        self.showAgainCheckboxLayout.addWidget(self.showAgainCheckbox)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.showAgainCheckboxLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.showAgainCheckboxLayout)

        self.separator = QFrame(QuitDialog)
        self.separator.setObjectName(u"separator")
        self.separator.setLineWidth(1)
        self.separator.setMidLineWidth(10)
        self.separator.setFrameShape(QFrame.Shape.HLine)
        self.separator.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.separator)

        self.quitCancelButtonsLayout = QHBoxLayout()
        self.quitCancelButtonsLayout.setObjectName(u"quitCancelButtonsLayout")
        self.quitCancelButtonsLayout.setContentsMargins(-1, 10, 0, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.quitCancelButtonsLayout.addItem(self.horizontalSpacer)

        self.quitCancelButtonBox = QDialogButtonBox(QuitDialog)
        self.quitCancelButtonBox.setObjectName(u"quitCancelButtonBox")
        self.quitCancelButtonBox.setLayoutDirection(Qt.LeftToRight)
        self.quitCancelButtonBox.setStandardButtons(QDialogButtonBox.No|QDialogButtonBox.Yes)

        self.quitCancelButtonsLayout.addWidget(self.quitCancelButtonBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.quitCancelButtonsLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.quitCancelButtonsLayout)


        self.retranslateUi(QuitDialog)
    # setupUi

    def retranslateUi(self, QuitDialog):
        QuitDialog.setWindowTitle(QCoreApplication.translate("QuitDialog", u"VRChat Group Assistant", None))
        self.quitDialogIcon.setText("")
        self.quitTextBrowser.setHtml(QCoreApplication.translate("QuitDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">VRCGA Service is still running! Are you sure you want to quit?</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Note: If you stop the VRCGA service, you won't be a"
                        "ble to get analytics data for your group, while it's offline.</p></body></html>", None))
        self.showAgainCheckbox.setText(QCoreApplication.translate("QuitDialog", u"Don't ask me again", None))
    # retranslateUi

