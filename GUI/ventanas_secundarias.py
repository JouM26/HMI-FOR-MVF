from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout

class VentanaDetalle(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Detalle")
        btn = QPushButton("Regresar")
        btn.clicked.connect(self.close)
        layout = QVBoxLayout()
        layout.addWidget(btn)
        self.setLayout(layout)

class VentanaControlManual(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Control Manual")
        btn = QPushButton("Regresar")
        btn.clicked.connect(self.close)
        layout = QVBoxLayout()
        layout.addWidget(btn)
        self.setLayout(layout)

class VentanaInicio(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Inicio")
        btn = QPushButton("Regresar")
        btn.clicked.connect(self.close)
        layout = QVBoxLayout()
        layout.addWidget(btn)
        self.setLayout(layout)