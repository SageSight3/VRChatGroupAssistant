from PySide6 import QtCore, QtWidgets

# Reference: https://gist.github.com/rBrenick/cb4c29f8a2d094e9df3e321a87eceb04
# Make sure ComboBox is set to editable in qt designer, to avoid bug of pyside6-uic
# it setting it to not be editable
class SearchableComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setEditable(True)
        self.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        
        filter_model = QtCore.QSortFilterProxyModel(self)
        filter_model.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        filter_model.setSourceModel(self.model())
        
        completer = QtWidgets.QCompleter(filter_model, self)
        completer.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)

        self.setCompleter(completer)
        self.lineEdit().textEdited.connect(filter_model.setFilterFixedString)