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
    self.btn_browse3 = tk.Button(self.master,width=12,height=2,text='Move Files')
    self.btn_browse3.grid(row=2,column=0,padx=(20,0),pady=(20,10),sticky=W)
    self.btn_browse4 = tk.Button(self.master,width=12,height=2,text='Close Program', command = root.destroy)
    self.btn_browse4.grid(row=2,column=3,padx=(20,0),pady=(20,10),sticky=W)

    mainloop()
    
  #  Define the listbox with a scrollbar and grid them
  #  self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
  #  self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
  #  self.lstList1.bind('<<ListboxSelect>>',lambda event: drill50_phonebook_func.onSelect(self,event))
  #  self.scrollbar1.config(command=self.lstList1.yview)
  #  self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
  #  self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

  #  owngui_func.create_db(self)
  #  owngui_func.onRefresh(self)


root = Tk()
root.withdraw()

def cur_directory(self):
    current_directory = filedialog.askdirectory()
    self.txt_filedir.insert(0,current_directory)

def cur_directory2(self):
    current_directory2 = filedialog.askdirectory()
    self.txt_filedir2.insert(0, current_directory2)


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
        
        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
       #  filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: owngui_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        """
            Finally, we apply the config method of the widget to display the menu
            From here we could also pass in additional aprams for additional 
            functionalityor appearances such as a borderwidth.
        """
        self.master.config(menu=menubar, borderwidth='1')





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    pass

