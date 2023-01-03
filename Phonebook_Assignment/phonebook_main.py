# Python ver. 3.11.1
#
# Author: Leonardo S. Salazar
#
# Purpose: Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#          Using Tkinter partent and class relattionships.
#
# Tested OS: This code was was wtritten and tested  to work on windows 11.

from tkinter import *
import tkinter as tk

# Be sure tto import our otther modules
# so we can have access to them
import phonebook_gui
import phonebook_func

#Frame is the tkinter frame class that our own class will inhrit from
class ParentWindow(Frame):
    def  __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master  = master
        self.master.minsize(500,300) # (Height, Widtth)
        self.master.maxsize(500,300)

        # This CenttterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("the Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")

        # This protocol method is a tkintter built-in method to catch if
        # The user clicks the upper corner, "X" on windows OS.
        self.master.protocol("WM_DELETE_WINDOW",lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Load in the GUI widgets from a separate module.
        # Keeping your code compartmentalized and cluttter free
        phonebook_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
