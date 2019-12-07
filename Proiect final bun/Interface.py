from tkinter import *
import backend
from tkinter import messagebox
import re


######## Define the functions 

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()
    if index:
        selected_tuple=list1.get(index)
        entry1.delete(0,END)
        entry1.insert(0,selected_tuple[1])
        entry2.delete(0,END)
        entry2.insert(0,selected_tuple[2])
        entry3.delete(0,END)
        entry3.insert(0,selected_tuple[3])
  


def view_all():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)


def add_entry():
    digits=re.search('[0-9]', CNP_text.get())
    letters=re.search('[a-zA-Z]', CNP_text.get())
    symbol=re.search('[!@#$%^&*(),.?":{}|<>]', CNP_text.get())
    digits1=re.search('[0-9]', name_text.get())
    letters1=re.search('[a-zA-Z]', name_text.get())
    symbol1=re.search('[!@#$%^&*(),.?":{}|<>]', name_text.get())
    digits2=re.search('[0,9]', salariu.get())
    letters2=re.search('[a-zA-Z]', salariu.get())
    symbol2=re.search('[!@#$%^&*(),?":{}|<>]', salariu.get())
                                                                            
    if len(name_text.get())==0:
        messagebox.showerror("Eroare", "Numele field nu poate sa fie gol!")
        return
    if len(CNP_text.get())==0:
        messagebox.showerror("Eroare", "CNP field nu poate sa fie gol!")
        return
    if len(salariu.get())==0:
        messagebox.showerror("Eroare", "Salariu field nu poate sa fie gol!")
        return
    for i in range(len(CNP_text.get())):
        for j in range(len(name_text.get())):
            for k in range(len(salariu.get())):
                if letters or symbol:
                    letters==True 
                    symbol==True
                    messagebox.showerror("Eroare", "CNP-ul nu poate sa contina litere sau simboluri!")
                    return
                elif digits1 or symbol1:
                    digits1==True 
                    symbol1==True
                    messagebox.showerror("Eroare", "Numele nu poate contine cifre sau simboluri!")
                    return
                elif letters2 or symbol2:
                    letters2==True 
                    messagebox.showerror("Eroare", "Salariul nu poate contine cifre sau simboluri!")
                    return
                elif digits and len(str(CNP_text.get()))==13:
                    digits==True
                    backend.insert(name_text.get(),CNP_text.get(),salariu.get())########apeleaza functia insert din backend.py
                    list1.delete(0,END)
                    list1.insert(END,(name_text.get(),CNP_text.get(),salariu.get()))
                    clear_text()
                    break
                elif len(str(CNP_text.get()))!=13:
                    messagebox.showerror("Eroare", "CNP-ul nu are 13 caractere!")
                    return

def delete_entry():
    backend.delete(selected_tuple[0]) ########apeleaza functia delete din backend.py
    view_all()

def update_angajat():
    digits=re.search('[0-9]', CNP_text.get())
    letters=re.search('[a-zA-Z]', CNP_text.get())
    symbol=re.search('[!@#$%^&*(),.?":{}|<>]', CNP_text.get())
    digits1=re.search('[0-9]', name_text.get())
    letters1=re.search('[a-zA-Z]', name_text.get())
    symbol1=re.search('[!@#$%^&*(),.?":{}|<>]', name_text.get())
    digits2=re.search('[0,9]', salariu.get())
    letters2=re.search('[a-zA-Z]', salariu.get())
    symbol2=re.search('[!@#$%^&*(),?":{}|<>]', salariu.get())
    
    if len(name_text.get())==0:
        messagebox.showinfo("Eroare", "Numele field nu poate sa fie gol!")
        return
    if len(CNP_text.get())==0:
        messagebox.showinfo("Eroare", "CNP field nu poate sa fie gol!")
        return
    if len(salariu.get())==0:
        messagebox.showinfo("Eroare", "Salariu field nu poate sa fie gol!")
    
    for i in range(len(CNP_text.get())):
        for j in range(len(name_text.get())):
            for k in range(len(salariu.get())):
                if letters or symbol:
                    letters==True 
                    symbol==True
                    messagebox.showinfo("Eroare", "CNP-ul nu poate contine litere sau simboluri!")
                    return 
                
                elif digits1 or symbol1:
                    digits1==True 
                    symbol1==True
                    messagebox.showinfo("Eroare", "Numele nu poate contine cifre sau simboluri!")
                    return
                
                elif letters2 or symbol2:
                    letters2==True 
                    messagebox.showinfo("Eroare", "Salariul nu poate contine cifre sau simboluri!")
                    return
                
                elif digits and len(str(CNP_text.get()))==13:
                    digits==True
                    backend.update_angajat(selected_tuple[0],name_text.get(),CNP_text.get()) ########apeleaza functia update_angajat din backend.py
                    
                    break
                elif len(str(CNP_text.get()))!=13:
                    messagebox.showinfo("Eroare", "CNP-ul nu are 13 caractere!")
                    return
    
    view_all()


def update_salariu():
    backend.update_salariu(selected_tuple[0],name_text.get(),salariu.get())   ########apeleaza functia update_salariu din backend.py
    view_all()

def minus5():
    backend.salariu_redus()
    view_all()

def clear_text():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

def clickExitButton(): 
        exit()

######  Interface, Label and buttons ######


#######

window = Tk()                                  # Create instance
window.title("Proiect Manda Mihaita")          # Create title
window.geometry ("800x450+50+50")



######Labels

label1=Label(window,text="Name",font=("calibri",12), pady=20)
label1.grid(row=1,column=0,)


label2=Label(window,text="CNP",font=("calibri",12), pady=20)
label2.grid(row=2,column=0)

label3=Label(window,text="Salariu",font=("calibri",12), pady=20)
label3.grid(row=3,column=0)


#######Input boxes 

name_text=StringVar()
entry1=Entry(window, textvariable=name_text)
entry1.grid(row=1,column=1,sticky=W)
entry1.insert(0,"Enter your Name: ")

CNP_text=StringVar()
entry2=Entry(window,textvariable=CNP_text)
entry2.grid(row=2,column=1,sticky=W)
entry2.insert(0,"Enter your CNP: ")

salariu=StringVar()
entry3=Entry(window,textvariable=salariu)
entry3.grid(row=3,column=1,sticky=W)
entry3.insert(0,"Enter your Salariu: ")


#########Buttons

b1=Button(window,text="Adaugare angajat", width=12, command=add_entry)
b1.grid(row=1, column=3)


b2=Button(window,text="Sterge angajat", width=12,command=delete_entry)
b2.grid(row=1, column=4)

b3=Button(window,text="Modifica angajat", width=12,command=update_angajat)
b3.grid(row=2, column=3)

b4=Button(window,text="Modifica Salariu", width=12,command=update_salariu)
b4.grid(row=2, column=4)

b5=Button(window,text="view all", width=12,command=view_all)
b5.grid(row=3, column=3)

b6=Button(window,text="-5% ", width=12,command=minus5)
b6.grid(row=3, column=4)

b6=Button(window,text="Exit", width=12,command=clickExitButton)
b6.grid(row=7, column=4)

#######Listbox#####

list1=Listbox(window,height=10,width=59)
list1.grid(row=4,column=1, rowspan =3, columnspan=2)

scrollbar=Scrollbar(window)
scrollbar.grid(row=4,column=0, sticky= 'ns',rowspan =6)

list1.configure(yscrollcommand=scrollbar.set) #connect scrollbar 
scrollbar.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>',get_selected_row)
view_all()



window.resizable(0, 0)
window.mainloop()