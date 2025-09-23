from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLabel, QProgressBar
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

class VentanaDetalle(QDialog):
    def __init__(self, ventana_anterior=None):
        super().__init__()
        self.ventana_anterior = ventana_anterior
        self.ui = uic.loadUi("GUI/Detalle.ui", self)
        self.ui.btnVolver.clicked.connect(self.volver)
        # Inicializa todas las luces en rojo
        self.set_led_color(self.ui.lblCamara, False)
        self.set_led_color(self.ui.lblSensor1, False)
        self.set_led_color(self.ui.lblSensor2, False)
        self.set_led_color(self.ui.lblMotor1, False)
        self.set_led_color(self.ui.lblMotor2, False)
        self.set_led_color(self.ui.lblMotor3, False)

    def set_led_color(self, label, activo):
        if activo:
            label.setStyleSheet("""
                background-color: #4cc417;
                border-radius: 7px;
                min-width: 14px;
                min-height: 14px;
                max-width: 14px;
                max-height: 14px;
                border: 1px solid #333;
            """)
        else:
            label.setStyleSheet("""
                background-color: #e74c3c;
                border-radius: 7px;
                min-width: 14px;
                min-height: 14px;
                max-width: 14px;
                max-height: 14px;
                border: 1px solid #333;
            """)

    def volver(self):
        self.close()
        if self.ventana_anterior:
            self.ventana_anterior.show()

class VentanaControlManual(QDialog):
    def __init__(self, ventana_anterior=None):
        super().__init__()
        self.ventana_anterior = ventana_anterior
        self.ui = uic.loadUi("GUI/ControlManual.ui", self)
        self.ui.btnVolver.clicked.connect(self.volver)

        # Filtros de la cámara
        self.filtros = ["Visual", "Infrarrojo", "Electroluminiscencia"]
        self.filtro_actual = 0

        # Mostrar filtro inicial
        self.ui.txtFiltros.setText(self.filtros[self.filtro_actual])

        # Conectar botones de filtro
        self.ui.btnFiltros_I.clicked.connect(self.filtro_izquierda)
        self.ui.btnFiltros_D.clicked.connect(self.filtro_derecha)

        # Conectar botón de cámara (simulado)
        self.ui.btnCamara.clicked.connect(self.tomar_captura)

        # Mostrar imagen de ejemplo al iniciar
        self.mostrar_imagen_camara("GUI/ejemplo.jpg")

        # --- Botones de los ejes ---
        self.valor_x = 0.0
        self.valor_y = 0.0
        self.valor_z = 0.0

        self.ui.btnMasX.clicked.connect(self.mas_x)
        self.ui.btnMenosX.clicked.connect(self.menos_x)
        self.ui.btnMasY.clicked.connect(self.mas_y)
        self.ui.btnMenosY.clicked.connect(self.menos_y)
        self.ui.btnMasZ.clicked.connect(self.mas_z)
        self.ui.btnMenosZ.clicked.connect(self.menos_z)

        self.actualizar_display_ejes()

        # --- Botones grandes ---
        self.ui.btnGirarModulo.clicked.connect(self.girar_modulo)
        self.ui.btnLlevarOrigen.clicked.connect(self.llevar_origen)
        self.ui.btnPruebaManual.clicked.connect(self.prueba_manual)

    def volver(self):
        self.close()
        if self.ventana_anterior:
            self.ventana_anterior.show()

    # Métodos para los filtros
    def filtro_izquierda(self):
        self.filtro_actual = (self.filtro_actual - 1) % len(self.filtros)
        self.ui.txtFiltros.setText(self.filtros[self.filtro_actual])

    def filtro_derecha(self):
        self.filtro_actual = (self.filtro_actual + 1) % len(self.filtros)
        self.ui.txtFiltros.setText(self.filtros[self.filtro_actual])

    def tomar_captura(self):
        pix = QPixmap("GUI/Panel_Visual.png")
        self.ui.lblCamara.setPixmap(pix.scaled(
            self.ui.lblCamara.width(),
            self.ui.lblCamara.height()
        ))

    def mostrar_imagen_camara(self, ruta_imagen):
        pix = QPixmap(ruta_imagen)
        self.ui.lblCamara.setPixmap(pix.scaled(
            self.ui.lblCamara.width(),
            self.ui.lblCamara.height()
        ))

    # Métodos para los ejes
    def actualizar_display_ejes(self):
        self.ui.txtEjeX.setText(f"{self.valor_x:+.2f}")
        self.ui.txtEjeY.setText(f"{self.valor_y:+.2f}")
        self.ui.txtEjeZ.setText(f"{self.valor_z:+.2f}")

    def mas_x(self):
        self.valor_x += 1.0
        self.actualizar_display_ejes()

    def menos_x(self):
        self.valor_x -= 1.0
        self.actualizar_display_ejes()

    def mas_y(self):
        self.valor_y += 1.0
        self.actualizar_display_ejes()

    def menos_y(self):
        self.valor_y -= 1.0
        self.actualizar_display_ejes()

    def mas_z(self):
        self.valor_z += 1.0
        self.actualizar_display_ejes()

    def menos_z(self):
        self.valor_z -= 1.0
        self.actualizar_display_ejes()

    # Métodos para los botones grandes
    def girar_modulo(self):
        print("Girando módulo...")
        self.ventana_progreso = VentanaProgresoGiro(self)
        self.ventana_progreso.show()

    def llevar_origen(self):
        print("Llevando al origen...")
        dlg = VentanaProgresoOrigen(self)
        dlg.exec_()

    def prueba_manual(self):
        dlg = VentanaPruebasManuales(self)
        dlg.exec_()

class VentanaInicio(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Inicio")
        btn = QPushButton("Regresar")
        btn.clicked.connect(self.close)
        layout = QVBoxLayout()
        layout.addWidget(btn)
        self.setLayout(layout)

class VentanaProgresoGiro(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Giro del Módulo")
        self.resize(300, 100)  # <-- Agranda la ventana aquí
        layout = QVBoxLayout()
        self.label = QLabel("Girando el módulo...")
        self.progress = QProgressBar()
        self.progress.setValue(0)
        layout.addWidget(self.label)
        layout.addWidget(self.progress)
        self.setLayout(layout)

        # Simulación de avance de la barra de progreso
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.avanzar)
        self.valor = 0
        self.timer.start(50)  # Actualiza cada 50 ms

    def avanzar(self):
        if self.valor < 100:
            self.valor += 2
            self.progress.setValue(self.valor)
        else:
            self.timer.stop()
            self.accept()  # Cierra la ventana automáticamente al terminar

class VentanaProgresoOrigen(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Llevar al Origen")
        self.resize(300, 100)
        layout = QVBoxLayout()
        self.label = QLabel("Llevando al origen...")
        self.progress = QProgressBar()
        self.progress.setValue(0)
        layout.addWidget(self.label)
        layout.addWidget(self.progress)
        self.setLayout(layout)

        # Simulación de avance de la barra de progreso
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.avanzar)
        self.valor = 0
        self.timer.start(50)

    def avanzar(self):
        if self.valor < 100:
            self.valor += 2
            self.progress.setValue(self.valor)
        else:
            self.timer.stop()
            self.accept()

class VentanaPruebasManuales(QDialog):
    def __init__(self, ventana_anterior=None):
        super().__init__()
        self.ventana_anterior = ventana_anterior
        self.ui = uic.loadUi("GUI/PruebasManuales.ui", self)
        self.ui.bntVolver.clicked.connect(self.volver)
        self.ui.bntT.clicked.connect(lambda: print("Ensayo Termografía"))
        self.ui.bntAE.clicked.connect(lambda: print("Ensayo Aislamiento Eléctrico"))
        self.ui.bntEL.clicked.connect(lambda: print("Ensayo Electroluminiscencia"))
        self.ui.bntIV.clicked.connect(lambda: print("Inspección Visual"))

    def volver(self):
        self.close()
        if self.ventana_anterior:
            self.ventana_anterior.show()