import sqlite3
from tkinter import messagebox

def connect():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    print("Successfully Connected to database")
    cur.execute("CREATE TABLE IF NOT EXISTs database (id INTEGER PRIMARY KEY, name TEXT ,cnp INTEGER, salariu FLOAT)")
    conn.commit()
    conn.close()

def insert(name,cnp,salariu):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    # from backend import valideaza_cnp
    # from backend import valideaza_nume
    # from backend import valideaza_salariu
    # from backend import valideaza_fielduri
    # if valideaza_fielduri(nume,cnp,salariu):
    cur.execute("INSERT INTO database VALUES (NULL, ?,?,?)",(name,cnp,salariu))
    conn.commit()
    messagebox.showinfo("Angajatul a fost adaugat cu success")
    conn.close()
    view()

def view():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor() 
    cur.execute("SELECT * FROM database")
    row=cur.fetchall()
    conn.close()
    return row 

def delete(id):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()    
    cur.execute("DELETE FROM database where id=?",(id,))
    conn.commit()
    conn.close()

def update_angajat(id,name,cnp):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("UPDATE DATABASE SET name=?,cnp =?  where id=?",(name,cnp,id))
    conn.commit()
    conn.close()

def update_salariu(id,name,salariu):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("UPDATE DATABASE SET name=?, salariu = ? where id=?",(name,salariu,id))
    conn.commit()
    conn.close()

def salariu_redus():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * from  database")
    row = cur.fetchall()
    for i in row:
            salariu=i[3]
            salariuredus= salariu - (salariu * 0.05)
            cur.execute("UPDATE database SET salariu=? WHERE id=?",
                      (round(salariuredus,2), i[0]))

            print(salariu, salariuredus)

   
    conn.commit()  
    conn.close()
    

# def cnp_este_unic(field):
#     conn=sqlite3.connect("database.db")
#     cur=conn.cursor()
#     cur.execute("SELECT nume FROM angajat WHERE cnp=?", [field])
#     cnp_unic = cur.fetchone()
#     if cnp_unic == None:
#         return(True)
#     else:
#         return(False)

# def salariu_is_float(field):
#     result = False
#     if field.count(".") == 1:
#         if field.replace(".", "").isdigit():
#             result = True
#     return result

# def valideaza_nume(field):
#     contine_litera=0
#     nume_valid=True
#     if not field:
#         messagebox.showinfo("Eroare", "Numele nu poate sa fie blank")
#         return FALSE
#     else:
#         for x in field:
#             if x.isalpha():
#                 contine_litera += 1
#             elif (x == " ") or (x == "-"):
#                     continue
#             else:
#                 messagebox.showinfo("Eroare", "Numele poate sa contina doar litere,spatii sau caracterul -")
#                 return False
#         if nume_valid:
#             if contine_litera>0:
#                 return True
#             else:
#                 messagebox.showinfo("Eroare", "Numele trebuie sa contina si litere")
#                 return False




# def valideaza_cnp(field):
#     if not field:
#         messagebox.showinfo("Eroare", "CNP-ul nu poate sa fie blank")
#         return FALSE
#     else:
#         if len(field) != 13:
#             messagebox.showinfo("Eroare", "CNP-ul trebuie sa contina 13 cifre")
#             return FALSE
#         else:
#             if field.isdigit() == False:
#                 messagebox.showinfo("Eroare", "CNP-ul trebuie sa contina doar cifre")
#                 return False
#             else:
#                 if cnp_este_unic(field) == True:
#                     return(True)
#                 else:
#                     messagebox.showinfo("Eroare", "CNP-ul exista deja in baza de date")
#                     return(False)


# def valideaza_salariu(field):
#     if not field:
#         messagebox.showinfo("Eroare", "Salariul nu poate sa fie blank")
#         return FALSE

# def valideaza_fielduri(nume,cnp,salariu):
#     if valideaza_nume(nume) == True:
#         if valideaza_cnp(cnp) == True:
#             if valideaza_salariu(salariu) == True:
#                 return True
#             else:
#                 return False

connect()
