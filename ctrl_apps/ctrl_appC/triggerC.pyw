import subprocess
import sys
import keyboard
import threading
import os

if os.name == 'nt':
    CREATE_NEW_CONSOLE = subprocess.CREATE_NEW_CONSOLE
else:
    CREATE_NEW_CONSOLE = 0

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONTROL_SCRIPT = os.path.join(SCRIPT_DIR, "controlC.py")

# Function to launch control.py when Ctrl+Alt+P is pressed
def launch_control():
    python_exe = sys.executable.replace("pythonw.exe", "python.exe")
    subprocess.Popen(
        [python_exe, CONTROL_SCRIPT],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
        cwd=os.path.dirname(os.path.abspath(__file__))
    )

# Setup hotkey listener (Ctrl+Alt+P) to run control.py
def setup_hotkey():
    keyboard.add_hotkey("ctrl+alt+p", launch_control)

if __name__ == "__main__":
    # Setup the hotkey for launching control.py
    setup_hotkey()

    # Keep the script running while waiting for the hotkey press
    print("Listening for hotkey Ctrl + Alt + P to launch control.py... Press Ctrl + C to exit.")
    while True:
        pass  # Keeps the program running indefinitely
