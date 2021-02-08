from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Insert images")


frame = LabelFrame(root, text="A frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)

my_img = ImageTk.PhotoImage(Image.open("shrimpart"))
my_label = Label(frame,image=my_img)
my_label.pack()

# button_quit = Button(frame,text="Close",bg="purple", command=root.quit)
# button_quit.pack()


root.mainloop()