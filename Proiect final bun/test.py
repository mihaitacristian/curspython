import sqlite3
import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox

##########################################################################################################
#############################             DB part              ###########################################
##########################################################################################################

## Conexiunea cu baza de date
conn = sqlite3.connect('proiect.db')
print("Opened database successfully")

## Verificam daca tabela exista deja
db = conn.cursor()
creaza_db=('''CREATE TABLE IF NOT EXISTS angajat
         (nume           TEXT    NOT NULL,
         cnp           TEXT     NOT NULL UNIQUE,
         salariu         REAL   NOT NULL);''')

db.execute(creaza_db)



##########################################################################################################
#############################            Interface part        ###########################################
##########################################################################################################
w = tk.Tk()
w.title("Proiect Despa Florin-Mircea")
w.geometry("300x300")


###########  Validari
def cnp_este_unic(field):
    db.execute("SELECT nume FROM angajat WHERE cnp=?", [field])
    cnp_unic = db.fetchone()
    if cnp_unic == None:
        return(True)
    else:
        return(False)

def salariu_is_float(field):
    result = False
    if field.count(".") == 1:
        if field.replace(".", "").isdigit():
            result = True
    return result

def valideaza_nume(field):
    if not field:
        messagebox.showinfo("Eroare", "Numele nu poate sa fie blank")
        return FALSE
    else:
        if field.isalpha():
            return True
        else:
            messagebox.showinfo("Eroare", "Numele trebuie sa contina doar litere")
            return False

def valideaza_cnp(field):
    if not field:
        messagebox.showinfo("Eroare", "CNP-ul nu poate sa fie blank")
        return FALSE
    else:
        if len(field) != 13:
            messagebox.showinfo("Eroare", "CNP-ul trebuie sa contina 13 cifre")
            return FALSE
        else:
            if field.isdigit() == False:
                messagebox.showinfo("Eroare", "CNP-ul trebuie sa contina doar cifre")
                return False
            else:
                if cnp_este_unic(field) == True:
                    return(True)
                else:
                    messagebox.showinfo("Eroare", "CNP-ul exista deja in baza de date")
                    return(False)


def valideaza_salariu(field):
    if not field:
        messagebox.showinfo("Eroare", "Salariul nu poate sa fie blank")
        return FALSE
    else:
        if salariu_is_float(field) == False:
            messagebox.showinfo("Eroare", "Salariul este scris incorect - trebuie sa fie sub forma de xxx.yy")
            return False
        else:
            if float(field)<1:
                messagebox.showinfo("Eroare", "Angajatul trebuie sa castige cel putin 1 leu #sarakie")
            else:
                return True


def valideaza_fielduri(nume,cnp,salariu):
    if valideaza_nume(nume) == True:
        if valideaza_cnp(cnp) == True:
            if valideaza_salariu(salariu) == True:
                return True
            else:
                return False

def adauga_in_db(nume,cnp,salariu):
    if valideaza_fielduri(nume,cnp,salariu):
        db.execute("INSERT INTO angajat VALUES (?,?,?)",
                   (nume, cnp, salariu))
        conn.commit()
        messagebox.showinfo("OK", "Angajatul a fost adaugat cu success")\







################################ functii


def listare_angajati():
    w0 = tk.Toplevel()
    w0.geometry("600x600")
    w0.resizable(0, 0)
    w0.wm_title("Listare angajati")
    lista_angajati(w0)
    inchide_fereastra = Button(w0, text="OK", command=w0.destroy)
    inchide_fereastra.place(x=10, y=50)

def adaugare_angajat():
    w1 = tk.Toplevel()
    w1.geometry("500x300")
    w1.resizable(0, 0)
    w1.wm_title("Adaugare angajat")
    ## definim variabelele
    nume = StringVar (w1)
    cnp = StringVar (w1)
    salariu = StringVar (w1)
    ###
    ## definim labels
    L1 = Label(w1, text = "Numele angajatului:", font=("arial", 16)).place(x=10,y=10)
    L2 = Label(w1, text = "CNP:", font=("arial", 16)).place(x=10,y=50)
    L3 = Label(w1, text="Salariu:", font=("arial", 16)).place(x=10, y=100)
    ##
    ## definim input boxes
    numeBox = Entry(w1, textvariable=nume)
    numeBox.place(x=200, y=15)
    cnpBox = Entry(w1, textvariable=cnp)
    cnpBox.place(x=200, y=55)
    salariuBox = Entry(w1, textvariable=salariu)
    salariuBox.place(x=200, y=105)
    inchide_fereastra = Button(w1, text="Inchide", command=w1.destroy)
    inchide_fereastra.place(x=200, y=200)
    adauga = Button(w1, text="Adauga", command= lambda : adauga_in_db(nume.get(),cnp.get(),salariu.get()))
    adauga.place(x=100,y=200)



def modifica_angajat():
    w2 = tk.Toplevel()
    w2.geometry("800x800")
    w2.resizable(0, 0)
    w2.wm_title("Modifica angajat")
    lista_angajati(w2)

def stergere_angajat():
    w3 = tk.Toplevel()
    w3.geometry("800x800")
    w3.resizable(0, 0)
    w3.wm_title("Stergere angajat")
    lista_angajati(w3)

def lista_angajati(field):
    db.execute("SELECT * from  angajat")
    Lb = Listbox(field, height=8, width=40, font=("arial", 12))
    Lb.pack(side=RIGHT, fill=Y)
    scroll = Scrollbar(field, orient=VERTICAL)  # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command=Lb.yview)
    scroll.pack(side=RIGHT, fill=Y)
    Lb.config(yscrollcommand=scroll.set)
    data = db.fetchall()
    print(data)
    Lb.insert(0, 'Nume, CNP, Salariu') #first row in listbox
    for row in data:
        Lb.insert(1,row)  # Inserts record row by row in list box


##########################################################################################################
#############################           Adaugare angajat       ###########################################
##########################################################################################################



b1 = Button(w, text = "Listare angajat", command = listare_angajati)
b1.place(x=10,y=10)

b2 = Button(w, text = "Adaugare angajat", command = adaugare_angajat)
b2.place(x=10,y=50)

b3 = Button(w, text = "Modifica angajat", command = modifica_angajat)
b3.place(x=10,y=90)

b4 = Button(w, text = "Sterge angajat", command = stergere_angajat)
b4.place(x=10,y=130)



w.resizable(0, 0)
# Code to add widgets will go here...
w.mainloop()