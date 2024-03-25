from tkinter import *
from tkinter import ttk

root = Tk()

framePack= ttk.LabelFrame(root)
framePack.grid(row=0, column=0)
framePack.config(padding=(50,30))
framePack.config(text= '.pack')


frameGrid= ttk.LabelFrame(root)
frameGrid.grid(row=0, column=1)
frameGrid.config(padding=(50,30))
frameGrid.config(text= '.grid')

framePlace= ttk.LabelFrame(root)
framePlace.grid(row=1, column=0)
framePlace.config(padding=(50,30))
framePlace.config(text= '.place')

btn1=ttk.Button(framePack, text="Left Side").pack()


root.mainloop()       