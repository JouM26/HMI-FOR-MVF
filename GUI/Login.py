from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox

class Login():
    def __init__(self):
        self.login = uic.loadUi("GUI/Login.ui")
        self.login.show()
