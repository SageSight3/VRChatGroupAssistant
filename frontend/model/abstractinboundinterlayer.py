from PySide6.QtCore import Signal
from abc import abstractmethod

from model.abstractinterlayerbase import AbstractInterlayer

err_msg_base = "AbstractInboundInterlayer: "

class AbstractInboundInterlayer(AbstractInterlayer):

    def __init__(self, parent=None):
        super().__init__(parent)