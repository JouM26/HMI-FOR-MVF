from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox
from GUI.ventanas_secundarias import VentanaDetalle, VentanaControlManual, VentanaInicio, VentanaPruebasManuales

class MainWindow:
    def __init__(self, nombre="", apellido="", usuario=""):
        self.main = uic.loadUi("GUI/main.ui")
        self.initGUI(nombre, apellido, usuario)
        self.main.show()

    def initGUI(self, nombre, apellido, usuario):
        # Mostrar identificación
        self.main.txtIdentificacion.setText(f"{nombre} {apellido} [{usuario}]")

        # Conectar botones a sus funciones
        self.main.btnDetalle.clicked.connect(self.abrir_detalle)
        self.main.btnControl_Manual.clicked.connect(self.abrir_control_manual)
        self.main.btnInicio.clicked.connect(self.abrir_inicio)
        self.main.btnSalir.clicked.connect(self.salir_usuario)  # <--- Aquí

        # Inicializar luces indicadoras en rojo (apagadas)
        self.set_led_color(self.main.lblIndicadorMaquina, False)
        self.set_led_color(self.main.lblIndicadorModulo, False)

        # Ejemplo: Cambiar color de los indicadores (simula señal de sensores)
        # self.set_led_color(self.main.lblIndicadorMaquina, True)   # Verde
        # self.set_led_color(self.main.lblIndicadorModulo, False)   # Rojo

    def set_led_color(self, label, activo):
        if activo:
            # Verde
            label.setStyleSheet("""
                background-color: #4cc417;
                border-radius: 10px;
                min-width: 20px;
                min-height: 20px;
                max-width: 20px;
                max-height: 20px;
                border: 2px solid #333;
            """)
        else:
            # Rojo
            label.setStyleSheet("""
                background-color: #e74c3c;
                border-radius: 10px;
                min-width: 20px;
                min-height: 20px;
                max-width: 20px;
                max-height: 20px;
                border: 2px solid #333;
            """)

    def abrir_detalle(self):
        self.ventana_detalle = VentanaDetalle(self.main)
        self.main.hide()
        self.ventana_detalle.show()

    def abrir_control_manual(self):
        self.ventana_control_manual = VentanaControlManual(self.main)
        self.main.hide()
        self.ventana_control_manual.show()

    def abrir_inicio(self):
        dlg = VentanaInicio(self.main)
        dlg.exec_()

    def prueba_manual(self):
        self.ventana_pruebas = VentanaPruebasManuales(self)
        self.hide()
        self.ventana_pruebas.show()

    def salir_usuario(self):
        from GUI.Login import Login  # Importa aquí, no arriba
        self.main.close()
        self.login = Login()

