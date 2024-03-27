from tkinter import *
from tkinter import ttk
root= Tk()

class Surprise:
    def __init__ (self,master):
      self.label= ttk.Label(master,text=" ")
      self.label.grid()
      self.btn= ttk.Button(master, text="Press for Surprise!", command= self.method1)
      self.btn.grid()
      self.btn2= ttk.Button(master, text= "Delete", command= self.method2)
      self.btn2.grid()
    def method1(self):
      self.label.config(text= "Surprise!")
    def method2(self):
       self.label.config(text= " ")

app= Surprise(root)
root.mainloop()
