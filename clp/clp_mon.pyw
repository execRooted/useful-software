import pyperclip
import time
import json
import os
from datetime import datetime
import keyboard
import subprocess
import threading
import subprocess
import sys

# Needed for CREATE_NEW_CONSOLE
if os.name == 'nt':
    CREATE_NEW_CONSOLE = subprocess.CREATE_NEW_CONSOLE
else:
    CREATE_NEW_CONSOLE = 0




SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(SCRIPT_DIR, "clipboard_history.json")
CLP_SCRIPT = os.path.join(SCRIPT_DIR, "clp.py")

MAX_HISTORY = 50
POLL_INTERVAL = 0.5

def ensure_history_file():
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f)

def load_history():
    ensure_history_file()
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_history(history):
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2)

def monitor_clipboard():
    history = load_history()
    known_entries = set(entry for _, entry in history)
    last_clipboard = pyperclip.paste()

    print("Clipboard monitor running. Press Ctrl+Alt+H to view history. Press Ctrl+C to stop.")

    while True:
        try:
            current = pyperclip.paste()
            if current.strip() and current != last_clipboard and current not in known_entries:
                last_clipboard = current
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                history.append((timestamp, current))
                known_entries.add(current)
                if len(history) > MAX_HISTORY:
                    removed = history.pop(0)
                    known_entries.discard(removed[1])
                save_history(history)
                print(f"[{timestamp}] New clipboard entry saved.")
            time.sleep(POLL_INTERVAL)
        except KeyboardInterrupt:
            print("\nMonitor stopped.")
            break

def launch_clp():
    subprocess.Popen(
        [sys.executable, "clp.py"],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
        cwd=os.path.dirname(os.path.abspath(__file__))
    )

def setup_hotkey():
    keyboard.add_hotkey("ctrl+alt+h", launch_clp)

if __name__ == "__main__":
    ensure_history_file()
    setup_hotkey()

    # Run clipboard monitor in main thread
    # and allow hotkeys to work by starting keyboard listener in background
    keyboard_thread = threading.Thread(target=keyboard.wait, args=("esc",), daemon=True)
    keyboard_thread.start()

    monitor_clipboard()
