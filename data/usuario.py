# -*- coding: utf-8 -*-
import conexion
from model.user import Usuario
import smtplib
from email.mime.text import MIMEText

class UsuarioData:
    def __init__(self):
        self.db = conexion.con.conectar()
        self.cursor = self.db.cursor()

    def login(self, usuario: Usuario):
        query = "SELECT * FROM usuarios WHERE usuario=? AND clave=?"
        self.cursor.execute(query, (usuario._usuario, usuario._clave))
        fila = self.cursor.fetchone()
        self.cursor.close()
        if fila:
            return Usuario(nombre=fila[1], apellido=fila[2], email=fila[3], usuario=fila[4], clave=fila[5])
        else:
            return None

    def enviar_enlace_recuperacion(self, email):
        query = "SELECT usuario FROM usuarios WHERE email=?"
        cursor = self.db.cursor()
        cursor.execute(query, (email,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            usuario = fila[0]
            token = usuario + "_token"
            # Aquí puedes guardar el token en memoria o en la base de datos
            enlace = f"http://localhost:5000/reset?token={token}"
            msg = MIMEText(
                f"Haz clic en este enlace para restablecer tu contraseña:\n\n{enlace}\n\nSi no solicitaste este cambio, ignora este mensaje."
            )
            msg["Subject"] = "Recuperación de contraseña HMI"
            msg["From"] = "pruebatesis2025@gmail.com"
            msg["To"] = email

            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login("pruebatesis2025@gmail.com", "mqof mmjq dqdw rjvu")
                    server.sendmail("pruebatesis2025@gmail.com", [email], msg.as_string())
                return True
            except Exception as e:
                print(e)
                return False
        else:
            return False
