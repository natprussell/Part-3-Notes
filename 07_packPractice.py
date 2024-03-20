from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('300x300')
#configure size of window so it doesnt shrink down

btn1= ttk.Button(root, text="left side")
btn1.pack(side="left")

btn2=ttk.Button(root, text='Top side')
btn2.pack(side=TOP)

root.mainloop()