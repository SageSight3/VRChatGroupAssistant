import sys

from signals import CustomSignals

class WidgetUI(CustomSignals):
    # https://doc.qt.io/qtforpython-6/tutorials/basictutorial/signals_and_slots.html

    def __init__(self, a_ui_widget):

        # initialize CustomSignals, signal senders won't stay in memory
        # if not done
        super().__init__()

        self.__dial = a_ui_widget.dial
        self.__label = a_ui_widget.label
        self.__button = a_ui_widget.pushButton
        
        self.__dial.valueChanged.connect(self.on_dial_value_changed)
        self.__button.clicked.connect(self.on_button_clicked)

    def on_dial_value_changed(self):
        new_val = self.__dial.value()
        self.__label.setText(f"{new_val}")

    def on_button_clicked(self):
        self.change_page.emit(0)
