from clases.jugador import Jugador
from clases.piezas import *
from termcolor import *
import colorama

colorama.init()


class Tablero:
    def __init__(self, jugador1, jugador2):
        self.tablero = [
            [Lancero(jugador1), Caballo(jugador1), General_plateado(jugador1), General_dorado(jugador1), Rey(jugador1),
             General_dorado(jugador1), General_plateado(jugador1), Caballo(jugador1), Lancero(jugador1)],
            ["--", Torre(jugador1), "--", "--", "--", "--", "--", Alfil(jugador1), "--"],
            [Peon(jugador1), Peon(jugador1), Peon(jugador1), Peon(jugador1), Peon(jugador1), Peon(jugador1),
             Peon(jugador1), Peon(jugador1), Peon(jugador1)],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            [Peon(jugador2), Peon(jugador2), Peon(jugador2), Peon(jugador2), Peon(jugador2), Peon(jugador2),
             Peon(jugador2), Peon(jugador2), Peon(jugador2)],
            ["--", Alfil(jugador2), "--", "--", "--", "--", "--", Torre(jugador2), "--"],
            [Lancero(jugador2), Caballo(jugador2), General_plateado(jugador2), General_dorado(jugador2), Rey(jugador2),
             General_dorado(jugador2), General_plateado(jugador2), Caballo(jugador2), Lancero(jugador2)]]
        self.diccionario = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, 1: 8, 2: 7, 3: 6,
                            4: 5, 5: 4, 6: 3, 7: 2, 8: 1, 9: 0}
        self.turno = 0
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def mostrar_tablero(self):

        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                self.mostrar_pieza(i, j)
            print("")

        print("   a    b    c    d    e    f    g    h    i")

    def mostrar_pieza(self, i, j):
        if j == 0:
            if self.tablero[i][j] == "--":
                print(str(self.diccionario.get(i + 1) + 1) + "| " + self.tablero[i][j] + " | ", end="")
            else:
                print(str(self.diccionario.get(i + 1) + 1) + "| " + colored(self.tablero[i][j].pieza, self.tablero[i][
                    j].jugador.color_consola) + " | ", end="")
        else:
            if self.tablero[i][j] == "--":
                print(self.tablero[i][j] + " | ", end="")
            else:
                print(colored(self.tablero[i][j].pieza, self.tablero[i][j].jugador.color_consola) + " | ", end="")

    def checkear_limites(self, x_0, y_0, x_1, y_1):
        if (x_0 or y_0 or x_1 or y_1) < 0 or (x_0 or y_0 or x_1 or y_1) > 9:
            print("Movimiento fuera de los limites del tablero")
            return False
        else:
            return True

    def checkear_pieza(self, x_0, y_0, x_1, y_1, jugador):
        if self.tablero[x_0][y_0] == "--":
            print("En esa casilla no hay ninguna ficha")
            return False
        else:
            if self.tablero[x_0][y_0].checkear_movimiento(x_0, y_0, x_1, y_1, jugador):
                return True
            else:
                return False


    def checkear(self, x_0, y_0, x_1, y_1, jugador):

        if self.checkear_limites(x_0, y_0, x_1, y_1) and self.checkear_pieza(x_0, y_0, x_1, y_1, jugador):
            return True
        else:
            return False

    def jugar(self):

        self.mostrar_tablero()
        if self.turno % 2 == 0:
            self.realizar_turno(self.jugador2)
        else:
            self.realizar_turno(self.jugador1)
        self.turno += 1

    def realizar_turno(self, jugador):
        print("Turno " + jugador.color + "!")
        desde = self.pedir_coordenadas_arranque()
        hasta = self.pedir_coordenadas_fin()

        if not self.checkear(desde[0], desde[1], hasta[0], hasta[1], jugador):
            self.realizar_turno(jugador)
        else:
            self.tablero[hasta[0]][hasta[1]] = self.tablero[desde[0]][desde[1]]
            self.tablero[desde[0]][desde[1]] = "--"

    def checkear_ganador(self):
        ##  Hacer!
        return False

    def pedir_coordenadas_arranque(self):
        mov = input("Elegir ficha para realizar movimiento(Ej: D2 o d2)")
        mov.replace(' ', '')
        desde = [10, 10]
        if (len(mov) != 2):
            print("Coordenadas invalidas")
        else:
            mov = mov.lower()
            desde = [self.diccionario.get(int(mov[1])), self.diccionario.get(mov[0])]
        return desde

    def pedir_coordenadas_fin(self):
        mov = input("Elegir destino de la ficha(Ej: D2 o d2)")
        mov.replace(' ', '')
        hasta = [10, 10]
        if (len(mov) != 2):
            print("Coordenadas invalidas")
        else:
            mov = mov.lower()
            hasta = [self.diccionario.get(int(mov[1])), self.diccionario.get(mov[0])]
        return hasta
