terminal-rename:
	python3.6 renameGames.py

gui-rename:
	python3.6 renameGUI.py

# remove all files from the slp dir, copy all the dirs and files from original-replays dir into the slpl dir. Files shoud be ready again for another rename test. 
clean-files: