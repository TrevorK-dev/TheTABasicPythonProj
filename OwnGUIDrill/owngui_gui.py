from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Be sure to import our other modules 
# so we can have access to them
import owngui_main


def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
        I prefer to use grid as it offers the best control
        for pacing the widgets, but is a little confusing at
        first, but that is what this demo is here for...
    """

    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=0,column=2,rowspan=1,columnspan=2,padx=(25,40),pady=(30,20),sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=1,column=2,rowspan=1,columnspan=2,padx=(25,40),pady=(30,20),sticky=N+E+W)


    #Define the listbox with a scrollbar and grid them
  #  self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
  #  self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
  #  self.lstList1.bind('<<ListboxSelect>>',lambda event: drill50_phonebook_func.onSelect(self,event))
  #  self.scrollbar1.config(command=self.lstList1.yview)
   # self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
  #  self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)
    
    self.btn_browse = tk.Button(self.master,width=12,height=2,text='Browse')
    self.btn_browse.grid(row=0,column=0,padx=(20,0),pady=(20,10),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=2,text='Browse')
    self.btn_browse2.grid(row=1,column=0,padx=(20,0),pady=(20,10),sticky=W)
    self.btn_browse3 = tk.Button(self.master,width=12,height=2,text='Check For Files')
    self.btn_browse3.grid(row=2,column=0,padx=(20,0),pady=(20,10),sticky=W)
    self.btn_browse4 = tk.Button(self.master,width=12,height=2,text='Close Program')
    self.btn_browse4.grid(row=2,column=3,padx=(20,0),pady=(20,10),sticky=W)


   #  owngui_func.create_db(self)
    # owngui_func.onRefresh(self)

    



if __name__ == "__main__":
    pass
