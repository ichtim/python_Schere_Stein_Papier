from zug import Zug
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk
import time
class my_window:
	def __init__(self,master):
		self.master=master
		self.frame=tk.Frame(self.master)
		self.button=[tk.Button(self.frame,text=Zug.Züge[i][0],image=ImageTk.PhotoImage(Zug.Züge[i][1].resize((40,40),Image.LANCZOS)),command=self.play(self.frame,Zug.val(i)),compound=TOP)for i in Zug.Züge.keys()]
#		self.button1=tk.Button(self.frame,text=Zug.Züge[0][0],image=tk.PhotoImage(file=Zug.Züge[0][1]),command=self.play(Zug.val(0)))
		for i,j in zip(self.button,range(4)):
			i.pack(ipadx=40,ipady=60)
		self.frame.pack()
	def play(self,master,z):
		z2=Zug.zufallszug()
		s=Zug.val.sieger(z,z2)
		w=Toplevel(master)
		l=Label(master,image=ImageTk.PhotoImage(Zug.Züge[z2.value][1].resize((40,40),Image.LANCZOS)))
		l.image=ImageTk.PhotoImage(Zug.Züge[z2.value][1].resize((40,40),Image.LANCZOS))
		l.pack()
		time.sleep(3)
		w.destroy()
if __name__=='__main__':
	root=tk.Tk()
	app=my_window(root)
	root.mainloop()
