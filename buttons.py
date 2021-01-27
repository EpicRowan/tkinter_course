from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="grey")
e.pack()

def my_click():
	hello = "Hello " + e.get()
	my_label = Label(root, text = hello)
	my_label.pack()


#Note, dont put () after command function
firstbutton = Button(root, text = "Enter name", padx = 50, pady = 50, command = my_click)
firstbutton.pack()

root.mainloop()