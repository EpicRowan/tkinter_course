from tkinter import *

root = Tk()

firstLabel = Label(root, text="Hello World!")
secondLabel = Label(root, text="I like puppies!")

# firstLabel.pack()

firstLabel.grid(row=0, column=0)
secondLabel.grid(row=1, column=0)


root.mainloop()