from tkinter import *

root = Tk()

firstLabel = Label(root, text="Hello World!")
secondLabel = Label(root, text="I like puppies!")

# firstLabel.pack()

firstLabel.grid()
secondLabel.grid()


root.mainloop()