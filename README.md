# useful-software

*A collection of useful software I created or found handy for day-to-day tasks. Tested on Windows.*

---

## clear.bat (created by me)

- A lightweight batch script that empties your Recycle Bin and unused temp files, waits a moment, then shuts down your PC.
- Useful for cleaning up when shutting down your computer.

---

## clp (created by me)

- A lightweight clipboard manager that monitors your clipboard and saves entries into a JSON file named `clipboard_history.json`.

- To install the program, download the .zip file, then put the clp folder somewhere in your computer. Then create a shortcut for clp_mon.pyw and place it into the startup folder.<br>
  *If you dont know how to get to the startup folder, visit the ***Help*** section down below*

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
  
- Dont forget to install the requirements (see below).

---
## ctrl_apps (created by me)

The **ctrl_apps** program is a collection of useful tools that give you easy access to important system and network metrics, alongside functionality for quickly shutting down, restarting, or refreshing your system and network. It displays real-time system stats and offers one-click options for managing your PC.

### Features

- **System Info:** View current system time, date, uptime, memory usage, disk usage, battery status, and more.
- **System Monitoring:** Real-time monitoring of CPU, memory, disk usage, and boot time.
- **Network Monitoring:** Monitor your network activity, including IP address and real-time upload/download usage or speeds<br>(not a speedtest, just monitoring how fast a file is downlaoding).

### Actions:
- **Shutdown & Clear Bin:** Shutdown your PC and clean the Recycle Bin (available in ctrl_appC version).
- **Restart:** Restart your system with one click.
- **Network Reset:** Refresh your network settings (useful for fixing network issues).

There are two versions of this tool:

- **ctrl_app:** Only offers the shutdown functionality.
- **ctrl_appC:** Includes both the shutdown functionality and an option to clear the Recycle Bin when shutting down.

### Installation

### 1. Download the Program:
After downloading, you'll find two folders: `ctrl_app` and `ctrl_appC`.

- **ctrl_app:** Contains the basic version with shutdown functionality.
- **ctrl_appC:** Contains the advanced version with both shutdown and Recycle Bin cleanup.

### 2. Choose Your Version:
Select the folder based on the functionality you need, and place it somewhere on your computer that is not encrypted by BitLocker (to ensure it can run at startup).

### 3. Install Dependencies:
Inside the folder, you.ll find a `requirements.txt` file. Install the requirements.txt file<br>(If you dont know how, visit the ***Help*** section down below.)


### 4. Set Up Auto-Start:

- Create a shortcut for the corresponding trigger file:
  - For **ctrl_app**, use `trigger.pyw`.
  
  - For **ctrl_appC**, use `triggerC.pyw`.

- Move the shortcut to your **Startup** folder so the program runs automatically after boot. <br>(If you dont know how to get to the startup folder, visit the ***Help*** section down below.)



### 5. Restart Your Computer:
After restarting, the program will automatically run in the background.

### Use the Program:

- To open the control panel interface, press `Ctrl + Alt + P`.
- To quit the program, make sure that the window is in focus (click on it) and press Q.
- From there, you can interact with the buttons for system information, shutdown, restart, and network reset.





***For troubleshooting, change the extension of the .pyw to .py, so you can see the console.***


---

# Help:

## How to convert a `.py` file into an `.exe` with PyInstaller

1. Make sure Python and pip are installed.
2. Open Command Prompt as Administrator and run:

        pip install PyInstaller

3. To create an executable with an icon <br>(icon file should be in the same folder as the Python script, and if you want to omit the icon, simply remove the --icon=theIcon.ico flag):

        python -m PyInstaller --onefile --icon=theIcon.ico pythonFile.py

4. Your `.exe` will be inside the `dist` folder.

*Note:* I included my profile picture as `theIcon.ico` in the main branch for you to use.

---
## How to get to the startup folder:

Press windows + R to open the run dialog → type this command in: `shell:startup`

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
