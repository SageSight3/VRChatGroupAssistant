# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appcontainer.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QStackedWidget, QTextBrowser,
    QVBoxLayout, QWidget)

from interactivepage import InteractivePage

class Ui_AppContainer(object):
    def setupUi(self, AppContainer):
        if not AppContainer.objectName():
            AppContainer.setObjectName(u"AppContainer")
        AppContainer.resize(800, 600)
        self.verticalLayout = QVBoxLayout(AppContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.appContent = QStackedWidget(AppContainer)
        self.appContent.setObjectName(u"appContent")
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.verticalLayout_2 = QVBoxLayout(self.aboutPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.aboutText = QTextBrowser(self.aboutPage)
        self.aboutText.setObjectName(u"aboutText")

        self.verticalLayout_2.addWidget(self.aboutText)

        self.appContent.addWidget(self.aboutPage)
        self.interactivePage = InteractivePage()
        self.interactivePage.setObjectName(u"interactivePage")
        self.appContent.addWidget(self.interactivePage)

        self.verticalLayout.addWidget(self.appContent)


        self.retranslateUi(AppContainer)

        self.appContent.setCurrentIndex(0)

    # setupUi

    def retranslateUi(self, AppContainer):
        AppContainer.setWindowTitle(QCoreApplication.translate("AppContainer", u"Form", None))
        self.aboutText.setHtml(QCoreApplication.translate("AppContainer", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This app is a simple demo of how you can create muti view applications with PySide6 using custom (promoted) widgets for different pages.<br /><br />If you switch to next page, you will find working controls to interact with the app's main window, despite those controls being inside a subview of the main window's app container subview.<br /><br />The buttons at the top of the main window will also allo"
                        "w to switch between the different pages of the app container subview.<br /><br />The view hierarchy should look like this:<br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-weight:700; text-decoration: underline;\">MainWindow</span><br /><span style=\" font-family:'Courier New';\">\u251c\u2500\u2500 dashboard</span><br /><span style=\" font-family:'Courier New';\">\u2514\u2500\u2500 </span><span style=\" font-family:'Courier New'; font-weight:700; text-decoration: underline;\">appContainer</span><span style=\" font-family:'Courier New';\"><br />    \u251c\u2500\u2500 aboutPage<br />    \u2514\u2500\u2500 </span><span style=\" font-family:'Courier New'; font-weight:700; text-decoration: underline;\">interactivePage</span><span style=\" font-family:'Courier New'; font-weight:700;\"><br /><br /></span>Underlined items are different subviews with their own unique ui files, separate fr"
                        "om the main window's, implemented as custom widgets, while unbolded items are made of different default widgets and GUI elements that come shipped with Qt6/PySide.</p></body></html>", None))
    # retranslateUi

