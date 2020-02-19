# Slippi File Renaming Tool
[Project Slippi](https://slippi.gg) Tool to rename files for easier readability

Written using:
- Python 3.7+
- [py-slippi](https://github.com/hohav/py-slippi) 1.3.1+
- [PyQt5](https://pypi.org/project/PyQt5/) 5.13.2+

To Build the tool yourself:
- Install PyInstaller
- Install Make 
- Execute the ```make build-release``` command on the terminal
    - NOTE: you might have to change the makefile command from ```pyinstaller.exe``` to ```pyinstaller``` since I am building using WSL. 
- The executable will be located in the ```dist``` directory that is in the same directory as the python scripts

To Use the tool:
1. Download the latest release
2. Execute the program
3. Click on the "Browse" button and select the directory you would like to rename

The tool will rename the files as long as the program window is open. If the renaming process is stopped in the middle, not all the files will be renamed afterward. 

Currently the program will rename files as per the specification below:
- Singles:
    - Format:  ```CharacterName(TAG)-Vs-CharacterName(TAG)<year-month-day-hour-minute-second>.slp```
    - Example: ```CaptainFalcon(DOOM)-Vs-Jigglypuff_20191010191914.slp```
- Doubles (includes team color used, tested to work with 2v2, 3v1, and 2v1): 
    - Format:  ```TeamCOLOR(Char-Char)-Vs-TeamCOLOR(Char-Char)_20191026205534.slp```
    - Example: ```TeamGREEN(Fox-Samus)-Vs-TeamBLUE(Falco-Fox)_20191026163452.slp```
- Free-for-all (supports 3 and 4 player matches):
    - Format:  ```FFA_Char-Vs-Char-Vs-Char_20191026145622.slp```
    - Example: ```FFA_Ganondorf-Vs-Ganondorf-Vs-Ganondorf_20191026172311.slp```



The tool will also rename files to show if it is a singles match, teams match with the team color, or a free for all match. 

I hope you enjoy this tool and find it useful. 


![Slippi Logo](slippi-logo.png)