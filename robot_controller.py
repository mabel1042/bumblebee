# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:07:20 2024

@author: lab
"""

class ControladorRobot:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def procesar_comando(self, comando):
        if comando.startswith("mover_elevacion"):
            try:
                _, elevacion = comando.split()
                elevacion = int(elevacion)
            except ValueError:
                self.vista.mostrar_error("Valor de elevacion invalido")
                return

            self.modelo.mover_elevacion(elevacion)
        elif comando.startswith("mover_rotacion"):
            try:
                _, rotacion = comando.split()
                rotacion = int(rotacion)
            except ValueError:
                self.vista.mostrar_error("Valor de rotacion invalido")
                return

            self.modelo.mover_rotacion(rotacion)
        elif comando.startswith("mover_longitud"):
            try:
                _, longitud = comando.split()
                longitud = int(longitud)
            except ValueError:
                self.vista.mostrar_error("Valor de longitud invalido")
                return

            self.modelo.mover_longitud(longitud)
        elif comando == "detener_movimiento":
            self.modelo.detener_movimiento()
        else:
            self.vista.mostrar_error("Comando desconocido")

    def ejecutar(self):
        while True:
            entrada_usuario = input("Ingrese comando: ")
            if entrada_usuario == "salir":
                break
            self.procesar_comando(entrada_usuario)
            self.vista.mostrar_estado_robot(self.modelo.posicion_base, self.modelo.estado_brazo)
