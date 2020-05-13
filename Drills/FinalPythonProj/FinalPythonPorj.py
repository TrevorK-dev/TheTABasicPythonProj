import shutil
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os, sys




def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
        I prefer to use grid as it offers the best control
        for pacing the widgets, but is a little confusing at
        first, but that is what this demo is here for...
    """

    self.txt_filedir = tk.Entry(self.master,text='')
    self.txt_filedir.grid(row=0,column=2,rowspan=1,columnspan=2,padx=(25,40),pady=(30,20),sticky=N+E+W)
    self.txt_filedir2 = tk.Entry(self.master,text='')
    self.txt_filedir2.grid(row=1,column=2,rowspan=1,columnspan=2,padx=(25,40),pady=(30,20),sticky=N+E+W)

    self.btn_browse = tk.Button(self.master,width=12,height=2,text='Source', command=lambda: cur_directory(self))
    self.btn_browse.grid(row=0,column=0,padx=(20,0),pady=(20,10),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=2,text='Destination', command=lambda: cur_directory2(self))
    self.btn_browse2.grid(row=1,column=0,padx=(20,0),pady=(20,10),sticky=W)
    self.btn_browse3 = tk.Button(self.master,width=12,height=2,text='Move Files', command=lambda: fmove(self))
    self.btn_browse3.grid(row=2,column=0,padx=(20,0),pady=(20,10),sticky=W)
    self.btn_browse4 = tk.Button(self.master,width=12,height=2,text='Close Program', command = root.destroy)
    self.btn_browse4.grid(row=2,column=3,padx=(20,0),pady=(20,10),sticky=W)



def cur_directory(self):
    self.current_directory = filedialog.askdirectory()
    self.txt_filedir.insert(0,self.current_directory)

def cur_directory2(self):
    self.current_directory2 = filedialog.askdirectory()
    self.txt_filedir2.insert(0, self.current_directory2)

def fmove(self):
    dirs = os.listdir(self.current_directory)
    print(dirs)
    for x in dirs:
        if x.endswith(".txt"):
            abspath = os.path.join(self.current_directory, x)
            gmtime = os.path.getmtime(abspath)
            print(x, gmtime)
            shutil.move(abspath, self.current_directory2)
    


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        # owngui_func.center_window(self,500,150)
        self.master.title("My Own GUI2")
        self.master.configure(bg="#F1F1F1")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        # self.master.protocol("WM_DELETE_WINDOW", lambda: owngui_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        load_gui(self)






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    pass

