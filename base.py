from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()

# vertical = Scale(root, from_=0, to=200)
# vertical.pack()


# def open():
# 	global my_img
# 	top = Toplevel()
# 	top.title("Enter Shrimp data")
# 	my_img = ImageTk.PhotoImage(Image.open("shrimpart"))
# 	my_label = Label(top, image=my_img).pack()


# btn = Button(root, text="Enter Shrimp data", command=open).pack()

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


def submit():
	f_name.delete(0,END)
	l_name.delete(0,END)
	address.delete(0,END)
	conn = sqlite3.connect('first_attempt.db')
	c = conn.cursor()
	c.execute("INSERT INTO first_attempt VALUES (:f_name, :l_name, :address)")
	conn.commit()
	conn.close()


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

submit_btn = Button(root, text="Add record", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2)

conn.commit()
conn.close()


mainloop()