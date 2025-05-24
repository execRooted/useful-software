@echo off

PowerShell.exe -NoProfile -Command "Clear-RecycleBin "

echo Recycle Bin Cleared :)


echo Deleating Temporary Files...


del /q /f /s C:\Windows\Temp\*
del /q /f /s C:\Windows\TEMP\*


echo Temporary Files Deleted :)

echo Shutting down in 3 seconds...

timeout 3

shutdown -s -f -t 0


pause

