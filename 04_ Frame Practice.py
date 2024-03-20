from tkinter import *
from tkinter import ttk

root= Tk()

frame1= Frame(root, relief=SOLID, padx=10, pady=10)
frame1.grid

btn1= ttk.Button(frame1, text= "Click here!")
btn1.grid()

btn2=ttk.Button(frame1, text= "Button 2")
btn2.grid()


root.mainloop()