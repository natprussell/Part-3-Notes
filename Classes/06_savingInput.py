from tkinter import *
from tkinter import ttk
root= Tk()

class PracticeClass:
    def __init__(self,master):
        self.eb1 = ttk.Entry(master, show= "*") #hides text being entered
        self.eb1.grid()
        self.submitbutton = ttk.Button(master, text="Submit!",command = self.printinfo)
        self.submitbutton.grid()
    def printinfo(self):
        print(self.eb1.get())
        self.eb1.delete(0,'end') #deletes entry from console


app= PracticeClass(root)
root.mainloop()