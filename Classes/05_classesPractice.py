from tkinter import *
from tkinter import ttk
root= Tk()

class Surprise:
    def __init__ (self,master):
      self.label= ttk.Label(master,text=" ")
      self.label.grid()
      self.btn= ttk.Button(master, text="Press for Surprise!", command= self.method1)
      self.btn.grid()
    def method1(self):
      self.label.config(text= "Surprise!")

app= Surprise(root)
root.mainloop()
