build-wsl-release:
	# command to build the release as a package. 
	pyinstaller.exe --noconsole rename-gui-qt.py --onefile --name Slippi-File-Rename

build-linux-release:
	pyinstaller --noconsole rename-gui-qt.py --onefile --name Slippi-File-Rename