from tkinter import *

root = Tk()

def my_click():
	my_label = Label(root, text = "You clicked me!")
	my_label.pack()


firstbutton = Button(root, text = "Click me!", padx = 50, pady = 50, command = my_click)
firstbutton.pack()

root.mainloop()