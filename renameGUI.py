




from renameGames import rename_files_in_folder
import tkinter as tk
from tkinter import *
import tkinter.tix as tix


class Application(tk.Tk):

    def __init__(self):

        # TODO: format the widgets better and add a label to the application.
        super().__init__(className="SLIPPI RENAME TOOL")
        self.minsize(800, 300)
        self.maxsize(800, 300)


        self.execute_button = tk.Button(self)
        self.execute_button["text"] = "Rename Files"
        self.execute_button["command"] = self.button_clicked
        self.execute_button.pack(side="right")

        self.browse_button = tk.Button(self)
        self.browse_button["text"] = "Browse"
        self.browse_button["command"] = self.select_directory
        self.browse_button.pack(side="right")

        self.dir_textbox = tk.Entry(self, width=200)
        self.dir_textbox.pack(side="left")
        self.dir_textbox.delete(0)
        self.dir_textbox.insert(0, "Enter a Directory to rename:")

    def select_directory(self):
        # select the directory. if a directory is selected, fill in the text box with the path string.
        # if the selection is cancelled, fill the text box with the default string. 

        # why the fuck is the directory selection dialog not working properly............

        dir_picker = tix.DirSelectDialog(master=self, command=self.print_dir)

        dir_picker.popup()

    def print_dir(self, args):
        print(f"selected dir: {args}")


    def button_clicked(self):

        s = self.dir_textbox.get()

        if s != '' and s != "Enter a Directory to rename:":

            rename_files_in_folder(self.dir_textbox.get())
        else:

            rename_files_in_folder("./slp")

    


# add a text area to enter the directory that is to be renamed

# add a button that starts the function execution with the directory name in the text area

# when the button is pressed, disable the main window and popup a "loading" window that runs while the program is running. 

app = Application()

app.mainloop()


'''

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

'''