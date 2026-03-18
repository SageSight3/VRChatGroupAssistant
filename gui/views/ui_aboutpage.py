# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutpage.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QTextBrowser,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_AboutPage(object):
    def setupUi(self, AboutPage):
        if not AboutPage.objectName():
            AboutPage.setObjectName(u"AboutPage")
        AboutPage.resize(800, 600)
        self.verticalLayout = QVBoxLayout(AboutPage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabs = QTabWidget(AboutPage)
        self.tabs.setObjectName(u"tabs")
        self.guideTab = QWidget()
        self.guideTab.setObjectName(u"guideTab")
        self.verticalLayout_3 = QVBoxLayout(self.guideTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.guide = QTextBrowser(self.guideTab)
        self.guide.setObjectName(u"guide")

        self.verticalLayout_3.addWidget(self.guide)

        self.tabs.addTab(self.guideTab, "")
        self.creditsTab = QWidget()
        self.creditsTab.setObjectName(u"creditsTab")
        self.verticalLayout_2 = QVBoxLayout(self.creditsTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.credits = QTextBrowser(self.creditsTab)
        self.credits.setObjectName(u"credits")

        self.verticalLayout_2.addWidget(self.credits)

        self.tabs.addTab(self.creditsTab, "")

        self.verticalLayout.addWidget(self.tabs)


        self.retranslateUi(AboutPage)

        self.tabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(AboutPage)
    # setupUi

    def retranslateUi(self, AboutPage):
        AboutPage.setWindowTitle(QCoreApplication.translate("AboutPage", u"Form", None))
        self.guide.setHtml(QCoreApplication.translate("AboutPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabs.setTabText(self.tabs.indexOf(self.guideTab), QCoreApplication.translate("AboutPage", u"Guide", None))
        self.tabs.setTabText(self.tabs.indexOf(self.creditsTab), QCoreApplication.translate("AboutPage", u"Credits", None))
    # retranslateUi

