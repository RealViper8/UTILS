

try:
    import sqlite3
except ModuleNotFoundError as E:
    print("\n"+str(E)+"\n")

class database:
    def __init__(self,name : str | None="database.db",path : str | None="") -> None:
        if path != "":
            name = name+"\\"+path
        self.conn = sqlite3.Connection(name)
        self.c = self.conn.cursor()
    def get_all(self,table):
        self.c.execute("SELECT * FROM "+table)
        return self.c.fetchall()
    def get_type(self,table,type):
        self.c.execute("SELECT * FROM {} WHERE type='{}'".format(table,type))
        return self.c.fetchall()
    def get_name(self,table,name):
        self.c.execute("SELECT {} FROM {}".format(name,table))
        return self.c.fetchall()
    def push_table(self,table,vars : str | None="age INTEGER, name TEXT"):
        self.c.execute("CREATE TABLE IF NOT EXISTS {}({})".format(table,vars))
    def exit(self):
        self.c.close()
        self.conn.close()
        print("Database closed")