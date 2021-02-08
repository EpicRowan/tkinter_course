from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Insert images")

r = IntVar()


Radiobutton(root, text="Option 1", variable=r, value=1).pack()
Radiobutton(root, text="Option 2", variable=r, value=2).pack()
Radiobutton(root, text="Option 3", variable=r, value=3).pack()

myLabel = myLabel


root.mainloop()