from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal

from views.ui_appmain import Ui_AppMain

import util

class AppMain(QWidget):

    # FLCE signals
    from vrcga_signals import logout

    closeApp = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_AppMain()
        self.__view.setupUi(self)

        # App nav buttons
        self.__aboutButton = self.__view.aboutButton
        self.__analyticsButton = self.__view.analyticsButton
        self.__vrcgaServiceStatus = self.__view.vrcgaServiceStatus
        self.__refreshDataButtonWidget = self.__view.refreshDataButtonWidget
        self.__refreshDataButton = self.__view.refreshDataButton
        self.__controlPanelButton = self.__view.controlPanelButton
        self.__vrcgaServiceSubPanel = self.__view.vrcgaServiceSubPanel
        self.__startVRCGAServiceButton = self.__view.startVRCGAServiceButton
        self.__stopVRCGAServiceButton = self.__view.stopVRCGAServiceButton
        self.__restartVRCGAServiceButton = self.__view.restartVRCGAServiceButton
        self.__settingsButton = self.__view.settingsButton
        self.__logoutButton = self.__view.logoutButton
        self.__quitButton = self.__view.quitButton

        # App content container
        self.__content = self.__view.content

        # App content pages
        self.__aboutPage = self.__view.aboutPage
        self.__analyticsPage = self.__view.analyticsPage
        self.__controlPanel = self.__view.controlPanel
        self.__settingsPage = self.__view.settingsPage

        self.setup_connections()
        self.set_launch_state()

    def setup_connections(self):
        self.__aboutButton.clicked.connect(self.switch_to_about_page)
        self.__analyticsButton.clicked.connect(self.switch_to_analytics_page)
        self.__controlPanelButton.clicked.connect(self.switch_to_control_panel)
        self.__settingsButton.clicked.connect(self.switch_to_settings_page)

        self.__logoutButton.clicked.connect(self.log_out)
        self.__quitButton.clicked.connect(self.close_app)

    def set_launch_state(self):
        # Hide the analytics sub panel in the main app's nav widget
        self.default_state()

        # Set current app page to the app's about page
        self.switch_to_about_page()
        self.__aboutButton.setChecked(True)

    def default_state(self):
        util.hide_ui_element(self.__vrcgaServiceSubPanel)
        util.hide_ui_element(self.__refreshDataButtonWidget)

    @Slot()
    def switch_to_about_page(self):
        self.switch_page(self.__aboutPage)

    @Slot()
    def switch_to_analytics_page(self):
        self.switch_page(self.__analyticsPage)
        util.show_ui_element(self.__refreshDataButtonWidget)

    @Slot()
    def switch_to_control_panel(self):
        self.switch_page(self.__controlPanel)
        util.show_ui_element(self.__vrcgaServiceSubPanel)

    @Slot()
    def switch_to_settings_page(self):
        self.switch_page(self.__settingsPage)

    def switch_page(self, page):
        self.default_state()
        self.__content.setCurrentWidget(page)

    @Slot()
    def log_out(self):
        self.logout.emit()

    @Slot()
    def close_app(self):
        self.closeApp.emit()
