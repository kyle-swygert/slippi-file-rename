
import os
from sys import platform

from renameGames import rename_files_in_folder

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QIcon
from threading import Thread

class SlippiRenameApp(QApplication):

    def __init__(self):
        super().__init__([])

        # adding a layout and window to add all the widgets to
        self.layout = QVBoxLayout()
        self.window = QWidget()

        self.setWindowIcon(QtGui.QIcon('slippi-logo.png'))

        # adding a prompt to direct the user what to do
        self.prompt_label = QLabel("Enter a Directory that you would like to Rename: ")
        self.layout.addWidget(self.prompt_label)

        # adding a textBox that the user will type in or will fill with the selected directory. 
        self.dir_textbox = QLineEdit("Enter a Directory to Rename:")
        self.layout.addWidget(self.dir_textbox)

        # adding button to browse for a file
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.select_directory)
        self.layout.addWidget(self.browse_button)

        # adding button to rename the desired directory
        self.rename_button = QPushButton("Rename Files")
        self.rename_button.clicked.connect(self.rename_button_clicked)
        self.layout.addWidget(self.rename_button)
        
        # setting window constraints
        self.window.setWindowTitle("Slippi File Rename")
        self.window.setLayout(self.layout)
        self.window.setFixedSize(500, 300)
        self.window.show()

        # starting the GUI app itself
        self.exec_()


    def select_directory(self):
        print('selecting a directory to rename')

        # open the directory selector at the Desktop directory of the computer
        #tempDir = str(QFileDialog.getExistingDirectory(None, "select a dir", os.path.join(os.environ['USERPROFILE'], 'Desktop')))

        tempDir = ''


        # open the dir selector to the Desktop directory with a custom prompt on the top of the window. 
        # NOTE: The code below works with Windows. Test that it works with Linux. DOES NOT work on MacOS!!!!


        # TODO: test that the top if statement would work with linux!!!!
        if platform == 'win32':
            tempDir = str(QFileDialog.getExistingDirectory(None, "Select a Directory to rename Slippi Files", os.path.join(os.environ['USERPROFILE'], 'Desktop')))
        elif platform == 'darwin' or platform == 'linux':
            tempDir = str(QFileDialog.getExistingDirectory(None, "Select a Directory to rename Slippi Files", os.path.join(os.path.expanduser('~') , 'Desktop')))


        if tempDir == '':
            self.dir_textbox.clear()
            self.dir_textbox.setText('Enter a Directory to Rename:')
        else:
            print(f"selected dir: {tempDir}, do stuff with the dir now...")
            # delete the string that is in the dir_textbox
            self.dir_textbox.clear()
            # set the selected dir as the string inside the self.dir_textbox object. 
            self.dir_textbox.setText(tempDir)

        
    def rename_button_clicked(self):
        print(f"the rename button was clicked")
        print(f'directory to rename: {self.dir_textbox.text()}')
        # rename the selected directory based on the text that is in the dir_textbox object

        rename_thread = Thread(target=rename_files_in_folder, args=(self.dir_textbox.text(),), daemon=True)

        rename_thread.start()

        # set the dir_textbox tet to a default value
        self.dir_textbox.setText('Enter a Directory to Rename:')

app = SlippiRenameApp()