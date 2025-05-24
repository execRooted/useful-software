# useful-software

 - A bunch of useful software that created and found useful in day-to-day activities, tested on windows:
------
## clearBinOnShutdown.bat

- A lightweight .bat program that deletes your files from the recicle bin, waits a bit, then shuts down your PC
- Useful when closing your PC

---

## clp

- A lightweight clipboard program, that monitors the clipboard, and saves it into a .json. To run it, press the clp_mon.pyw.
- To run it automaticly on every start of the pc, open the task manager, then go to the startup folder. Right-click on any .exe, then copy clp_mon.pyw and clp.py in there.
- When the clp_mon.pyw is running, to see your clipboard history, press ctrl + alt + H.
- To delete the .json and the history, press the last numbered option, when the cllp.py is running. 
- Useful for accesing the clipboard.
- I do not recommend to turn any of the files into executables. I found it that on some systems it does not read the .json correctly.
- There is no problem with a .json beeing in the startup folder. It will not open it at startup as a txt file, if you insall it as i said, so I do not want you to yap in the comments about this aspect.
- Install the requirements.txt
------

### How to turn a .py into a .exe with PyInstaller:
- Have python & pip installed
- Open cmd as adm and type:

  
		pip install PyInstaller

The icon flag isnt necesary. 

		python -m PyInstaller --onefile --icon=theIcon.ico pythonFile.py


Check inside the dist folder, there will be your .exe.

------

### How to install the requirements.txt:
  - Have python & pip installed
  - Open CMD as adm and type:

        pip install -r requirements.txt

*If there are python folders witought a requirements.txt file, that means that python comes preinstalled with the libraries, and you do not have to do anything.

**I Will ocasionally update this repository, when i find other useful stuff**

------

**Made by execRooted**
