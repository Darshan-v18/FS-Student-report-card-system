from asyncio.windows_events import NULL
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
root = Tk();
root.title('Student report card system')
def addStudent():
    top = Toplevel(root);
    top.title('Student report card system')
    def insert():
           
            b = namee.get()
            c = usne.get()
            d = branche.get()
            f = click.get()
            e = semaile.get()
            slist = [c,b,d,f,e]
            with open('students.csv','a+',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(slist)
            f.close()
            messagebox.showinfo(title="Success",message="Record successfuly inserted.")
            
            namee.delete(0,END);
            usne.delete(0,END);
            branche.delete(0,END);
            
            semaile.delete(0,END)
            top.destroy()
            
    
        
    top.geometry("650x400")
    top.resizable(width=False,height=False);
    Label(top, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
    Label(top,text="Add Student", fg="RoyalBlue2",font="comicsansms 10 bold", pady=5).place(x=260,y=50)
    count=0
    sem = []
    subject = []
    with open('subject.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            subject.append(row)
            a=subject[count][0]
            sem.append(a)
            count += 1
    #id = Label(root,text="ID")
    name = Label(top,text="Name")
    usn = Label(top,text="USN")
    semail = Label(top,text="E-mail")
    ssem = Label(top,text="Semester")
    branch = Label(top,text="Branch")

    #sid.place(x=200,y=100)
    name.place(x=200,y=150)
    usn.place(x=200,y=100)
    semail.place(x=200,y=200)
    branch.place(x=200,y=250)
    ssem.place(x=200,y=300)

    #sidValue = StringVar()
    nameValue = StringVar()
    usnValue = StringVar()
    semailValue = StringVar()
    
    branchValue = StringVar()
    click = StringVar()
    click.set("Select Semester")
    drop = OptionMenu(top, click, *sem)
    drop.config(width=20)
    drop.place(x=200,y=300)
    
    #side = Entry(root,textvariable=sidValue)
    namee = Entry(top,textvariable=nameValue)
    usne = Entry(top,textvariable=usnValue)
    semaile = Entry(top,textvariable=semailValue)
    branche = Entry(top,textvariable=branchValue)
    
    #side.place(x=260,y=100)
    namee.place(x=260,y=150)
    usne.place(x=260,y=100)
    semaile.place(x=260,y=200)
    branche.place(x=260,y=250)
   
    Button(top,text="Add",command=insert,width=15).place(x=240,y=350)
    top.mainloop()


def removeStudent():
    topv = Toplevel(root)
    topv.title('Student report card system')
    topv.geometry("650x350")
    topv.resizable(width=False,height=False);
    Label(topv, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
    Label(topv,text="Student Details", fg="RoyalBlue2", font="comicsansms 10 bold", pady=5).place(x=250,y=45)
    def update():
        top = Toplevel(topv)
        top.geometry("650x400")
        top.resizable(width=False,height=False);
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        Label(top, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
        Label(top,text="Add Student", font="comicsansms 10 bold", pady=5).place(x=260,y=50)
        #id = Label(root,text="ID")
        name = Label(top,text="Name")
        usn = Label(top,text="USN")
        semail = Label(top,text="E-mail")
        branch = Label(top,text="Branch")

        #sid.place(x=200,y=100)
        name.place(x=200,y=150)
        usn.place(x=200,y=100)
        semail.place(x=200,y=200)
        branch.place(x=200,y=250)

        #sidValue = StringVar()
        nameValue = StringVar()
        usnValue = StringVar()
        semailValue = StringVar()
        branchValue = StringVar()
        
        #side = Entry(root,textvariable=sidValue)
        namee = Entry(top,textvariable=nameValue)
        usne = Entry(top,textvariable=usnValue)
        semaile = Entry(top,textvariable=semailValue)
        
        branche = Entry(top,textvariable=branchValue)
        #side.place(x=260,y=100)
        namee.place(x=260,y=150)
        usne.place(x=260,y=100)
        semaile.place(x=260,y=200)
        branche.place(x=260,y=250)
        usne.insert(0,tree_list[0])
        namee.insert(0,tree_list[1])
        semaile.insert(0,tree_list[2])
        branche.insert(0,tree_list[3])
        def updateStudent(i):
            def updateNewlist(j):
                with open('students.csv','w',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(j)
                f.close()
            newList = []
            id = str(i[0])
            with open('students.csv','r') as f:
                reader = csv.reader(f)
                for row in reader:
                    newList.append(row)
                    for element in row:
                        if element == id:
                            name = i[1]
                            email = i[2]
                            branc = i[3]
                            data = [id,name,email,branc]
                            index = newList.index(row)
                            newList[index] = data
            f.close()
            updateNewlist(newList)
        def abc():
            idu = usne.get()
            nameu = namee.get()    
            emailu = semaile.get()
            branchu = branche.get()
            nl = [idu,nameu,emailu,branchu]
            updateStudent(nl)
            messagebox.showinfo("Success","Record updated successfuly")
            usne.delete(0,END)
            namee.delete(0,END)
            semaile.delete(0,END)   
            branche.delete(0,END)
            top.destroy()
            disp()
        Button(top,text="Update",command=abc).place(x=240,y=300)
        
        top.mainloop()
    def disp():
        data = []
        with open("students.csv","r") as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        f.close()       
        global tree


        listheader = ['Name', 'USN','Branch','Section']

        tree = ttk.Treeview(topv, selectmode="extended", columns=listheader, show="headings")

        vsb = ttk.Scrollbar(topv, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(topv, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.place(x=140,y=80)
        # vsb.place(x=200,y=100)
        # hsb.place(x=200,y=100)

        #tree head
        tree.heading(0, text='Name', anchor=NW)
        tree.heading(1, text='USN', anchor=NW)
        tree.heading(2, text='Branch', anchor=NW)
        tree.heading(3, text='Section',anchor=NW)
        

        # tree  columns
        tree.column(0, width=50, anchor='nw')
        tree.column(1, width=100, anchor='nw')
        tree.column(2, width=120, anchor='nw')
        tree.column(3, width=140, anchor='nw')
        
        for item in data:
            tree.insert(parent='', index='end',values=item)
    disp()
    def to_remove():
        try:
            tree_data = tree.focus()
            tree_dictionary = tree.item(tree_data)
            tree_list = tree_dictionary['values']
            tree_student = str(tree_list[0])
            remove(tree_student)

            messagebox.showinfo('Success', 'Data has been deleted successfully')

            
            disp()
            topv.destroy()
            

        except IndexError:
            messagebox.showerror('Error', 'Select one of them from the table')
    def remove(i):
        def save(j):
            with open('students.csv','w',newline='') as f:
                writer = csv.writer(f)
                writer.writerows(j)
            f.close()
        newList = []
        id = i
        with open('students.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                newList.append(row)

                for element in row:
                    if element == id:
                        newList.remove(row)
        save(newList)
    Button(topv,text="Remove",command=to_remove,width=8).place(x=250,y=315)
    Button(topv,text="Update",width=8,command=update).place(x=350,y=315)
    topv.mainloop()

    
def addMarks():
    top = Toplevel(root);
    top.title('Student report card system')
    def insert():
            sem = []
            usn = click.get()
            with open('students.csv')as f:
                reader =csv.reader(f)
                for row in reader:
                    sem.append(row)
            f.close()
            x = ''
            for i in sem:
                if(usn==i[0]):
                    x = i[3]
                    break
                     
            a = m1e.get()
            b = m2e.get()
            c = m3e.get()
            d = m4e.get()
            e = m5e.get()
            f = m6e.get()
            

            
            if ( a=='' or b=='' or c=='' or d=='' or e=='' or f=='' or usn=='Select USN'):
                messagebox.showerror("Error!","Fields cannot be empty")
            else:
                tlist = [usn,x,a,b,c,d,e,f]
                with open('marks.csv','a+',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(tlist)
                f.close()
                messagebox.showinfo(title="Success",message="Marks successfuly inserted.")
                m1e.delete(0,END);
                m2e.delete(0,END);
                m3e.delete(0,END);
                m4e.delete(0,END);
                m5e.delete(0,END);
                m6e.delete(0,END);
                
                top.destroy()

    # def Select():
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


        
        
                    
    
    top.geometry("650x550")
    top.resizable(width=False,height=False);
    Label(top, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
    Label(top,text="Add Marks", font="comicsansms 10 bold", pady=5).place(x=260,y=50)
    click = StringVar()
    click.set("Select USN")
    drop = OptionMenu(top, click, *usn)
    drop.config(width=20)
    drop.place(x=230,y=50)

    m1 = Label(top,text="subject1")
    m2 = Label(top,text="subject2")
    m3 = Label(top,text="subject3")
    m4 = Label(top,text="subject4")
    m5 = Label(top,text="subject5")
    m6 = Label(top,text="subject6")
    m1.place(x=200,y=100)
    m2.place(x=200,y=150)
    m3.place(x=200,y=200)
    m4.place(x=200,y=250)
    m5.place(x=200,y=300)
    m6.place(x=200,y=350)
    m1Value = StringVar()
    m2Value = StringVar()
    m3Value = StringVar()
    m4Value = StringVar()
    m5Value = StringVar()
    m6Value = StringVar()
    m1e = Entry(top,textvariable=m1Value)
    m2e = Entry(top,textvariable=m2Value)
    m3e = Entry(top,textvariable=m3Value)
    m4e = Entry(top,textvariable=m4Value)
    m5e = Entry(top,textvariable=m5Value)
    m6e = Entry(top,textvariable=m6Value)
    m1e.place(x=260,y=100)
    m2e.place(x=260,y=150)
    m3e.place(x=260,y=200)
    m4e.place(x=260,y=250)
    m5e.place(x=260,y=300)
    m6e.place(x=260,y=350)

    Button(top,text="Add Marks",command=insert,width=15).place(x=240,y=400)
    
    top.mainloop()


def view():
    topv = Toplevel(root)
    topv.title('Student report card system')
    def to_search():
                    usn = e_search.get()
                    if(str(usn) == ''):
                        disp()
                    else:

                        data = search(str(usn))
                        
                        if(len(data) == 0):
                            tree.delete(*tree.get_children())

                        else:
                            final_data = []
                            final_data.append(data[0][0])
                            final_data.append(data[0][1])
                            final_data.append(data[0][2])
                            final_data.append(data[0][3])
                            final_data.append(data[0][4])
                            final_data.append(data[0][5])
                            final_data.append(data[0][6])
                            # print(final_data)
                            
                            tree.delete(*tree.get_children())
                            tree.insert('',END,values = final_data)
                            e_search.delete(0,END)
    def search(i):
        data = []
        usn = i 
        with open('Marks.csv','r') as f:
            reader = csv.reader(f)
            for row in reader:
                for element in row:
                    if element == usn:
                        data.append(row)
        f.close()
        return data
                
                # Search label and entry

    e_search = Entry(topv)
    e_search.place(x=600,y=75)
    b = Button(topv,text="Search",command=to_search).place(x=730,y=71)

    def update():
        top = Toplevel(topv)
        top.title('Student report card system')
        top.geometry("650x550")
        top.resizable(width=False,height=False);
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values'    ]
        Label(root, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
        Label(top,text="Add Marks", font="comicsansms 10 bold", pady=5).place(x=260,y=50)
        usn = Label(top,text="USN")
        m1 = Label(top,text="subject1")
        m2 = Label(top,text="subject2")
        m3 = Label(top,text="subject3")
        m4 = Label(top,text="subject4")
        m5 = Label(top,text="subject5")
        m6 = Label(top,text="subject6")
        usn.place(x=200,y=100)
        m1.place(x=200,y=150)
        m2.place(x=200,y=200)
        m3.place(x=200,y=250)
        m4.place(x=200,y=300)
        m5.place(x=200,y=350)
        m6.place(x=200,y=400)
        usnValue = StringVar()
        m1Value = StringVar()
        m2Value = StringVar()
        m3Value = StringVar()
        m4Value = StringVar()
        m5Value = StringVar()
        m6Value = StringVar()
        usne = Entry(top,textvariable=usnValue)
        m1e = Entry(top,textvariable=m1Value)
        m2e = Entry(top,textvariable=m2Value)
        m3e = Entry(top,textvariable=m3Value)
        m4e = Entry(top,textvariable=m4Value)
        m5e = Entry(top,textvariable=m5Value)
        m6e = Entry(top,textvariable=m6Value)
        usne.place(x=260,y=100)
        m1e.place(x=260,y=150)
        m2e.place(x=260,y=200)
        m3e.place(x=260,y=250)
        m4e.place(x=260,y=300)
        m5e.place(x=260,y=350)
        m6e.place(x=260,y=400)
        usne.insert(0,tree_list[0])
        m1e.insert(0,tree_list[1])
        m2e.insert(0,tree_list[2])
        m3e.insert(0,tree_list[3])
        m4e.insert(0,tree_list[4])
        m5e.insert(0,tree_list[5])
        m6e.insert(0,tree_list[6])
        def updateMarks(i):
            def updateNewlist(j):
                with open('marks.csv','w',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(j)
                f.close()
            newList = []
            id = str(i[0])
            with open('marks.csv','r') as f:
                reader = csv.reader(f)
                for row in reader:
                    newList.append(row)
                    for element in row:
                        if element == id:
                            m1 = i[1]
                            m2 = i[2]
                            m3 = i[3]
                            m4 = i[4]
                            m5 = i[5]
                            m6 = i[6]
                            data = [id,m1,m2,m3,m4,m5,m6]
                            index = newList.index(row)
                            newList[index] = data
            f.close()
            updateNewlist(newList)
        def abc():
            usng = usne.get()
            m1g = m1e.get()
            m2g = m2e.get()
            m3g = m3e.get()
            m4g = m4e.get()
            m5g = m5e.get()
            m6g = m6e.get()
            nl = [usng,m1g,m2g,m3g,m4g,m5g,m6g]
            updateMarks(nl)
            messagebox.showinfo("Success","Record updated successfuly")
            usne.delete(0,END)
            m1e.delete(0,END)
            m2e.delete(0,END)
            m3e.delete(0,END)
            m4e.delete(0,END)
            m5e.delete(0,END)
            m6e.delete(0,END)
            top.destroy()
            disp()
        Button(top,text="Update",command=abc).place(x=260,y=470)
        top.mainloop()

    topv.geometry("900x450")
    topv.resizable(width=False,height=False);
    Label(topv, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=340,y=5)
    Label(topv,text="Student Marks", fg="RoyalBlue2",font="comicsansms 10 bold", pady=5).place(x=410,y=50)


    
    def to_remove():
        try:
            tree_data = tree.focus()
            tree_dictionary = tree.item(tree_data)
            tree_list = tree_dictionary['values']
            tree_marks = str(tree_list[0])
            remove(tree_marks)

            messagebox.showinfo('Success', 'Data has been deleted successfully')

            
            disp()
            topv.destroy()
            

        except IndexError:
            messagebox.showerror('Error', 'Select one of them from the table')
    def remove(i):
        def save(j):
            with open('marks.csv','w',newline='') as f:
                writer = csv.writer(f)
                writer.writerows(j)
            f.close()
        newList = []
        id = i
        with open('marks.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                newList.append(row)

                for element in row:
                    if element == id:
                        newList.remove(row)
        save(newList)

    def disp():
        data = []
        with open("marks.csv","r") as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        f.close()
        data1 = []
        with open("subject.csv","r") as f:
            reader = csv.reader(f)
            for row in reader:
                data1.append(row)
        f.close()
        # print(data1)
        global tree

        listheader = ['USN', 'SUBJECT1', 'SUBJECT2','SUBJECT3','SUBJECT4','SUBJECT5','SUBJECT6']

        tree = ttk.Treeview(topv, selectmode="extended", columns=listheader, show="headings")

        vsb = ttk.Scrollbar(topv, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(topv, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.place(x=110,y=100)
        # vsb.place(x=200,y=100)
        # hsb.place(x=200,y=100)

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
        tree.column(1, width=100, anchor='nw')
        tree.column(2, width=120, anchor='nw')
        tree.column(3, width=100, anchor='nw')
        tree.column(4, width=100, anchor='nw')
        tree.column(5, width=100, anchor='nw')
        tree.column(6, width=100, anchor='nw')
        
        
        id = 1
        for item in data:
            print(item)
            
            tree.insert(parent='', iid=id,open=False,index='end',values=item)
            for item1 in data1:

                if(item[1]==item1[0]):
                    item1[0] = ''
                    tree.insert(parent=id,open=True,index='end',values=item1)
            id += 1

    
    disp()
    Button(topv,text="Update",command=update,width=10).place(x=400,y=330)
    Button(topv,text="Delete",command = to_remove,width=10).place(x=500,y=330)
    topv.mainloop()
    
root.geometry("650x350")
root.resizable(width=False,height=False);
Label(root, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
Label(root,text="Faculty Portal",fg="RoyalBlue2", font="comicsansms 10 bold", pady=5).place(x=260,y=50)
a = Button(text="Add Student",width=20,command=addStudent).place(x=230,y=120)
b = Button(text="View Student",width=20,command=removeStudent).place(x=230,y=165)
d = Button(text="Add Student marks",width=20,command=addMarks).place(x=230,y=210)
e = Button(text="View Student Marks",width=20,command=view).place(x=230,y=255)
root.mainloop()