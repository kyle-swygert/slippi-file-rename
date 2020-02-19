build-release:
	# command to build the release as a package. 
	pyinstaller.exe --noconsole rename-gui-qt.py --onefile --name Slippi-File-Rename