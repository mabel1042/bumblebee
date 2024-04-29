# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:06:33 2024

@author: lab
"""

class ModeloRobot:
    def __init__(self):
        self.posicion_base = (0, 0)
        self.estado_brazo = {'elevacion': 0, 'rotacion': 0, 'longitud': 0}
        self.movimiento_activo = False

    def mover_elevacion(self, elevacion):
        self.estado_brazo['elevacion'] = elevacion

    def mover_rotacion(self, rotacion):
        self.estado_brazo['rotacion'] = rotacion

    def mover_longitud(self, longitud):
        self.estado_brazo['longitud'] = longitud

    def detener_movimiento(self):
        self.movimiento_activo = False
