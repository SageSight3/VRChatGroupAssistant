from PySide6.QtCore import Signal, QObject

class CustomSignals(QObject):
    change_page = Signal(int)