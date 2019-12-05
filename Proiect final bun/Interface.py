from tkinter import *
import backend
from tkinter import messagebox





def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()
    if index:
        selected_tuple=list1.get(index)
    # print(selected_tuple)
        entry1.delete(0,END)
        entry1.insert(0,selected_tuple[1])
        entry2.delete(0,END)
        entry2.insert(0,selected_tuple[2])
        entry3.delete(0,END)
        entry3.insert(0,selected_tuple[3])
    # entry4.delete(0,END)
    # entry4.insert(END,selected_tuple[4])


def view_all():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def add_entry():
    backend.insert(name_text.get(),CNP_text.get(),salariu.get())
    list1.delete(0,END)
    list1.insert(END,(name_text.get(),CNP_text.get(),salariu.get()))
    view_all()

def delete_entry():
    backend.delete(selected_tuple[0])
    view_all()

def update_angajat():
    backend.update_angajat(selected_tuple[0],name_text.get(),CNP_text.get())
    view_all()


def update_salariu():
    backend.update_salariu(selected_tuple[0],name_text.get(),salariu.get())
    view_all()

def bla():
    backend.salariu_redus()
    view_all()

# def minus5():
#     a=float(salariu.get())
#     a=a-a*0.5
#     backend.update(selected_tuple[0],name_text.get(),salariu.get())



# def search_command():
#     list1.delete(0,END)
#     for row back.search(name_text.get(),CNP_text.get(),salariu.get()):
#     list1.insert(END,row)

# def modify_salariu():
#     backend.update(selected_tuple[0],name_text.get(),salariu.get())






window = Tk()
window.title("Proiect Manda")
window.geometry ("800x400")

###### Define the Label and buttons 

label1=Label(window,text="Name",font=("bold",10), pady=20)
label1.grid(row=1,column=0,)


label2=Label(window,text="CNP",font=("bold",10), pady=20)
label2.grid(row=2,column=0)

label3=Label(window,text="Salariu",font=("bold",10), pady=20)
label3.grid(row=3,column=0)

name_text=StringVar()
entry1=Entry(window, textvariable=name_text)
entry1.grid(row=1,column=1,sticky=W)
entry1.insert(0,"Enter your name: ")

CNP_text=StringVar()
entry2=Entry(window,textvariable=CNP_text)
entry2.grid(row=2,column=1,sticky=W)
entry2.insert(0,"Enter your CNP: ")

salariu=StringVar()
entry3=Entry(window,textvariable=salariu)
entry3.grid(row=3,column=1,sticky=W)
entry3.insert(0,"Enter your Salariu: ")


b1=Button(window,text="add entry", width=12, command=add_entry)
b1.grid(row=1, column=3)

b2=Button(window,text="delete entry", width=12,command=delete_entry)
b2.grid(row=1, column=4)

b3=Button(window,text="update angajat", width=12,command=update_angajat)
b3.grid(row=2, column=3)

b4=Button(window,text="modify salariu", width=12,command=update_salariu)
b4.grid(row=2, column=4)

b5=Button(window,text="view all", width=12,command=view_all)
b5.grid(row=3, column=3)

b6=Button(window,text="-5% ", width=12,command=bla)
b6.grid(row=3, column=4)

list1=Listbox(window,height=10,width=59)
list1.grid(row=4,column=1, rowspan =3, columnspan=2)

scrollbar=Scrollbar(window)
scrollbar.grid(row=4,column=0, sticky= 'ns',rowspan =6)

list1.configure(yscrollcommand=scrollbar.set) #connect scrollbar 
scrollbar.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>',get_selected_row)
view_all()




window.mainloop()