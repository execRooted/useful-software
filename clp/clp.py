import pyperclip
import json
import os
import re

os.system("title CLP Manager - by execRooted")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(SCRIPT_DIR, "clipboard_history.json")
MARKER_FILE = os.path.join(SCRIPT_DIR, "cleared.marker")


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def clear_history_contents():
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump([], f)

    # Clear clipboard
    pyperclip.copy("")

    # Create marker file
    with open(MARKER_FILE, 'w') as marker:
        marker.write("cleared")

    print("\n✅ Clipboard history and clipboard content cleared.")
    input("Press Enter to exit...")
    exit()


def show_history_menu(history):
    if not history:
        print("Clipboard history is empty.")
        input("Press Enter to exit...")
        return

    print("\n--- Clipboard History ---\n")
    for i, (timestamp, entry) in enumerate(reversed(history), 1):
        display = re.sub(r'\s+', ' ', entry).strip()[:70]
        print(f"{i}. [{timestamp}] {display}{'...' if len(entry) > 70 else ''}")

    delete_option_index = len(history) + 1
    print(f"{delete_option_index}. Clear clipboard history")

    print("\nSelect an entry to copy to clipboard.")
    choice = input(f"Choice (1–{delete_option_index} or Enter to cancel): ").strip()

    if choice == "":
        print("No selection made. Exiting.")
        return

    if choice.isdigit():
        idx = int(choice)
        if 1 <= idx <= len(history):
            selected_entry = history[-idx][1]
            pyperclip.copy(selected_entry)
            print("Copied to clipboard.")
            input("Press Enter to exit...")
            return
        elif idx == delete_option_index:
            clear_history_contents()
        else:
            print("Invalid choice.")
    else:
        print("Invalid input.")

    input("Press Enter to exit...")


if __name__ == "__main__":
    history = load_history()
    show_history_menu(history)
