# -*- coding: utf-8 -*-
from PyQt5 import uic
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from GUI.main import MainWindow
from data.usuario import UsuarioData
from model.user import Usuario
from GUI.RecuperarContrasena import RecuperarContrasena

class Login:
    def __init__(self):
        self.ui = uic.loadUi("GUI/Login.ui")
        self.initGUI()
        self.ui.lblMensaje.setText("")
        self.ui.show()

    def ingresar(self):
        if len(self.ui.txtUsuario.text()) < 2:
            self.ui.lblMensaje.setText("Por favor ingrese usuario valido")
            self.ui.txtUsuario.setFocus()
        elif len(self.ui.txtClave.text()) < 3:
            self.ui.lblMensaje.setText("Por favor ingrese contraseña valida")
            self.ui.txtClave.setFocus()
        else:
            self.ui.lblMensaje.setText("")
            usu = Usuario(usuario=self.ui.txtUsuario.text(), clave=self.ui.txtClave.text())
            usuData = UsuarioData()
            res = usuData.login(usu)
            if res:
                # Pasa los datos del usuario a la ventana principal
                self.main = MainWindow(res._nombre, res._apellido, res._usuario)
                self.ui.hide()
            else:
                self.ui.lblMensaje.setText("Usuario o contraseña incorrectos")

    def restablecer_contrasena(self):
        dlg = RecuperarContrasena()
        dlg.exec_()

    def initGUI(self):
        self.ui.btnAcceder.clicked.connect(self.ingresar)
        self.ui.btnRestablecer.clicked.connect(self.restablecer_contrasena)
