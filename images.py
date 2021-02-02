from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Insert images")

my_img = ImageTk.PhotoImage(Image.open("shrimpart"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root,text="Close",width=50, bg="pink", command=root.quit)
button_quit.pack()

root.mainloop()