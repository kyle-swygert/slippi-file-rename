# Slippi File Renaming Tool
[Project Slippi](https://slippi.gg) Tool to rename files for easier readability

Written using:
- Python 3.7+
- [py-slippi](https://github.com/hohav/py-slippi) 1.3.1
- [PyQt5](https://pypi.org/project/PyQt5/) 5.13.2

To Use the tool:
1. Download the latest release
2. Execute the program
3. Click on the "Browse" button and select the directory you would like to rename

The tool will rename the files as long as the program window is open. If the renaming process is stopped in the middle, not all the files will be renamed afterward. 

Currently the program will rename files as per the specification below:

```CharacterName(TAG)-Vs-CharacterName(TAG)<year-month-day-hour-minute-second>.slp```

Example: ```CaptainFalcon(DOOM)-Vs-Jigglypuff<20191010191914>.slp```

The tool will also rename files to show if it is a singles match, teams match with the team color, or a free for all match. 

I hope you enjoy this tool and find it useful. 
