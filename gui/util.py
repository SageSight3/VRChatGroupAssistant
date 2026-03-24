from PySide6.QtWidgets import QWidget

def hide_ui_element(uiElement):
    if not uiElement.isHidden():
        uiElement.hide()

def show_ui_element(uiElement):
    if uiElement.isHidden():
        uiElement.show()