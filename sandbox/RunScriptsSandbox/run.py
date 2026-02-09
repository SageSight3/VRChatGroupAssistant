import subprocess
import psutil
import os.path
import sys
import time

# Set CWD

print(os.getcwd())
os.chdir("../../../")
print(os.getcwd())

# Backend executable name
backend_name = "VRChatGroupAssistant0.6.1.exe"

# Launch backend as an external process.
# Returns backend process name and pid, once launched
def launch_backend():
    backendExePath = os.path.dirname(__file__) + "/../../../../" + backend_name
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
    
    backend_process = is_running(backend_name)
    while not backend_process[0]:
        time.sleep(1)
        backend_process = is_running(backend_name)

    return backend_process[1]

# Search for external process
def is_running(name):
    for process in  psutil.process_iter(["name"]):
        if process.info["name"] == name:
            return (True, process)
    return (False, None)

# Check if backend is running, and if not, launch it
# Returns backend process name and pid
def startup():
    backend_running = is_running(backend_name)
    if backend_running[0]:
        print("Backend is already running")
        print(backend_running[1])

        return backend_running[1]
    else:
        print("Backend process not found")
        print("Starting backend...")
        backend_process = launch_backend()
        print("Backend launched")
        print(backend_process)

        return backend_process

# Stops the backend process
# Attempts force kill if it can't terminate it normally
def stop_backend(backend_process: psutil.Process):
    try:
        backend_process.terminate()
        print("Backend stopped succesfully")
    except Exception as error:
        print(f"ERROR: Failed to terminate backend process: {error}")
    
    time.sleep(3)
    try:
        if is_running(backend_process.name)[0] == True:
            print("Backend Process failed to terminate successfully")
            print("Attempting force kill")
            backend_process.kill()
    except Exception as error:
        print(f"ERROR: Failed to force kill backend process: {error}")

backend_process = startup()

quit_backend = input("Type \"quit\" and hit enter to close process: ")
if quit_backend == "quit":
    stop_backend(backend_process)

exit = input("Press enter to exit")