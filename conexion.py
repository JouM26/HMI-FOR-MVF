# -*- coding: utf-8 -*-
import sqlite3

class Conexion:
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
                                clave TEXT)"""
        cur = self.connection.cursor()
        cur.execute(sql_create_table1)
        cur.close()
        self.crearAdmin()

    def crearAdmin(self):
        try:
            sql_insert = """INSERT OR IGNORE INTO usuarios VALUES (null,?,?,?,?,?)"""
            cur = self.connection.cursor()
            cur.execute(sql_insert, ('Joe', 'Medina', 'pruebatesis2025@gmail.com', 'JOU', '12345'))
            self.connection.commit()
            cur.close()
        except Exception as ex:
            print(ex)

    def conectar(self):
        return self.connection

con = Conexion()