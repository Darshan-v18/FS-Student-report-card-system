from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Student report card system')
def validate():
    a = unameentry.get()
    b = passentry.get()
    if (a != "Admin" and b!="1234") :
        messagebox.showerror(title="Login Error",message="Invalid Username / password")
    else:
        unameentry.delete(0,END)
        passentry.delete(0,END)
        root.destroy()
        import adminMain
root.geometry("650x350")
root.resizable(width=False,height=False);
Label(root, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
Label(root,text="Admin Login", font="comicsansms 10 bold", pady=5,fg="RoyalBlue2").place(x=250,y=50)
username = Label(root, text="Username")
password = Label(root, text="Password")
username.place(x=200,y=100)
password.place(x=200,y=150)
unamevalue = StringVar()
passvalue = StringVar()
unameentry = Entry(root, textvariable=unamevalue)
passentry = Entry(root, textvariable=passvalue,show="*")
unameentry.place(x=260,y=100)
passentry.place(x=260,y=150)
Button(text="Submit",command=validate).place(x=270,y=200)
root.mainloop();