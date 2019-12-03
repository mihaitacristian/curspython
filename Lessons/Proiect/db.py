import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS angajati (id INTEGER PRIMARY KEY,nume text, CnP text, salariu integer)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM angajati")
        rows = self.cur.fetchall()
        return rows

    def insert(self,nume, CnP, salariu):
        self.cur.execute("INSERT INTO angajati VALUES (NULL,?,?,?)",
                         (nume, CnP, salariu))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM angajati WHERE id=?", (id,))
        self.conn.commit()

    def update(self,id,nume,CnP,salariu):
        self.cur.execute("UPDATE angajati SET nume=?, CnP=?, salariu=? WHERE id=?",
                         (nume,CnP,salariu,id))
        self.conn.commit()
                          
    def __del__(self):
        self.conn.close()


#db = Database('store.db')
#db.insert("Ion Fieraru","19712181520","100")
#db.insert("Vasile Franaru","19712181521","200")
#db.insert("Doru Motoru", "19712181522", "300")
