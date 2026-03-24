from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal

from views.ui_appmain import Ui_AppMain

import util

class AppMain(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__view = Ui_AppMain()
        self.__view.setupUi(self)

        # App nav buttons
        self.__aboutButton = self.__view.aboutButton
        self.__analyticsButton = self.__view.analyticsButton
        self.__analyticsSubPanel = self.__view.analyticsSubPanel
        self.__autologgerStatus = self.__view.autologgerStatus
        self.__refreshDataButton = self.__view.refreshDataButton
        self.__startAutologgerButton = self.__view.startAutologgerButton
        self.__stopAutologgerButton = self.__view.stopAutologgerButton
        self.__restartAutologgerButton = self.__view.restartAutologgerButton
        self.__analyticsControlPanelButton = self.__view.autologgerControlPanelButton
        self.__settingsButton = self.__view.settingsButton
        self.__logoutButton = self.__view.logoutButton
        self.__quitButton = self.__view.quitButton

        # App content container
        self.__content = self.__view.content

        # App content pages
        self.__aboutPage = self.__view.aboutPage
        self.__analyticsPage = self.__view.analyticsPage
        self.__analyticsControlPanel = self.__view.analyticsControlPanel
        self.__settingsPage = self.__view.settingsPage

        self.setup_connections()
        self.set_launch_state()

    def setup_connections(self):
        self.__aboutButton.clicked.connect(self.switch_to_about_page)
        self.__analyticsButton.clicked.connect(self.switch_to_analytics_page)
        self.__analyticsControlPanelButton.clicked.connect(self.switch_to_analytics_control_panel)
        self.__settingsButton.clicked.connect(self.switch_to_settings_page)

    def set_launch_state(self):
        # Hide the analytics sub panel in the main app's nav widget
        self.default_state()

        # Set current app page to the app's about page
        self.switch_to_about_page()
        self.__aboutButton.setChecked(True)

    def default_state(self):
        util.hide_ui_element(self.__analyticsSubPanel)

    @Slot()
    def switch_to_about_page(self):
        self.switch_page(self.__aboutPage)

    @Slot()
    def switch_to_analytics_page(self):
        self.switch_page(self.__analyticsPage)
        util.show_ui_element(self.__analyticsSubPanel)

    @Slot()
    def switch_to_analytics_control_panel(self):
        self.switch_page(self.__analyticsControlPanel)
        
        # Still need to show analytics subpanel, since it's hidden in switch_page()
        util.show_ui_element(self.__analyticsSubPanel)

    @Slot()
    def switch_to_settings_page(self):
        self.switch_page(self.__settingsPage)

    def switch_page(self, page):
        self.default_state()
        self.__content.setCurrentWidget(page)
