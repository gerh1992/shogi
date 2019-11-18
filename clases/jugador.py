from .piezas import *


class Jugador:

    def __init__(self, nombre, color):

        self.nombre = nombre
        self.color = color
        if self.color == "blancas":
            self.color_consola = "red"
        else:
            self.color_consola = "blue"



