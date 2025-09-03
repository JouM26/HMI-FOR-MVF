import sqlite3

class Conexion():
    def __init__(self):
        try:
            self.connection = sqlite3.connect('registro.db')
            self.creartablas()
        except Exception as ex:
            print(ex)

    def creartablas(self):
        sql_create_table1 = """CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nombre TEXT,
                                apellido TEXT,
                                email TEXT UNIQUE,
                                usuario TEXT UNIQUE,
                                password TEXT)"""
        cur = self.connection.cursor()  # Corregido: self.connection
        cur.execute(sql_create_table1)
        cur.close()
        self.crearAdmin()

    def crearAdmin(self):
        try:  # Corregido: dos puntos
            sql_insert = """INSERT OR IGNORE INTO usuarios values(null,'{}','{}','{}','{}','{}')""".format(
                'Joe', 'Medina', 'puebatesis2025@gmail.com', 'JOU', '12345')
            cur = self.connection.cursor()
            cur.execute(sql_insert)
            self.connection.commit()
        except Exception as ex:
            print(ex)

con = Conexion()