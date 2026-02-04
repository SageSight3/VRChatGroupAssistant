import subprocess
import os.path
import sys

# This was written in the release build dir, to begin experimenting/testing how the program will launch

backendExePath = os.path.dirname(__file__) + "/../../../../VRChatGroupAssistant0.6.1.exe"
print(backendExePath)
print(os.getcwd())
os.chdir("../../../")
print(os.getcwd())

run_args = [backendExePath]

# Make so backend program doesn't close when prcess is closed
# Popen args needed differ, depending on OS

if sys.platform == "win32": # for Windows
    subprocess.Popen(
        run_args,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS,
        shell=True
    )
else: # for POSIX systems (like linux and macOS)
    subprocess.Popen(
        run_args,
        start_new_session=True,
        shell=True
    )

exit = input("Press enter to exit")