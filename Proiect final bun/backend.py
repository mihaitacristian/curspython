import sqlite3

def connect():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    print("Successfully Connected to database")
    cur.execute("CREATE TABLE IF NOT EXISTs database (id INTEGER PRIMARY KEY, name TEXT ,cnp INTEGER, salariu INTEGER)")
    conn.commit()
    conn.close()

def insert(name,cnp,salariu):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO database VALUES (NULL, ?,?,?)",(name,cnp,salariu))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor() 
    cur.execute("SELECT * FROM database")
    row=cur.fetchall()
    conn.close()
    return row 

def search(name="",cnp="",salariu=""):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM database WHERE name=? or cnp = ? or salariu = ?",(name,cnp,salariu))
    row=cur.fetchall()
    conn.close()
    return row

def delete(id):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()    
    cur.execute("DELETE FROM database where id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,cnp,salariu):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("UPDATE DATABASE SET name=?,cnp =?, salariu =? where id=?",(name,cnp,salariu,id))
    conn.commit()
    conn.close()

# def update_salariu(id,name,salariu):
#     conn=sqlite3.connect("database.db")
#     cur=conn.cursor()
#     cur.execute("UPDATE DATABASE SET name=?, or salariu = ? where id=?",(name,salariu,id))
#     conn.commit()
#     conn.close()

# def salariu(salariu):
#     db.execute("SELECT * from  angajat")
#     data = db.fetchall()
#     for i in data:
#             salariu=float(i[2])
#             salariuSarakit= salariu - (salariu * 0.05)
#             db.execute("UPDATE angajat SET salariu=? WHERE cnp=?",
#                       (str(round(salariuSarakit,2)), i[1]))
#             conn.commit()
#             refresh_listbox()

connect()
