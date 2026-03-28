import sys
from controller import Controller

def main():
    app = Controller(sys.argv)

    app.run()

if __name__ == "__main__":
    main()