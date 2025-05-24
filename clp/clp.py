import pyperclip
import json
import os

os.system("title CLP Manager - by execRooted")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(SCRIPT_DIR, "clipboard_history.json")

MAX_ENTRIES_TO_SHOW = 10

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def delete_history_file():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print("\n✅ Clipboard history deleted.")
    else:
        print("\n No history file to delete.")
    input("Press Enter to exit...")
    exit()

def show_history_menu(history):
    if not history:
        print("Clipboard history is empty.")
        input("Press Enter to exit...")
        return

    print("\n--- Clipboard History ---\n")
    recent = history[-MAX_ENTRIES_TO_SHOW:]
    for i, (timestamp, entry) in enumerate(reversed(recent), 1):
        display = entry.replace("\n", " ")[:70]
        print(f"{i}. [{timestamp}] {display}{'...' if len(entry) > 70 else ''}")

    delete_option_index = len(recent) + 1
    print(f"{delete_option_index}. Delete clipboard history")

    print("\nSelect an entry to copy to clipboard.")
    choice = input(f"Choice (1–{delete_option_index} or Enter to cancel): ").strip()

    if choice == "":
        print("No selection made. Exiting.")
        return

    if choice.isdigit():
        idx = int(choice)
        if 1 <= idx <= len(recent):
            selected_entry = recent[-idx][1]
            pyperclip.copy(selected_entry)
            print("Copied to clipboard.")
            input("Press Enter to exit...")
            return
        elif idx == delete_option_index:
            delete_history_file()
        else:
            print("Invalid choice.")
    else:
        print("Invalid input.")

    input("Press Enter to exit...")

if __name__ == "__main__":
    print("If you see this when the PC starts up, it's indicating that the program works normally :D")
    print()
    history = load_history()
    show_history_menu(history)
