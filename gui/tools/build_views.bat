cd %~dp0

CALL "..\..\.venv\\Scripts\activate.bat"

ECHO ON

pyside6-uic ..\views\mainwidget.ui -o ..\views\ui_mainwidget.py
pyside6-uic ..\views\applogin.ui -o ..\views\ui_applogin.py
pyside6-uic ..\views\appmain.ui -o ..\views\ui_appmain.py
pyside6-uic ..\views\analyticspage.ui -o ..\views\ui_analyticspage.py
pyside6-uic ..\views\autologgercontrolpanel.ui -o ..\views\ui_autologgercontrolpanel.py
pyside6-uic ..\views\onlinecountstracker.ui -o ..\views\ui_onlinecountstracker.py
pyside6-rcc ..\resources.qrc -o ..\resources_rc.py

CALL "..\..\.venv\\Scripts\deactivate.bat"
echo venv deactivated

ECHO ON

pause