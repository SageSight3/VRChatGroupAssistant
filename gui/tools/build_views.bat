REM Make sure we're executing commands from the dir the batch file's located in
cd %~dp0

CALL "..\..\.venv\\Scripts\activate.bat"

ECHO ON

pyside6-uic ..\views\mainwidget.ui -o ..\views\ui_mainwidget.py -a
pyside6-uic ..\views\applogin.ui -o ..\views\ui_applogin.py -a
pyside6-uic ..\views\appmain.ui -o ..\views\ui_appmain.py -a
pyside6-uic ..\views\analyticspage.ui -o ..\views\ui_analyticspage.py -a
pyside6-uic ..\views\autologgercontrolpanel.ui -o ..\views\ui_autologgercontrolpanel.py -a
pyside6-uic ..\views\onlinecountstracker.ui -o ..\views\ui_onlinecountstracker.py -a
pyside6-uic ..\views\quitdialog.ui -o ..\views\ui_quitdialog.py -a
pyside6-rcc ..\resources.qrc -o ..\resources_rc.py

CALL "..\..\.venv\\Scripts\deactivate.bat"
echo venv deactivated

ECHO ON

pause