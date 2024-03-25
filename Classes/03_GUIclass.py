from tkinter import *
from tkinter import ttk
root= Tk()

class GreetingApp:
    def __init__ (self, master):
        self.label1= ttk.Label(master)
        self.label1.config(text="hello")
        self.label1.grid()

app= GreetingApp(root)

root.mainloop()