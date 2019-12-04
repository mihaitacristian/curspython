import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox

##########################################################################################################
#############################             DB part              ###########################################
##########################################################################################################

## Conexiunea cu baza de date
conn = sqlite3.connect('myProject.db')
print("Opened database successfully")

## Verificam daca tabela exista deja
db = conn.cursor()
creaza_db=('''CREATE TABLE IF NOT EXISTS angajat
         (nume           TEXT    NOT NULL,
         cnp           TEXT     NOT NULL UNIQUE,
         salariu         REAL   NOT NULL);''')

db.execute(creaza_db)

##########################################################################################################
#############################             Validari             ###########################################
##########################################################################################################


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
    contine_litera=0
    nume_valid=True
    if not field:
        messagebox.showinfo("Eroare", "Numele nu poate sa fie blank")
        return FALSE
    else:
        for x in field:
            if x.isalpha():
                contine_litera += 1
            elif (x == " ") or (x == "-"):
                    continue
            else:
                messagebox.showinfo("Eroare", "Numele poate sa contina doar litere,spatii sau caracterul -")
                return False
        if nume_valid:
            if contine_litera>0:
                return True
            else:
                messagebox.showinfo("Eroare", "Numele trebuie sa contina si litere")
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
            if float(field)<1000:
                messagebox.showinfo("Eroare", "Angajatul trebuie sa castige cel putin 1000 lei #sarakie")
            else:
                return True


def valideaza_fielduri(nume,cnp,salariu):
    if valideaza_nume(nume) == True:
        if valideaza_cnp(cnp) == True:
            if valideaza_salariu(salariu) == True:
                return True
            else:
                return False

##########################################################################################################
#############################             Operations           ###########################################
##########################################################################################################
def refresh_listbox():
    db.execute("SELECT * from  angajat")
    data = db.fetchall()
    Lb.delete(0,END)
    for row in data:
        Lb.insert(0,row)  # Inserts record row by row in list box


def listare_angajati():
    w0 = tk.Toplevel()
    w0.geometry("600x600")
    w0.resizable(0, 0)
    w0.grab_set()
    w0.wm_title("Listare angajati")
    db.execute("SELECT * from  angajat")
    angajati = Listbox(w0, height=8, width=40, font=("arial", 12))
    angajati.pack(side=RIGHT, fill=Y)
    scroll = Scrollbar(w0, orient=VERTICAL)
    scroll.config(command=angajati.yview)
    scroll.pack(side=RIGHT, fill=Y)
    angajati.config(yscrollcommand=scroll.set)
    data = db.fetchall()
    for row in data:
        angajati.insert(0, row)
    inchide_fereastra = Button(w0, text="Inchide", command=w0.destroy)
    inchide_fereastra.place(x=50, y=50)


def adauga_in_db(nume,cnp,salariu):
    if valideaza_fielduri(nume,cnp,salariu):
        db.execute("INSERT INTO angajat VALUES (?,?,?)",
                   (nume, cnp, salariu))
        conn.commit()
        messagebox.showinfo("OK", "Angajatul a fost adaugat cu success")
        refresh_listbox()

def modifica_angajat_in_db(nume,cnp):
    if cnp_este_unic(cnp): ## Daca CNP-ul este UNIC inseamna ca angajatul nu exista in DB
        messagebox.showinfo("Eroare", "Angajatul nu exista in baza de date")
    elif valideaza_nume(nume): ## Validam ca noul nume selectat  respecta cerintele
        db.execute("UPDATE angajat SET nume=? WHERE cnp=?",
                   (nume,cnp))
        conn.commit()
        refresh_listbox()

def modificare_salariu_in_db(cnp,salariu):
    if cnp_este_unic(cnp): ## Daca CNP-ul este UNIC inseamna ca angajatul nu exista in DB
        messagebox.showinfo("Eroare", "Angajatul nu exista in baza de date")
    elif valideaza_salariu(salariu):
        db.execute("UPDATE angajat SET salariu=? WHERE cnp=?",
                   (salariu,cnp))
        conn.commit()
        refresh_listbox()

def sarakie():
    db.execute("SELECT * from  angajat")
    data = db.fetchall()
    for i in data:
            salariu=float(i[2])
            salariuSarakit= salariu - (salariu * 0.05)
            db.execute("UPDATE angajat SET salariu=? WHERE cnp=?",
                      (str(round(salariuSarakit,2)), i[1]))
            conn.commit()
            refresh_listbox()

def sterge_angajat(cnp):
    if cnp_este_unic(cnp): ## Daca CNP-ul este UNIC inseamna ca angajatul nu exista in DB
        messagebox.showinfo("Eroare", "Angajatul nu exista in baza de date")
    else:
        db.execute("DELETE from angajat WHERE cnp=?",
                   (cnp,))
        conn.commit()
        refresh_listbox()

def on_select(event):
    index = Lb.curselection()
    if index:
        numeBox.delete(0,END)
        cnpBox.delete(0,END)
        salariuBox.delete(0,END)
        valori=Lb.get(index)
        numeBox.insert(0,valori[0])
        cnpBox.insert(0,valori[1])
        salariuBox.insert(0,valori[2])


##########################################################################################################
#############################             Interfata            ###########################################
##########################################################################################################

w = tk.Tk()
w.title("Proiect Despa Florin-Mircea")
w.geometry("800x400")


###### Listbox ######
Lb = Listbox(w, height=8, width=40, font=("arial", 12))
Lb.pack(side=RIGHT, fill=Y)
scroll = Scrollbar(w, orient=VERTICAL)
scroll.config(command=Lb.yview)
scroll.pack(side=RIGHT, fill=Y)
Lb.config(yscrollcommand=scroll.set)
refresh_listbox()
###########################

#### Boxuri #######

nume = StringVar(w)
cnp = StringVar(w)
salariu = StringVar(w)
###
## definim labels
L1 = Label(w, text="Numele angajatului:", font=("arial", 16)).place(x=10, y=10)
L2 = Label(w, text="CNP:", font=("arial", 16)).place(x=10, y=50)
L3 = Label(w, text="Salariu:", font=("arial", 16)).place(x=10, y=100)
##
## definim input boxes
numeBox = Entry(w, textvariable=nume)
numeBox.place(x=200, y=15)
cnpBox = Entry(w, textvariable=cnp)
cnpBox.place(x=200, y=55)
salariuBox = Entry(w, textvariable=salariu)
salariuBox.place(x=200, y=105)



## Butoanele pe main interface


adauga = Button(w, text="Adauga angajat", command=lambda: adauga_in_db(nume.get(), cnp.get(), salariu.get()))
adauga.place(x=10, y=200)

listare = Button(w, text="Listare angajati", command=lambda: listare_angajati())
listare.place(x=10, y=250)

modifica_detalii = Button(w, text="Modifica numele angajatului", command=lambda: modifica_angajat_in_db(nume.get(), cnp.get()))
modifica_detalii.place(x=130, y=200)

modifica_salariu = Button(w, text="Modifica salariul angajatului", command=lambda: modificare_salariu_in_db(cnp.get(), salariu.get()))
modifica_salariu.place(x=130, y=250)

micsorare_salariu = Button(w, text="#Sarakie -5%", command=lambda: sarakie())
micsorare_salariu.place(x=320, y=200)

sterge = Button(w, text="Stergere angajat", command=lambda: sterge_angajat(cnp.get()))
sterge.place(x=320, y=250)

inchide_fereastra = Button(w, text="Inchide", command=w.destroy)
inchide_fereastra.place(x=350, y=350)

Lb.bind("<<ListboxSelect>>", on_select)

w.resizable(0, 0)
w.mainloop()