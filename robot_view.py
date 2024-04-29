# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:07:05 2024

@author: lab
"""

class VistaRobot:
    def __init__(self):
        pass

    def mostrar_estado_robot(self, posicion_base, estado_brazo):
        print(f"Posicion base: {posicion_base}")
        print(f"Estado brazo: {estado_brazo}")

    def obtener_entrada_usuario(self):
        elevacion = int(input("Ingrese elevacion: "))
        rotacion = int(input("Ingrese rotacion: "))
        longitud = int(input("Ingrese longitud: "))
        return elevacion, rotacion, longitud

    def mostrar_error(self, mensaje):
        print(f"Error: {mensaje}")
