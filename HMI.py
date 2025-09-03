from PyQt5.QtWidgets import QApplication

class HMI():
    def __init__(self):
        self.app = QApplication([])
        from GUI.Login import Login
        self.login = Login()
        
        self.app.exec_()