# create label frame

from tkinter import *
from tkinter import ttk

class LFPractice:
    def __init__(self,master):
        self.lf1 = ttk.LabelFrame(master,text="Cool Buttons",height=100,width=200)
        self.lf1.pack()
        self.btn1 = ttk.Button(self.lf1,text="Button 1")
        self.btn1.grid()
        self.btn2 = ttk.Button(self.lf1,text="Button 2")
        self.btn2.grid()
        
root = Tk()
app = LFPractice(root)
root.mainloop()
