from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Insert images")


# my_img = ImageTk.PhotoImage(Image.open("shrimpart"))
# my_label = Label(image=my_img)
# my_label.pack()

frame = LabelFrame(root, text="A frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)

button_quit = Button(frame,text="Close",bg="purple", command=root.quit)
button_quit.pack()


root.mainloop()