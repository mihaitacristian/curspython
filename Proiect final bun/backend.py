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
    



connect()
