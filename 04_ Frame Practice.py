from tkinter import *
from tkinter import ttk

root= Tk()

frame1= ttk.Frame(root, relief=SOLID, padding=(12,35))
frame1.grid()

btn1= ttk.Button(frame1, text= "Click here!")
btn1.grid()

btn2= ttk.Button(frame1, text= "Button 2")
btn2.grid()

frame2= ttk.Frame(root, relief=SOLID, padding=(12,35))
frame2.grid()

btn3= ttk.Button(frame2, text= "Button 3")
btn3.grid()

btn4= ttk.Button(frame2, text= "Button 4")
btn4.grid()


root.mainloop()