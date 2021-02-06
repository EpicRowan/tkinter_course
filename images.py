from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Insert images")


my_img = ImageTk.PhotoImage(Image.open("shrimpart"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root,text="Close",bg="purple", command=root.quit)
button_quit.pack()

button_test1 = Button(root,text="Test1", bg="grey", command=root.quit)
button_test1.pack()

button_test2 = Button(root,text="Test2", bg="white", command=root.quit)
button_test2.pack()

root.mainloop()