# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:07:59 2024

@author: lab
"""

from robot_model import ModeloRobot
from robot_view import VistaRobot
from robot_controller import ControladorRobot

if __name__ == "__main__":
    modelo = ModeloRobot()
    vista = VistaRobot()
    controlador = ControladorRobot(modelo, vista)

    controlador.ejecutar()
