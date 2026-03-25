import sys
from PySide6.QtWidgets import QApplication

from gui.mainwidget import MainWidget

def main():
    app = QApplication(sys.argv)

    window = MainWidget()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()