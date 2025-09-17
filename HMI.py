# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
from GUI.Login import Login

class HMI:
    def __init__(self):
        self.app = QApplication([])
        self.login = Login()
        self.app.exec()