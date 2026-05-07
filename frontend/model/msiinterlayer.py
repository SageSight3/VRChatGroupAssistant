from model.abstractinboundinterlayer import AbstractInboundInterlayer

class MSIInterlayer(AbstractInboundInterlayer):

    def __init__(self, parent=None):
        super().__init__(parent)