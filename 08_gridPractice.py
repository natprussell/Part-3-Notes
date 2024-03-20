from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('300x300')
#configure size of window so it doesnt shrink down

btn1= ttk.Button(root, text="0,0")
btn1.grid(row=0, column=0)

btn2=ttk.Button(root, text='0,1')
btn2.grid(row=0, column=1)

btn3= ttk.Button(root, text='0,100')
btn3.grid(row=0, column=100)

root.mainloop()