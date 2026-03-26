import sys
from PySide6.QtWidgets import QApplication

from gui.mainwidget import MainWidget
from model.model import Model

class Controller():

    # Initialize frontend app components
    def __init__(self, args):
        self.__qapp = QApplication(args)

        self.__gui = MainWidget()
        self.__model = Model()

        # TEST
        for day in self.__model.get_days():
            print(day.date + " " + day.weekday)
        
        print(self.__model.get_online_counts_data().timestamps)
        print(self.__model.get_online_counts_data().online_counts)
        print(self.__model.get_online_counts_data().total_counts)
        print(self.__model.get_online_counts_data().online_percents)

    def setup_connections(self):
        pass

    # Run method for full front end
    def run(self):
        self.__gui.show()
        sys.exit(self.__qapp.exec())

def main():
    app = Controller(sys.argv)

    sys.exit(app.run())

if __name__ == "__main__":
    main()