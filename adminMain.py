from tkinter import *
from tkinter import messagebox
from tkinter import ttk;
import csv
root = Tk();
root.title('Student report card system')
def add():
    top = Toplevel(root)
    top.title('Student report card system')
    top.geometry("650x350")
    top.resizable(width=False,height=False);
    Label(top, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
    Label(top,text="Add Teacher",fg="RoyalBlue2", font="comicsansms 10 bold", pady=5).place(x=260,y=50)
    tid = Label(top,text="ID")
    name = Label(top,text="Name")
    temail = Label(top,text="E-mail")
    tpass = Label(top,text="Password")
    tid.place(x=200,y=100)
    name.place(x=200,y=150)
    temail.place(x=200,y=200)
    tpass.place(x=200,y=250)
    tidValue = StringVar()
    nameValue = StringVar()
    temailValue = StringVar()
    tpassValue = StringVar()
    tide = Entry(top,textvariable=tidValue)
    namee = Entry(top,textvariable=nameValue)
    emaile = Entry(top,textvariable=temailValue)
    tpasse = Entry(top,textvariable=tpassValue)
    tide.place(x=260,y=100)
    namee.place(x=260,y=150)
    emaile.place(x=260,y=200)
    tpasse.place(x=260,y=250)
    tpasse.config(show="*")
    def insert():
        a = tide.get()
        b = namee.get()
        c = emaile.get()
        d = tpasse.get()
        if ( a=='' or b=='' or c=='' or d==''):
            messagebox.showerror("Error!","Fields cannot be empty")
        else:
            tlist = [a,b,c,d]
            with open('teachers.csv','a+',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(tlist)
            f.close()
            messagebox.showinfo(title="Success",message="Record successfuly inserted.")
            tide.delete(0,END);
            namee.delete(0,END);
            emaile.delete(0,END);
            tpasse.delete(0,END);
            top.destroy()
    Button(top,text="Add",command=insert,width=15).place(x=240,y=300)
    top.mainloop()

    
def view():
    topv= Toplevel(root)
    topv.title('Student report card system')
    topv.geometry("650x400")
    topv.resizable(width=False,height=False);
    Label(topv, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
    Label(topv,text="Teacher Details", fg="RoyalBlue2",font="comicsansms 10 bold", pady=5).place(x=250,y=50)
    def update():
        top = Toplevel(topv)
        top.geometry("650x400")
        top.resizable(False,False)
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        Label(top, fg="tomato2",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
        Label(top,text="Add Teacher", fg="RoyalBlue2",font="comicsansms 10 bold", pady=5).place(x=260,y=50)
        tid = Label(top,text="ID")
        name = Label(top,text="Name")
        temail = Label(top,text="E-mail")
        tpass = Label(top,text="Password")
        tid.place(x=200,y=100)
        name.place(x=200,y=150)
        temail.place(x=200,y=200)
        tpass.place(x=200,y=250)
        tidValue = StringVar()
        nameValue = StringVar()
        temailValue = StringVar()
        tpassValue = StringVar()
        tide = Entry(top,textvariable=tidValue)
        namee = Entry(top,textvariable=nameValue)
        emaile = Entry(top,textvariable=temailValue)
        tpasse = Entry(top,textvariable=tpassValue)
        tide.place(x=260,y=100)
        namee.place(x=260,y=150)
        emaile.place(x=260,y=200)
        tpasse.place(x=260,y=250)
        tide.insert(0,tree_list[0])
        namee.insert(0,tree_list[1])
        emaile.insert(0,tree_list[2])
        tpasse.insert(0,tree_list[3])
        def updateTeacher(i):
            def updateNewlist(j):
                with open('teachers.csv','w',newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(j)
                f.close()
            newList = []
            id = str(i[0])
            with open('teachers.csv','r') as f:
                reader = csv.reader(f)
                for row in reader:
                    newList.append(row)
                    for element in row:
                        if element == id:
                            name = i[1]
                            email = i[2]
                            passw = i[3]
                            data = [id,name,email,passw]
                            index = newList.index(row)
                            newList[index] = data
            f.close()
            updateNewlist(newList)
        def abc():
            idu = tide.get()
            nameu = namee.get()    
            emailu = emaile.get()
            passu = tpasse.get()
            nl = [idu,nameu,emailu,passu]
            updateTeacher(nl)
            messagebox.showinfo("Success","Record updated successfuly")
            tide.delete(0,END)
            namee.delete(0,END)
            emaile.delete(0,END)   
            tpasse.delete(0,END)
            top.destroy()
            disp()
        Button(top,text="update",command=abc).place(x=260,y=300)
        top.mainloop()
    def disp():
        data = []
        with open("teachers.csv","r") as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        f.close()
        global tree

        listheader = ['ID', 'Name', 'Email','Password']

        tree = ttk.Treeview(topv, selectmode="extended", columns=listheader, show="headings")

        vsb = ttk.Scrollbar(topv, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(topv, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.place(x=140,y=100)
        # vsb.place(x=200,y=100)
        # hsb.place(x=200,y=100)

        #tree head
        tree.heading(0, text='ID', anchor=NW)
        tree.heading(1, text='Name', anchor=NW)
        tree.heading(2, text='Email', anchor=NW)
        tree.heading(3, text='Password',anchor=NW)
        

        # tree  columns
        tree.column(0, width=50, anchor='nw')
        tree.column(1, width=100, anchor='nw')
        tree.column(2, width=120, anchor='nw')
        tree.column(3, width=100, anchor='nw')
        
        
        for item in data:
            tree.insert(parent='', index='end',values=item)
        
    
    disp()
    Button(topv,text="Update",command=update).place(x=280,y=330)

    def to_search():
                    name = e_search.get()
                    if(str(name) == ''):
                        disp()
                    else:

                        data = search(str(name))
                        
                        if(len(data) == 0):
                            tree.delete(*tree.get_children())

                        else:
                            final_data = []
                            final_data.append(data[0][0])
                            final_data.append(data[0][1])
                            final_data.append(data[0][2])
                            final_data.append(data[0][3])
                            
                            # print(final_data)
                            
                            tree.delete(*tree.get_children())
                            tree.insert('',END,values = final_data)
                            e_search.delete(0,END)
                    
    def search(i):
        data = []
        name= i 
        with open('teachers.csv','r') as f:
            reader = csv.reader(f)
            for row in reader:
                for element in row:
                    if element == name:
                        data.append(row)
        f.close()
        return data

    
    e_search = Entry(topv)
    e_search.place(x=400,y=75)
    b = Button(topv,text="Search",command=to_search)
    b.place(x=530,y=71)
    topv.mainloop()
def remove():
    top = Toplevel(root)
    top.title('Student report card system')
    top.geometry("650x350")
    top.resizable(width=False,height=False);
    Label(top, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
    Label(top,text="Teacher Details", fg="RoyalBlue2",font="comicsansms 10 bold", pady=5).place(x=250,y=45)

    def disp():
        data = []
        with open("teachers.csv","r") as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        f.close()       
        global tree


        listheader = ['ID', 'Name', 'Email','Password']

        tree = ttk.Treeview(top, selectmode="extended", columns=listheader, show="headings")

        vsb = ttk.Scrollbar(top, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(top, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.place(x=140,y=80)
        # vsb.place(x=200,y=100)
        # hsb.place(x=200,y=100)

        #tree head
        tree.heading(0, text='ID', anchor=NW)
        tree.heading(1, text='Name', anchor=NW)
        tree.heading(2, text='Email', anchor=NW)
        tree.heading(3, text='Password',anchor=NW)
        

        # tree  columns
        tree.column(0, width=50, anchor='nw')
        tree.column(1, width=100, anchor='nw')
        tree.column(2, width=120, anchor='nw')
        tree.column(3, width=100, anchor='nw')
        
        for item in data:
            tree.insert(parent='', index='end',values=item)
    disp()
    def to_remove():
        try:
            tree_data = tree.focus()
            tree_dictionary = tree.item(tree_data)
            tree_list = tree_dictionary['values']
            tree_teacher = str(tree_list[0])
            remove(tree_teacher)

            messagebox.showinfo('Success', 'Data has been deleted successfully')

            
            disp()
            top.destroy()
            

        except IndexError:
            messagebox.showerror('Error', 'Select one of them from the table')
    def remove(i):
        def save(j):
            with open('teachers.csv','w',newline='') as f:
                writer = csv.writer(f)
                writer.writerows(j)
            f.close()
        newList = []
        id = i
        with open('teachers.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                newList.append(row)

                for element in row:
                    if element == id:
                        newList.remove(row)
        save(newList)
    Button(top,text="Remove",command=to_remove,width=15).place(x=250,y=315)
    top.mainloop()

root.geometry("650x350")
root.resizable(width=False,height=False);
Label(root, fg="firebrick1",text="Student Report Card System", font="comicsansms 13 bold", pady=15).place(x=190,y=5)
Label(root,text="Admin Portal", fg="RoyalBlue2",font="comicsansms 10 bold", pady=5).place(x=260,y=50)
a = Button(text="Add Teacher",width=20,command=add).place(x=230,y=120)
b = Button(text="Remove Teacher",command=remove,width=20).place(x=230,y=165)
d = Button(text="View",width=20,command=view).place(x=230,y=210)
root.mainloop()