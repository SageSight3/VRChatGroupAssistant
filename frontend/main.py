import sys
from controller import Controller
import os

def main():
    
    # os.chdir("../../") for compiling to --one-dir with PyInstaller
    # os.chdir("../") for compiling to --one-file with PyInstaller with cwd in frontend dir of release build debug dir
    # print(os.getcwd())
    # input("Press enter to continue")
    app = Controller(sys.argv)

    app.run()

if __name__ == "__main__":
    main()