from PySide6.QtWidgets import QComboBox, QCompleter
from PySide6.QtCore import Qt, QSortFilterProxyModel


def hide_ui_element(uiElement):
    if not uiElement.isHidden():
        uiElement.hide()

def show_ui_element(uiElement):
    if uiElement.isHidden():
        uiElement.show()

class SearchableComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.NoInsert)
        
        filter_model = QSortFilterProxyModel(self)
        filter_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        filter_model.setSourceModel(self.model())
        
        completer = QCompleter(filter_model, self)
        completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)

        self.setCompleter(completer)
        self.lineEdit().textEdited.connect(filter_model.setFilterFixedString)