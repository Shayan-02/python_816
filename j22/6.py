from tkinter import *


def new_tab():
    window = Tk()
    window.mainloop()


root = Tk()
btn1 = Button(root, text="New Tab", command=lambda: new_tab())
btn1.pack()
root.mainloop()