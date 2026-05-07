from PySide6.QtCore import QObject

from abc import ABCMeta, ABC

# Combine QObject's and ABC's metaclasses so Abstract Interlayer can inherit from both of them
# ABC - Abstract Base Class
class QObjectABCMeta(ABCMeta, QObject.__class__):
    pass

# AbstractInterlayer will inherit from QObject, since the interlayers
# may need to be able to receive or emit signals
class AbstractInterlayer(QObject, ABC, metaclass=QObjectABCMeta):
    pass