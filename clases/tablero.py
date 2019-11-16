from clases.jugador import Jugador
from clases.piezas import *
from termcolor import *
import colorama

colorama.init()

class Tablero:
    def __init__(self, jugador1, jugador2):
        self.tablero = [[Lancero(jugador1), Caballo(jugador1), General_plateado(jugador1), General_dorado(jugador1), Rey(jugador1), General_dorado(jugador1), General_plateado(jugador1), Caballo(jugador1), Lancero(jugador1)],
                   ["--", Torre(jugador1), "--", "--", "--", "--", "--", Alfil(jugador1), "--"],
                   [Peon(jugador1), Peon(jugador1), Peon(jugador1), Peon(jugador1), Peon(jugador1),Peon(jugador1), Peon(jugador1), Peon(jugador1), Peon(jugador1)],
                   ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                   ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                   ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
                   [Peon(jugador2), Peon(jugador2), Peon(jugador2), Peon(jugador2), Peon(jugador2),Peon(jugador2), Peon(jugador2), Peon(jugador2), Peon(jugador2)],
                   ["--", Alfil(jugador2), "--", "--", "--", "--", "--", Torre(jugador2), "--"],
                   [Lancero(jugador2), Caballo(jugador2), General_plateado(jugador2), General_dorado(jugador2), Rey(jugador2), General_dorado(jugador2), General_plateado(jugador2), Caballo(jugador2), Lancero(jugador2)]]

    def mostrar_tablero(self):

        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                self.mostrar_pieza(i, j)
            print("")

        print("    a    b    c    d    e    f    g    h    i")

    def mostrar_pieza(self, i, j):
        if j == 0:
            if self.tablero[i][j] == "--":
                print(str(i + 1) + "| " + self.tablero[i][j] + " | ", end="")
            else:
                print(str(i + 1) + "| " + colored(self.tablero[i][j].pieza, self.tablero[i][j].jugador.color) + " | ", end="")
        else:
            if self.tablero[i][j] == "--":
                print(self.tablero[i][j] + " | ", end="")
            else:
                print(colored(self.tablero[i][j].pieza, self.tablero[i][j].jugador.color) + " | ", end="")

    def checkear_limites(self, x_0, y_0, x_1, y_1):
        if(x_0 or y_0 or x_1 or y_1) < 0 or (x_0 or y_0 or x_1 or y_1) > 9:
            return False
        else:
            return True