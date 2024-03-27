from tkinter import *
from tkinter import ttk
root= Tk()

class PracticeClass:
    def __init__(self,master):
        self.eb1 = ttk.Entry(master)
        self.eb1.grid()
        self.submitbutton = ttk.Button(master, text="Submit!",command = self.printinfo)
        self.submitbutton.grid()
    def printinfo(self):
        print(self.eb1.get())

app= PracticeClass(root)
root.mainloop()