from tkinter import *
from tkinter import ttk

root= Tk()

sampleLabel= ttk.Label(root, text= 'Sample Text1')
sampleLabel.pack(side=RIGHT)

sampleLabel2= ttk.Label(root, text= 'Sample Text2')
sampleLabel2.pack(side=LEFT)

sampleLabel3= ttk.Label(root, text= 'Sample Text3')
sampleLabel3.pack(side=BOTTOM)

sampleLabel4= ttk.Label(root, text= 'Sample Text4')
sampleLabel4.pack(side=TOP)

root.mainloop()