# -*- coding: utf-8 -*-
import threading
import reset_server  # Asegúrate de que reset_server.py esté en la misma carpeta o en el path

# Iniciar Flask en un hilo (sin debug=True para evitar errores con threading)
flask_thread = threading.Thread(target=reset_server.app.run, kwargs={'port': 5000})
flask_thread.daemon = True
flask_thread.start()

from HMI import HMI
app = HMI()