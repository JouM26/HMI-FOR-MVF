from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox
from data.usuario import UsuarioData

class RecuperarContrasena(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("GUI/RecuperarContrasena.ui", self)
        self.ui.btnRecuperar.clicked.connect(self.recuperar)

    def recuperar(self):
        email = self.ui.txtCorreo.text()
        if email:
            usuData = UsuarioData()
            if usuData.enviar_enlace_recuperacion(email):
                QMessageBox.information(self, "Recuperación", "Se envió un enlace de recuperación a tu correo.")
                self.accept()
            else:
                QMessageBox.warning(self, "Error", "Correo no registrado.")
        else:
            QMessageBox.warning(self, "Error", "Ingrese su correo.")