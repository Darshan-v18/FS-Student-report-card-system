from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Student report card system')
def Login():
        text=click.get()
        if (text=="User"):
            messagebox.showerror(title="",message="Select a user!")
        elif (text=="Admin"):
            root.destroy()
            import adminLogin
        elif (text=="Teacher"):
            root.destroy()
            import teacherLogin
        else:
            root.destroy()
            import studentMain
root.geometry("644x344")
root.resizable(width=False,height=False);
Label(root, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
options = ["Admin","Teacher","Student"]

click = StringVar()
click.set("User")
drop = OptionMenu(root,click,*options)
drop.config(width=15)
drop.place(x=240,y=100)
Button(text="Submit",command=Login).place(x=275,y=200)
root.mainloop();