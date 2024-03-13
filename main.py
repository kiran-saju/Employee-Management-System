from tkinter import *
from tkinter import ttk
from db1 import Database
from tkinter import messagebox

db=Database("Emp.db")

root=Tk() #root is object for Tkinter
root.title("Employee Management System")
root.geometry("1366x768+0+0") #for window size (0,0 for x&y axis)
root.config(bg="#2c3e50")
root.state("zoomed")

name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()
# address=StringVar()

#entry frame
entries_frame=Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X) #for pack to entry frame
title=Label(entries_frame,text="Employee Management System",font=("Calibra",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20)

lblName=Label(entries_frame,text="Name",font=("Calibri",16),bg="#535c68",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtName=Entry(entries_frame,textvariable=name,font=("Calibri",16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky="w")

lblAge=Label(entries_frame,text="Age",font=("Calibri",16),bg="#535c68",fg="white")
lblAge.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtAge=Entry(entries_frame,textvariable=age,font=("Calibri",16),width=30)
txtAge.grid(row=1,column=3,padx=10,pady=10,sticky="w")

lblDoj=Label(entries_frame,text="Date",font=("Calibri",16),bg="#535c68",fg="white")
lblDoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtDoj=Entry(entries_frame,textvariable=doj,font=("Calibri",16),width=30)
txtDoj.grid(row=2,column=1,padx=10,pady=10,sticky="w")

lblEmail=Label(entries_frame,text="Email",font=("Calibri",16),bg="#535c68",fg="white")
lblEmail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txtEmail=Entry(entries_frame,textvariable=email,font=("Calibri",16),width=30)
txtEmail.grid(row=2,column=3,padx=10,pady=10,sticky="w")

lblGender=Label(entries_frame,text="Gender",font=("Calibri",16),bg="#535c68",fg="white")
lblGender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
comboGender=ttk.Combobox(entries_frame,textvariable=gender,font=("Calibri",16),width=28,state="readonly")
comboGender['value']=("Male","Female")
comboGender.grid(row=3,column=1,padx=10,pady=10,sticky="w")

lblContact=Label(entries_frame,text="Contact",font=("Calibri",16),bg="#535c68",fg="white")
lblContact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txtContact=Entry(entries_frame,textvariable=contact,font=("Calibri",16),width=30)
txtContact.grid(row=3,column=3,padx=10,pady=10,sticky="w") 

lblAdress=Label(entries_frame,text="Address",font=("Calibri",16),bg="#535c68",fg="white")
lblAdress.grid(row=4,column=0,padx=10,pady=10,sticky="w")
txtAdress=Text(entries_frame,width=85,height=3,font=("Calibri",16))
txtAdress.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

def getData(event):
    selectedrow= tv.focus()
    data=tv.item(selectedrow)
    global row 
    row=data["values"]
    # print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAdress.delete(1.0,END)
    txtAdress.insert(END,row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for rows in db.fetch():
        tv.insert("",END,values=rows)
def add_employee():
    if txtName.get() ==""or txtAge.get()=="" or txtDoj.get()=="" or txtEmail.get()=="" or comboGender.get()=="" or txtContact.get()=="" or txtAdress.get(1.0,END)=="":
        messagebox.showerror("Error in input","Please fill all the details")
        return
    db.insert(txtName.get(),txtAge.get(),txtDoj.get(),txtEmail.get(),comboGender.get(), txtContact.get(),txtAdress.get(1.0,END))
    messagebox.showinfo("Success","Record Inserted")
    clearAll()
    displayAll()

def update_employee():
    if txtName.get() ==""or txtAge.get()=="" or txtDoj.get()=="" or txtEmail.get()=="" or comboGender.get()=="" or txtContact.get()=="" or txtAdress.get(1.0,END)=="":
        messagebox.showerror("Error in input","Please fill all the details")
        return
    db.update(row[0],txtName.get(),txtAge.get(),txtDoj.get(),txtEmail.get(),comboGender.get(), txtContact.get(),txtAdress.get(1.0,END))
    messagebox.showinfo("Success","Record Updated")
    clearAll()
    displayAll()

def delete_employee():
    db.remove(row[0])
    clearAll()
    displayAll()
                      
def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    email.set("")
    gender.set("")
    contact.set("")
    txtAdress.delete(1.0,END)

btn_frame=Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")

btnAdd=Button(btn_frame,command=add_employee,text="Add Details",width=15,font=("Calibri",16,"bold"),fg="white",bg="#16a885",bd=0)
btnAdd.grid(row=0,column=0,padx=10)

btnUpdate=Button(btn_frame,command=update_employee,text="Update Details",width=15,font=("Calibri",16,"bold"),fg="white",bg="#2980b9",bd=0)
btnUpdate.grid(row=0,column=1,padx=10)

btnDelete=Button(btn_frame,command=delete_employee,text="Delete Details",width=15,font=("Calibri",16,"bold"),fg="white",bg="#c0392b",bd=0)
btnDelete.grid(row=0,column=2,padx=10)

btnClear=Button(btn_frame,command=clearAll,text="Clear Details",width=15,font=("Calibri",16,"bold"),fg="white",bg="#f39c12",bd=0)
btnClear.grid(row=0,column=3,padx=10)

#table frame
tree_frame=Frame(root,bg="white")
tree_frame.place(x=0,y=480,width=1500, height=520)
style=ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',18),rowheight=50) #modify font of body
style.configure("mystyle.Treeview.Headings",font=('Calibri',18))
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8))
tv.heading("1", text="ID")
tv.column("1",width=1)
tv.heading("2",text="Name")
tv.heading("3",text="Age")
tv.column("3",width=1)
tv.heading("4",text="D.O.B")
tv.column("4",width=5)
tv.heading("5",text="Email")
tv.heading("6",text="Gender")
tv.column("6",width=1)
tv.heading("7",text="Contact")
tv.column("7",width=3)
tv.heading("8",text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)

displayAll()
displayAll()
root.mainloop()