import sqlite3 as sql


class TransactionObject:
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        self.conn = sql.connect(self.database)
        self.cur = self.conn.cursor()
        self.connected = True

    def disconnect(self):
        self.conn.close()
        self.connected = False

    def execute(self, sql, parms=None):
        if self.connected:
            if parms == None:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return self.cur.fetchall()

    def persist(self):
        self.conn.commit()

    def close(self):
        if self.connected:
            self.conn.commit()
            return True
        else:
            return False

def initBD():
    transaction = TransactionObject()
    transaction.connect()
    transaction.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
    transaction.persist()
    transaction.disconnect()

def insert(nome, sobrenome, email, cpf):
    transaction = TransactionObject()
    transaction.connect()
    transaction.execute("INSERT INTO clientes (nome, sobrenome, email, cpf) VALUES (?, ?, ?, ?)",(nome, sobrenome, email, cpf))
    transaction.persist()
    transaction.disconnect()

def view():
    transaction = TransactionObject()
    transaction.connect()
    transaction.execute("SELECT * FROM clientes")
    rows = transaction.fetchall()
    transaction.disconnect()
    return rows

def search(nome="", sobrenome="", email="", cpf=""):
    transaction = TransactionObject()
    transaction.connect()
    transaction.execute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=?",(nome, sobrenome, email, cpf))
    rows = transaction.fetchall()
    transaction.disconnect()
    return rows

def delete(id):
    transaction = TransactionObject()
    transaction.connect()
    transaction.execute("DELETE FROM clientes WHERE id=?", (id,))
    transaction.persist()
    transaction.disconnect()

def update(id, nome, sobrenome, email, cpf):
    transaction = TransactionObject()
    transaction.connect()
    transaction.execute("UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?", (nome, sobrenome, email, cpf, id))
    transaction.persist()

initBD()
