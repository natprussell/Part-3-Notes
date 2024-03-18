from tkinter import *
from tkinter import ttk

root= Tk()

btn1=ttk.Button(root)
btn1.config(text= "Click here!")
# can be used to add text or context to button
btn1.grid(row=0, column=0)
# can use .grid  or .place  or .pack 

btn2=ttk.Button(root, text= "This is button 2")
btn2.grid(row=1, column=2)
# by adding ttk.button it creates a themed button 


root.mainloop() 


