from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()

vertical = Scale(root, from_=0, to=200)
vertical.pack()


def open():
	global my_img
	top = Toplevel()
	top.title("Enter Shrimp data")
	my_img = ImageTk.PhotoImage(Image.open("shrimpart"))
	my_label = Label(top, image=my_img).pack()


btn = Button(root, text="Enter Shrimp data", command=open).pack()

#database
conn = sqlite3.connect('first_attempt.db')
c = conn.cursor()

#tables

c.execute("""
	


	""")


conn.commit()
conn.close()


mainloop()