from tkinter import *
from PIL import ImageTk,Image

root = Tk()

def open():
	global my_img
	top = Toplevel()
	top.title("Enter Shrimp data")
	my_img = ImageTk.PhotoImage(Image.open("shrimpart"))
	my_label = Label(top, image=my_img).pack()


btn = Button(root, text="Enter Shrimp data", command=open).pack()

mainloop()