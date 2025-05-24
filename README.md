# useful-software

*A collection of useful software I created or found handy for day-to-day tasks. Tested on Windows.*

---

## clearBinOnShutdown.bat (created by me)

- A lightweight batch script that empties your Recycle Bin, waits a moment, then shuts down your PC.
- Useful for cleaning up when shutting down your computer.

---

## clp (created by me)

- A lightweight clipboard manager that monitors your clipboard and saves entries into a JSON file named `clipboard_history.json`.

- To install the program, download the .zip file, then put the clp folder somewhere in your computer. Then create a shortcut for clp_mon.pyw and place it into the startup folder. <br>
  *Quick tip:* Press windows + R to open the *run dialog* → type this command in: shell:startup → Copy the two files there. 

- To start monitoring, restart your PC
  
- Press **Ctrl + Alt + H** to open the clipboard history.
  
- To delete the clipboard history file (`clipboard_history.json`), choose the last option in `clp.py`, AKA the menu that shows up when you click **Ctrl + Alt + H**.
  
- Useful for quick access to your clipboard history.
  
- **Note:** I do not recommend converting these scripts to executables as some systems may not read the JSON file correctly.
  
- The `.pyw` extension hides the console window for the monitoring script. For debugging, rename it to `.py` to see output messages in the console.
  
- The JSON file is created automatically when you run `clp_mon.pyw` for the first time.
  
- To stop the monitor, either restart your PC or use Task Manager to kill the process.
  *If it's in startup, it will restart automatically after login, so remove it from Startup if you want to stop it permanently.*
 
- To uninstall, delete `clp.py`, `clp_mon.pyw`, and `clipboard_history.json` from your computer, after remove the shortcut from your startup folder, then restart your PC.
  
- Don’t forget to install the requirements (see below).

---

## How to convert a `.py` file into an `.exe` with PyInstaller

1. Make sure Python and pip are installed.
2. Open Command Prompt as Administrator and run:

        pip install PyInstaller

3. To create an executable with an icon (icon file should be in the same folder as the Python script):

        python -m PyInstaller --onefile --icon=theIcon.ico pythonFile.py

4. Your `.exe` will be inside the `dist` folder.

*Note:* I included my profile picture as `theIcon.ico` in the main branch for you to use.

---

## How to install the requirements

1. Make sure Python and pip are installed.
2. Open Command Prompt as Administrator and run:

        pip install -r requirements.txt

*If some Python folders don’t have a `requirements.txt`, it means those libraries come pre-installed and no action is needed.*

---

I will occasionally update this repository when I create or find new useful tools.

---

**Made by execRooted**
