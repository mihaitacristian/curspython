from tkinter import *
from tkinter import messagebox
from db import Database
import re
db=Database("store.db")


def selecteaza(event):
    global item_selectat
    index=angajati_list.curselection()[0]
    item_selectat=angajati_list.get(index)
    print(item_selectat)

    nume_entry.delete(0,END)
    nume_entry.insert(END,item_selectat[1])
    CnP_entry.delete(0,END)
    CnP_entry.insert(END,item_selectat[2])
    salariu_entry.delete(0,END)
    salariu_entry.insert(END,item_selectat[3])
    
def lista():
    angajati_list.delete(0,END)
    for row in db.fetch():
        angajati_list.insert(END,row)

def adaugare_angajat():
    cifre=re.search('[0-9]', CnP_text.get())
    litere=re.search('[a-zA-Z]', CnP_text.get())
    simbol=re.search('[!@#$%^&*(),.?":{}|<>]', CnP_text.get())
    cifre1=re.search('[0-9]', nume_text.get())
    litere1=re.search('[a-zA-Z]', nume_text.get())
    simbol1=re.search('[!@#$%^&*(),.?":{}|<>]', nume_text.get())
    cifre2=re.search('[0,9]', salariu_text.get())
    litere2=re.search('[a-zA-Z]', salariu_text.get())
    simbol2=re.search('[!@#$%^&*(),?":{}|<>]', salariu_text.get())

    for i in range(len(CnP_text.get())):
        for j in range(len(nume_text.get())):
            for k in range(len(salariu_text.get())):
                if litere or simbol:
                    litere==True 
                    simbol==True
                    messagebox.showinfo("Eroare", "CNP-ul nu poate contine litere sau simboluri!")
                    return
                elif cifre1 or simbol1:
                    cifre1==True 
                    simbol1==True
                    messagebox.showinfo("Eroare", "Numele nu poate contine cifre sau simboluri!")
                    return
                elif litere2 or simbol2:
                    litere2==True 
                    messagebox.showinfo("Eroare", "Salariul nu poate contine litere sau simboluri!")
                    return
                elif cifre and len(str(CnP_text.get()))==13:
                    cifre==True
                    db.insert(nume_text.get(),CnP_text.get(),salariu_text.get())
                    angajati_list.delete(0,END)
                    angajati_list.insert(END,(nume_text.get(),CnP_text.get(),salariu_text.get()))
                    clear_text()
                    lista()
                    break
                elif len(str(CnP_text.get()))!=13:
                    messagebox.showinfo("Eroare", "CNP-ul nu are 13 caractere!")
                    return


def sterge_angajat():
    db.remove(item_selectat[0])
    clear_text()
    lista()


def modifica_angajat():
    cifre=re.search('[0-9]', CnP_text.get())
    litere=re.search('[a-zA-Z]', CnP_text.get())
    simbol=re.search('[!@#$%^&*(),.?":{}|<>]', CnP_text.get())
    cifre1=re.search('[0-9]', nume_text.get())
    litere1=re.search('[a-zA-Z]', nume_text.get())
    simbol1=re.search('[!@#$%^&*(),.?":{}|<>]', nume_text.get())
    cifre2=re.search('[0,9]', salariu_text.get())
    litere2=re.search('[a-zA-Z]', salariu_text.get())
    simbol2=re.search('[!@#$%^&*(),?":{}|<>]', salariu_text.get())
    
    for i in range(len(CnP_text.get())):
        for j in range(len(nume_text.get())):
            for k in range(len(salariu_text.get())):
                if litere or simbol:
                    litere==True 
                    simbol==True
                    messagebox.showinfo("Eroare", "CNP-ul nu poate contine litere sau simboluri!")
                    return 
                
                elif cifre1 or simbol1:
                    cifre1==True 
                    simbol1==True
                    messagebox.showinfo("Eroare", "Numele nu poate contine cifre sau simboluri!")
                    return
                
                elif litere2 or simbol2:
                    litere2==True 
                    messagebox.showinfo("Eroare", "Salariul nu poate contine litere sau simboluri!")
                    return
                
                elif cifre and len(str(CnP_text.get()))==13:
                    cifre==True
                    db.update(item_selectat[0],nume_text.get(),CnP_text.get(),salariu_text.get())
                    lista()
                    break
                elif len(str(CnP_text.get()))!=13:
                    messagebox.showinfo("Eroare", "CNP-ul nu are 13 caractere!")
                    return
    


def salariu_angajat():
    a=float(salariu_text.get())
    a=a-a*0.05
    db.update(item_selectat[0],nume_text.get(),CnP_text.get(),a)
    lista()
    
    


def clear_text():
    nume_entry.delete(0,END)
    CnP_entry.delete(0,END)
    salariu_entry.delete(0,END)

proiect=Tk()
#Fereastra
proiect.title("GESTIONRAE ANGAJATI")
proiect.geometry("800x400")

#Nume
nume_text=StringVar()
nume_label=Label(proiect,text="Nume",font=("bold",10), pady=20)
nume_label.grid(row=0,column=0,sticky=W)
nume_entry=Entry(proiect,textvariable=nume_text)
nume_entry.grid(row=0,column=1)

#CnP
CnP_text=StringVar()
CnP_label=Label(proiect,text="CNP",font=("bold",10), pady=20)
CnP_label.grid(row=0,column=2,sticky=W)
CnP_entry=Entry(proiect,textvariable=CnP_text)
CnP_entry.grid(row=0,column=3)

#Salariu
salariu_text=StringVar()
salariu_label=Label(proiect,text="Salariu",font=("bold",10), pady=20)
salariu_label.grid(row=1,column=0,sticky=W)
salariu_entry=Entry(proiect,textvariable=salariu_text)
salariu_entry.grid(row=1,column=1)

#Lista Angajati

angajati_list=Listbox(proiect, height=12,width=60,border=0)
angajati_list.grid(row=3,column=0,columnspan=3,rowspan=6,pady=20,padx=20)

#Creare scrollbar
scrollbar=Scrollbar(proiect)
scrollbar.grid(row=3,column=3)

#Scrollbar la lista
angajati_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=angajati_list.yview)

#Selectare linie
angajati_list.bind("<<ListboxSelect>>",selecteaza)


#Butoane

adaugare_btn=Button(proiect,text="Adaugare Angajat",width=14,command=adaugare_angajat)
adaugare_btn.grid(row=2,column=0)

sterge_btn=Button(proiect,text="Sterge Angajat",width=14,command=sterge_angajat)
sterge_btn.grid(row=2,column=1)

modifica_btn=Button(proiect,text="Modifica Angajat",width=14,command=modifica_angajat)
modifica_btn.grid(row=2,column=2)

sterge_btn=Button(proiect,text="Salariu Angajat",width=14,command=salariu_angajat)
sterge_btn.grid(row=2,column=3)

#Lista
lista()

proiect.mainloop()
