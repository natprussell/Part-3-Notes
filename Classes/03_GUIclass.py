from tkinter import *
from tkinter import ttk
root= Tk()

class GreetingApp:
    def __init__ (self, master):
        self.label1= ttk.Label(master)
        self.label1.config(text="Hello")
        self.label1.grid()

        self.btn1= ttk.Button(master)
        self.btn1.config(text= "Press here")
        self.btn1.config(command= self.GoodbyeMethod)
        self.btn1.grid()
        
    def GoodbyeMethod(self):
        return self.label1.config(text="Goodbye")


app= GreetingApp(root)

root.mainloop()