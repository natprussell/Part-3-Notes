from tkinter import *
from tkinter import ttk

root= Tk()

btn1=ttk.Button(root, text= "This is button 1").grid()
# can use .grid  or .place  or .pack 
btn2=ttk.Button(root, text= "This is button 2").pack()
# by adding ttk.button it creates a themed button 


root.mainloop()


