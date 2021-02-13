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

# c.execute("""CREATE TABLE addresses (
# 	first_name text,
# 	last_name text,
# 	zipcode integer
# )
# 	""")

f_name = Entry(root, width=30)
f_name.grid(row=0, column=0, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=0, column=0, padx=20)

address = Entry(root, width=30)
address.grid(row=0, column=0, padx=20)

conn.commit()
conn.close()


mainloop()