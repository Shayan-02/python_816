from tkinter import *


def showFullName():
    fullName = fname_ent.get() + " " + lname_ent.get()
    fullName_lbl.config(text=f"اسم کامل شما {fullName} است.")

root = Tk()
root.title("fullname app")
root.geometry("450x500")
root.resizable(False, False)
root.configure(bg="black")

fname_lbl = Label(root, text="نام", fg="white", bg="black", font=("vazir", 20))
fname_lbl.place(x=325, y=20)

fname_ent = Entry(root, font=("vazir", 15), width=20)
fname_ent.place(x=30, y=30)

lname_lbl = Label(root, text="نام خانوادگی", fg="white", bg="black", font=("vazir", 20))
lname_lbl.place(x=275, y=80)

lname_ent = Entry(root, font=("vazir", 15), width=20)
lname_ent.place(x=30, y=90)

fullName_btn = Button(root, text="نام کامل", fg="white", bg="#21AA58", width=10, font=("vazir", 20, 'bold'), command=lambda: showFullName())
fullName_btn.place(x=150, y=140)

fullName_lbl = Label(root, text="", fg="white", bg="black", font=("vazir", 20))
fullName_lbl.place(x=30, y=140)

root.mainloop()