from .piezas import *

class Jugador:

    def __init__(self, nombre, color):

        self.nombre = nombre
        self.color = color
        if self.color == "blancas":
            self.color_consola = "red"
        else:
            self.color_consola = "blue"
        self.piezas_capturadas = []


    def mostrar_piezas_capturadas(self):
        print("capturadas: [", end="")
        for i in range(len(self.piezas_capturadas)):
            if i == len(self.piezas_capturadas) - 1:
                print(self.piezas_capturadas[i].simbolo, end = "")
            else:
                print(self.piezas_capturadas[i].simbolo + ",", end="")
        print("]")

    def mostrar_piezas_capturadas_indexadas(self):
        print("capturadas: [", end="")
        for i in range(len(self.piezas_capturadas)):
            if i == len(self.piezas_capturadas) - 1:
                print(str(i + 1) + " - " + self.piezas_capturadas[i].simbolo, end = "")
            else:
                print(str(i + 1) + " - " + self.piezas_capturadas[i].simbolo + ",", end="")
        print("]")



