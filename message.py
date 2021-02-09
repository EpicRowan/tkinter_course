from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()

def popup():
	messagebox.showinfo("This is the popup", "Hello world")

Button(root, text="Popup", command=popup).pack()

mainloop()