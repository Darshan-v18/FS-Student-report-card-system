from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
root = Tk();
root.title('Student report card system')
def viewStudent():
    top = Toplevel(root)
    top.geometry("650x450")
    top.resizable(width=False,height=False);
    Label(top, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
    Label(top,text="Student Details", fg="RoyalBlue2",font="comicsansms 10 bold", pady=5).place(x=250,y=50)

    def disp():
        data = []
        with open("students.csv","r") as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        f.close()       
        global tree
        listheader = ['Name','USN','E-mail','Branch','Sem']

        tree = ttk.Treeview(top, selectmode="extended", columns=listheader, show="headings")

        vsb = ttk.Scrollbar(top, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(top, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        tree.place(x=120,y=190)
        # vsb.place(x=200,y=100)
        # hsb.place(x=200,y=100)

        #tree head
        tree.heading(0, text='USN', anchor=NW)
        tree.heading(1, text='Name', anchor=NW)
        tree.heading(2, text='Branch', anchor=NW)
        tree.heading(3,text="Sem",anchor=NW)
        tree.heading(4, text='E-mail',anchor=NW)
        

        # tree  columns
        tree.column(0, width=80, anchor='nw')
        tree.column(1, width=80, anchor='nw')
        tree.column(2, width=50, anchor='nw')
        tree.column(3, width=50, anchor='nw')
        tree.column(4, width=120, anchor='nw')
        
        for item in data:
            #print(item)
            if(item[0]==click.get()):
                tree.insert(parent='', index='end',values=item)
    count=0
    usn = []
    student = []
    with open('students.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            student.append(row)
            a=student[count][0]
            usn.append(a)
            count += 1
    click = StringVar()
    click.set("Select USN")
    drop = OptionMenu(top, click, *usn)
    drop.config(width=20)
    drop.place(x=210,y=100)
    Button(top,text="Submit",command=disp).place(x=260,y=190)
    top.mainloop()
def viewMarks():
    top = Toplevel(root)
    top.title('Student report card system')
    top.geometry("650x450")
    top.resizable(width=False,height=False);
    Label(top, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
    Label(top,text="Student Marks", fg="RoyalBlue2",font="comicsansms 10 bold", pady=5).place(x=250,y=50)
    def disp():
        data = []
        with open("marks.csv","r") as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        global tree

        listheader = ['USN', 'SUBJECT1', 'SUBJECT2','SUBJECT3','SUBJECT4','SUBJECT5','SUBJECT6']

        tree = ttk.Treeview(top, selectmode="extended", columns=listheader, show="headings")

        vsb = ttk.Scrollbar(top, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(top, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.place(x=70,y=190)
        #vsb.place(x=200,y=100)
        #hsb.place(x=200,y=300)

        #tree head
        tree.heading(0, text='USN', anchor=NW)
        tree.heading(1, text='SUBJECT1', anchor=NW)
        tree.heading(2, text='SUBJECT2', anchor=NW)
        tree.heading(3, text='SUBJECT3',anchor=NW)
        tree.heading(4, text='SUBJECT4',anchor=NW)
        tree.heading(5, text='SUBJECT5',anchor=NW)
        tree.heading(6, text='SUBJECT6',anchor=NW)
        
        

        # tree  columns
        tree.column(0, width=100, anchor='nw')
        tree.column(1, width=70, anchor='nw')
        tree.column(2, width=70, anchor='nw')
        tree.column(3, width=70, anchor='nw')
        tree.column(4, width=70, anchor='nw')
        tree.column(5, width=70, anchor='nw')
        tree.column(6, width=70, anchor='nw')
        
        data1 = []
        with open("subject.csv","r") as f:
            reader = csv.reader(f)
            for row in reader:
                data1.append(row)
        f.close()
        id = 1
        for item in data:
            #print(item)
            if(item[0]==click.get()):
                tree.insert(parent='',iid=id,open=False,index='end',values=item)
                for item1 in data1:
                    if(item[1]==item1[0]):
                        item1[0] = ''
                        tree.insert(parent=id,open=True,index='end',values=item1)
            id += 1
            
    count=0
    usn = []
    student = []
    with open('students.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            student.append(row)
            a=student[count][0]
            usn.append(a)
            count += 1
    click = StringVar()
    click.set("Select USN")
    drop = OptionMenu(top, click, *usn)
    drop.config(width=20)
    drop.place(x=210,y=100)
    Button(top,text="Submit",command=disp).place(x=260,y=150)
    top.mainloop() 
root.geometry("650x350")
root.resizable(width=False,height=False);
Label(root, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
Label(root,text="Student Portal", fg="RoyalBlue2",font="comicsansms 10 bold", pady=5).place(x=260,y=70)
a = Button(text="View Details",width=20,command=viewStudent).place(x=230,y=140)
e = Button(text="View Marks",width=20,command=viewMarks).place(x=230,y=200)
root.mainloop()