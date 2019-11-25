from clases.jugador import Jugador
from clases.piezas import *


class Tablero:
    def __init__(self, negras, blancas):
        self.tablero = [
            [Lancero(negras), Caballo(negras), General_plateado(negras), General_dorado(negras), Rey(negras),
             General_dorado(negras), General_plateado(negras), Caballo(negras), Lancero(negras)],
            ["---", Torre(negras), "---", "---", "---", "---", "---", Alfil(negras), "---"],
            [Peon(negras), Peon(negras), Peon(negras), Peon(negras), Peon(negras), Peon(negras),
             Peon(negras), Peon(negras), Peon(negras)],
            ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
            ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
            ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
            [Peon(blancas), Peon(blancas), Peon(blancas), Peon(blancas), Peon(blancas), Peon(blancas),
             Peon(blancas), Peon(blancas), Peon(blancas)],
            ["---", Alfil(blancas), "---", "---", "---", "---", "---", Torre(blancas), "---"],
            [Lancero(blancas), Caballo(blancas), General_plateado(blancas), General_dorado(blancas), Rey(blancas),
             General_dorado(blancas), General_plateado(blancas), Caballo(blancas), Lancero(blancas)]]

        self.turno = 0
        self.negras = negras
        self.blancas = blancas
        self.rey_negras = [0, 4]
        self.rey_blancas = [8, 4]

    def mostrar_tablero(self):
        self.negras.mostrar_piezas_capturadas()
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                self.mostrar_pieza(i, j)
            print("")

        print("   a     b     c     d     e     f     g     h     i")
        self.blancas.mostrar_piezas_capturadas()

    def mostrar_pieza(self, i, j):
        if j == 0:
            if self.es_vacio(i, j):
                print(str(diccionario.get(i + 1) + 1) + "| " + self.tablero[i][j] + " | ", end="")
            else:
                print(str(diccionario.get(i + 1) + 1) + "| " + self.tablero[i][j].pieza + " | ", end="")
        else:
            if self.es_vacio(i, j):
                print(self.tablero[i][j] + " | ", end="")
            else:
                print(self.tablero[i][j].pieza + " | ", end="")

    def checkear_limites(self, x_0, y_0, x_1, y_1):
        if (x_0 or y_0 or x_1 or y_1) < 0 or (x_0 or y_0 or x_1 or y_1) > 9:
            print("Movimiento fuera de los limites del tablero")
            return False
        else:
            return True

    def checkear_pieza(self, i_0, j_0, i_1, j_1, jugador):
        if self.es_vacio(i_0, j_0):
            print("En esa casilla no hay ninguna ficha de las " + jugador.color)
            return False
        elif not self.es_vacio(i_1, j_1) and self.tablero[i_1][j_1].jugador.color == jugador.color:
            print("No se pudo mover " + str(
                self.tablero[i_0][j_0]) + " porque ya hay una ficha suya ocupando la casilla de destino")
            return False
        else:
            if self.tablero[i_0][j_0].checkear_movimiento(i_0, j_0, i_1, j_1, jugador, True):
                return self.checkear_camino(i_0, j_0, i_1, j_1)
            else:
                return False

    def checkear(self, i_0, j_0, i_1, j_1, jugador):
        if self.checkear_limites(i_0, j_0, i_1, j_1) and self.checkear_pieza(i_0, j_0, i_1, j_1, jugador):
            return True
        else:
            return False

    def jugar(self):
        self.mostrar_tablero()

        if self.turno % 2 == 0:
            self.realizar_turno(self.blancas)
        else:
            self.realizar_turno(self.negras)
        self.turno += 1

    def realizar_turno(self, jugador):
        if self.checkear_jaque(jugador):
            mensaje_jaque(jugador)
        mensaje_turno(jugador)
        if consultar_resurrecion(jugador):
            self.revivir_pieza(jugador)
        else:
            i_0, j_0 = pedir_coordenadas(0)
            i_1, j_1 = pedir_coordenadas(1)

            if not self.checkear(i_0, j_0, i_1, j_1, jugador):
                self.realizar_turno(jugador)
            else:
                self.mover_pieza(jugador, i_0, j_0, i_1, j_1)

    def mover_pieza(self, jugador, i_0, j_0, i_1, j_1):
        if not self.es_vacio(i_1, j_1):
            self.remover_pieza(jugador, i_1, j_1)
        self.actualizar_tablero(jugador, i_0, j_0, i_1, j_1)

    def remover_pieza(self, jugador, i, j):
        if turno_blancas(jugador):
            self.blancas.piezas_capturadas.append(self.tablero[i][j])
        else:
            self.negras.piezas_capturadas.append(self.tablero[i][j])

    def actualizar_tablero(self, jugador, i_0, j_0, i_1, j_1):
        self.tablero[i_1][j_1] = self.tablero[i_0][j_0]
        self.tablero[i_0][j_0] = "---"
        if self.tablero[i_1][j_1].__class__ is Rey:
            self.actualizar_posicion_rey(jugador, i_1, j_1)
        if self.checkear_promocion(i_0, i_1, self.tablero[i_1][j_1], jugador):
            self.promover_pieza(i_1, j_1)

    def actualizar_posicion_rey(self, jugador, i, j):
        if turno_blancas(jugador):
            self.rey_blancas = [i, j]
        elif not turno_blancas(jugador):
            self.rey_negras = [i, j]

    def checkear_ganador(self):
        if self.rey_negras in self.negras.piezas_capturadas:
            mensaje_victoria(self.negras)
            return True
        elif self.rey_blancas in self.blancas.piezas_capturadas:
            mensaje_victoria(self.blancas)
            return True
        else:
            return False

    def promover_pieza(self, i, j):
        self.tablero[i][j] = self.tablero[i][j].promover()

    def checkear_camino(self, i_0, j_0, i_1, j_1):
        if self.tablero[i_0][j_0].__class__ == Caballo:
            return True

        while i_0 != i_1 or j_0 != j_1:
            i_0 = acercar(i_0, i_1)
            j_0 = acercar(j_0, j_1)
            if i_0 == i_1 and j_0 == j_1:
                break
            elif not self.es_vacio(i_0, j_0):
                print("No se puede realizar ese movimiento! Esta " + str(
                    self.tablero[i_0][j_0]) + " bloqueando el camino!")
                return False
        return True

    def revivir_pieza(self, jugador):
        pieza = elegir_pieza(jugador)
        jugador.piezas_capturadas.remove(pieza)
        if pieza.__class__ in piezas_promocionadas:
            pieza = pieza.involucionar(jugador)
        else:
            pieza.__init__(jugador)
        while True:
            i, j = pedir_coordenadas(0)
            if self.son_coordenadas_validas_resurreccion(i, j, jugador, pieza.__class__):
                self.tablero[i][j] = pieza
                break
            else:
                print("Movimiento invalido! No se puede ubicar la pieza en esas coordenadas")

    def checkear_promocion(self, x_0, x_1, pieza, jugador):
        if esta_en_zona_promocionable(jugador, x_0, x_1) and pieza.__class__ in piezas_promocionables:
            return preguntar_promocion(pieza, jugador)

    def checkear_jaque(self, jugador):
        if self.buscar_amenazas(jugador):
            return True
        else:
            return False

    def buscar_amenazas(self, jugador):
        rey = self.rey_blancas if turno_blancas(jugador) else self.rey_negras
        enemigo = self.negras if turno_blancas(jugador) else self.blancas
        if self.amenazas_horizontales(rey, enemigo, jugador) or self.amenazas_verticales(rey,enemigo, jugador) \
                or self.amenazas_diagonal_1(rey, enemigo, jugador) or self.amenazas_diagonal_2(rey, enemigo, jugador)\
                or self.amenazas_caballos(rey, enemigo, jugador):
            return True
        else:
            return False

    def amenazas_horizontales(self, rey, enemigo, jugador):
        i = rey[0]
        j_1 = rey[1] + 1
        j_2 = rey[1] - 1

        # Revisar la derecha y dps la izquierda
        while j_1 < 9:
            if not self.es_vacio(i, j_1) and self.tablero[i][j_1].jugador is jugador:
                break
            elif not self.es_vacio(i, j_1):
                if self.tablero[i][j_1].checkear_movimiento(i, j_1, rey[0], rey[1], enemigo, False):
                    return True
                else:
                    break
            j_1 += 1

        while j_2 > -1:
            if not self.es_vacio(i, j_2) and self.tablero[i][j_2].jugador is jugador:
                break
            elif not self.es_vacio(i, j_2):
                if self.tablero[i][j_2].checkear_movimiento(i, j_2, rey[0], rey[1], enemigo, False):
                    return True
                else:
                    break
            j_2 -= 1

        return False

    def amenazas_verticales(self, rey, enemigo, jugador):
        i_1 = rey[0] + 1
        i_2 = rey[0] - 1
        j = rey[1]

        while i_1 < 9:
            if not self.es_vacio(i_1, j) and self.tablero[i_1][j].jugador is jugador:
                break
            elif not self.es_vacio(i_1, j):
                if self.tablero[i_1][j].checkear_movimiento(i_1, j, rey[0], rey[1], enemigo, False):
                    return True
                else:
                    break
            i_1 += 1

        while i_2 > -1:
            if not self.es_vacio(i_2, j) and self.tablero[i_2][j].jugador is jugador:
                break
            elif not self.es_vacio(i_2, j):
                if self.tablero[i_2][j].checkear_movimiento(i_2, j, rey[0], rey[1], enemigo, False):
                    return True
                else:
                    break
            i_2 -= 1

        return False

    def amenazas_diagonal_1(self, rey, enemigo, jugador):
        i_1 = rey[0] + 1
        i_2 = rey[0] - 1
        j_1 = rey[1] + 1
        j_2 = rey[1] - 1

        while i_1 < 9 and j_1 < 9:
            if not self.es_vacio(i_1, j_1) and self.tablero[i_1][j_1].jugador is jugador:
                break
            elif not self.es_vacio(i_1, j_1):
                if self.tablero[i_1][j_1].checkear_movimiento(i_1, j_1, rey[0], rey[1], enemigo, False):
                    return True
                else:
                    break
            i_1 += 1
            j_1 += 1

        while (i_2 and j_2) > -1:
            if not self.es_vacio(i_2, j_2) and self.tablero[i_2][j_2].jugador is jugador:
                break
            elif not self.es_vacio(i_2, j_2):
                if self.tablero[i_2][j_2].checkear_movimiento(i_2, j_2, rey[0], rey[1], enemigo, False):
                    return True
                else:
                    break
            i_2 -= 1
            j_2 -= 1
        return False

    def amenazas_diagonal_2(self, rey, enemigo, jugador):
        i_1 = rey[0] + 1
        i_2 = rey[0] - 1
        j_1 = rey[1] - 1
        j_2 = rey[1] + 1

        while i_1 < 9 and j_1 > -1:

            if not self.es_vacio(i_1, j_1) and self.tablero[i_1][j_1].jugador is jugador:
                break
            elif not self.es_vacio(i_1, j_1):
                if self.tablero[i_1][j_1].checkear_movimiento(i_1, j_1, rey[0], rey[1], enemigo, False):
                    return True
                else:
                    break
            i_1 += 1
            j_1 -= 1

        while i_2 > -1 and j_2 < 9:
            if not self.es_vacio(i_2, j_2) and self.tablero[i_2][j_2].jugador is jugador:
                break
            elif not self.es_vacio(i_2, j_2):
                if self.tablero[i_2][j_2].checkear_movimiento(i_2, j_2, rey[0], rey[1], enemigo, False):
                    return True
                else:
                    break
            i_2 -= 1
            j_2 += 1
        return False

    def amenazas_caballos(self, rey, enemigo, jugador):
        i, j = rey
        if jugador is self.blancas:
            if i - 2 > -1 and j + 1 < 9 and j - 1 > -1:
                if not self.es_vacio(i - 2, j + 1) and self.tablero[i - 2][j + 1].jugador is enemigo:
                    if self.tablero[i - 2][j + 1].__class__ is Caballo:
                        return True
                elif not self.es_vacio(i - 2, j - 1) and self.tablero[i - 2][j - 1].jugador is enemigo:
                    if self.tablero[i - 2][j - 1].__class__ is Caballo:
                        return True
            return False
        else:
            if i - 2 < 9 and j - 1 > -1 and j + 1 < 9:
                if not self.es_vacio(i + 2, j + 1) and self.tablero[i + 2][j + 1].jugador is enemigo:
                    if self.tablero[i + 2][j - 1].__class__ is Caballo:
                        return True
                elif not self.es_vacio(i + 2, j - 1) and self.tablero[i + 2][j - 1].jugador is enemigo:
                    if self.tablero[i + 2][j - 1].__class__ is Caballo:
                        return True
            return False


    def es_vacio(self, i, j):
        return True if self.tablero[i][j] == '---' else False

    def son_coordenadas_validas_resurreccion(self, i, j, jugador, tipo_pieza):
        if self.es_vacio(i, j) and tipo_pieza not in (Lancero, Peon, Caballo):
            return True
        elif self.es_vacio(i, j) and tipo_pieza in (Peon, Lancero) and turno_blancas(jugador) and i != 0:
            return True
        elif self.es_vacio(i, j) and tipo_pieza in (Peon, Lancero) and not turno_blancas(jugador) and i != 8:
            return True
        elif self.es_vacio(i, j) and tipo_pieza is Caballo and turno_blancas(jugador) and i >= 2:
            return True
        elif self.es_vacio(i, j) and tipo_pieza is Caballo and not turno_blancas(jugador) and i <= 6:
            return True
        else:
            return False


def mensaje_coordenadas_invalidas():
    print("Coordenadas invalidas")


def preguntar_promocion(pieza, jugador):
    respuesta = input("Quiere promover " + str(pieza) + " de las " + jugador.color + " Y/N")
    if respuesta.lower() == 'y':
        return True
    else:
        return False


def esta_en_zona_promocionable(jugador, x_0, x_1):
    if turno_blancas(jugador):
        return ((x_0 >= 0 and x_0 <= 2) or (x_1 >= 0 and x_1 <= 2))
    elif not turno_blancas(jugador):
        return ((x_0 <= 8 and x_0 >= 6) or (x_1 <= 8 and x_1 >= 6))
    else:
        return False


def acercar(var_0, var_1):
    if var_0 > var_1:
        return var_0 - 1
    elif var_0 < var_1:
        return var_0 + 1
    else:
        return var_0


diccionario = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, 1: 8, 2: 7, 3: 6,
               4: 5, 5: 4, 6: 3, 7: 2, 8: 1, 9: 0}
piezas_promocionadas = {Caballo_promocionado, Peon_promocionado, Torre_promocionada, Alfil_promocionado,
                        General_plateado_promocionado, Lancero_promocionado}
piezas_promocionables = {Caballo, Peon, Torre, Alfil, General_plateado, Lancero}
amenazas_horizontales = {Torre, Torre_promocionada}
amenazas_verticales = {Torre, Torre_promocionada}
amenazas_diagonales = {Alfil, Alfil_promocionado}


def pedir_coordenadas(codigo):
    if codigo == 0:
        mensaje = "Elegir coordenadas de la pieza(Ej: D2 o d2)"
    else:
        mensaje = "Elegir destino de la pieza(Ej: D2 o d2)"
    mov = input(mensaje)
    mov.replace(' ', '')
    coordenadas = [10, 10]
    if (len(mov) != 2) or mov.isdigit() or mov.isalpha():
        mensaje_coordenadas_invalidas()
    else:
        mov = mov.lower()
        coordenadas = [diccionario.get(int(mov[1])), diccionario.get(mov[0])]
    return coordenadas


def mensaje_jaque(jugador):
    print("Las " + jugador.color + " estan en jaque!")


def mensaje_turno(jugador):
    print("Turno " + jugador.color + "!")


def mensaje_victoria(jugador):
    print("Las " + jugador.color + " han ganado la partida!!!")


def consultar_resurrecion(jugador):
    if len(jugador.piezas_capturadas) == 0:
        return False
    else:
        respuesta = input("Quiere revivir una de las piezas que ha capturado?. Y/N")
        return respuesta.lower() == "y"


def elegir_pieza(jugador):
    while True:
        jugador.mostrar_piezas_capturadas_indexadas()
        indice = input(
            "Elija un numero del 1 al " + str(len(jugador.piezas_capturadas)) + " para revivir una de sus piezas")
        if not indice.isdigit() or int(indice) > len(jugador.piezas_capturadas) or int(indice) < 1:
            print("El indice elegido esta fuera de rango. Vuelva a elegir")
        else:
            return jugador.piezas_capturadas[int(indice) - 1]
