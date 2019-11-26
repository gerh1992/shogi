class Pieza():

    piezas_capturadas = []

    def __init__(self, jugador):
        self.jugador = jugador

class Rey(Pieza):
    simbolo = "K"

    def __init__(self, jugador):
        super().__init__(jugador)
        self.pieza = "K ^" if jugador.color == "blancas" else "K v"

    def __repr__(self):
        return "el rey"

    def checkear_movimiento(self, i_0, j_0, i_1, j_1, jugador, mensaje):
        if self.jugador != jugador:
            if mensaje: mensaje_pieza_rival(self)
            return False
        elif (checkear_fila(i_0, i_1) and abs(j_0 - j_1) == 1) or (checkear_columna(j_0, j_1) and abs(i_0 - i_1) == 1):
            return True
        elif abs(i_0 - i_1) == 1 and abs(j_0 - j_1) == 1:
            return True
        else:
            if mensaje: mensaje_movimiento_invalido(self)
            return False


class Torre(Pieza):
    simbolo = "R"

    def __init__(self, jugador):
        super().__init__(jugador)
        self.pieza = "R ^" if jugador.color == "blancas" else "R v"

    def __repr__(self):
        return "la torre"

    def checkear_movimiento(self, i_0, j_0, i_1, j_1, jugador, mensaje):
        if self.jugador != jugador:
            if mensaje: mensaje_pieza_rival(self)
            return False
        elif (checkear_columna(j_0, j_1) and not checkear_fila(i_0, i_1)) or (not checkear_columna(j_0, j_1) and checkear_fila(i_0, i_1)):
            return True
        else:
            if mensaje: mensaje_movimiento_invalido(self)
            return False

    def promover(self):
        return Torre_promocionada(self.jugador)

class Torre_promocionada(Pieza):
    simbolo = "+R"

    def __init__(self, jugador):
        super().__init__(jugador)
        self.pieza = "+R^" if jugador.color == "blancas" else "+Rv"

    def __repr__(self):
        return "la torre promocionada"

    def checkear_movimiento(self, i_0, j_0, i_1, j_1, jugador, mensaje):
        if self.jugador != jugador:
            if mensaje: mensaje_pieza_rival(self)
            return False
        elif (checkear_columna(j_0, j_1) and not checkear_fila(i_0, i_1)) or (not checkear_columna(j_0, j_1) and checkear_fila(i_0, i_1)):
            return True
        elif abs(i_0 - i_1) == 1 and abs(j_0 - j_1) == 1:
            return True
        else:
            if mensaje: mensaje_movimiento_invalido(self)
            return False

    def involucionar(self, jugador):
        return Torre(jugador)

class Alfil(Pieza):
    simbolo = "B"

    def __init__(self, jugador):
        super().__init__(jugador)
        self.pieza = "B ^" if jugador.color == "blancas" else "B v"

    def __repr__(self):
        return "el alfil"

    def checkear_movimiento(self, i_0, j_0, i_1, j_1, jugador, mensaje):
        if self.jugador != jugador:
            if mensaje: mensaje_pieza_rival(self)
            return False
        elif checkear_diag1(i_0, j_0, i_1, j_1) or checkear_diag2(i_0, j_0, i_1, j_1,):
            return True
        else:
            if mensaje: mensaje_movimiento_invalido(self)
            return False

    def promover(self):
        return  Alfil_promocionado(self.jugador)

class Alfil_promocionado(Pieza):
    simbolo = "+B"

    def __init__(self, jugador):
        super().__init__(jugador)
        self.pieza = "+B^" if jugador.color == "blancas" else "+Bv"

    def __repr__(self):
        return "el alfil promocionado"

    def checkear_movimiento(self, i_0, j_0, i_1, j_1, jugador, mensaje):
        if self.jugador != jugador:
            if mensaje: mensaje_pieza_rival(self)
            return False
        elif checkear_diag1(i_0, j_0, i_1, j_1) or checkear_diag2(i_0, j_0, i_1, j_1, ):
            return True
        elif (checkear_fila(i_0, i_1) and abs(j_0 - j_1) == 1) or (checkear_columna(j_0, j_1) and abs(i_0 - i_1) == 1):
            return True
        else:
            if mensaje: mensaje_movimiento_invalido(self)
            return False

    def involucionar(self, jugador):
        return Alfil(jugador)

class General_dorado(Pieza):
    simbolo = "G"

    def __init__(self, jugador):
        super().__init__(jugador)
        self.pieza = "G ^" if jugador.color == "blancas" else "G v"

    def __repr__(self):
        return "el general dorado"

    def checkear_movimiento(self, i_0, j_0, i_1, j_1, jugador, mensaje):
        if self.jugador != jugador:
            if mensaje: mensaje_pieza_rival(self)
            return False
        elif (abs(i_0 - i_1) == 1 and j_0 == j_1) or (abs(j_0 - j_1) == 1 and i_0 == i_1):
            return True
        elif turno_blancas(jugador):
            if i_0 - i_1 == 1 and abs(j_0 - j_1) == 1:
                return True
            if mensaje: mensaje_movimiento_invalido(self)
            return False
        elif not turno_blancas(jugador):
            if i_0 - i_1 == -1 and abs(j_0 - j_1) == 1:
                return True
            if mensaje: mensaje_movimiento_invalido(self)
            return False

class General_plateado(Pieza):
    simbolo = "S"

    def __init__(self, jugador):
        super().__init__(jugador)
        self.pieza = "S ^" if jugador.color == "blancas" else "S v"

    def __repr__(self):
        return "el general plateado"

    def checkear_movimiento(self, i_0, j_0, i_1, j_1, jugador, mensaje):
        if self.jugador != jugador:
            if mensaje: mensaje_pieza_rival(self)
            return False
        elif abs(i_0 - i_1) == 1 and abs(j_0 - j_1) == 1:
            return True
        elif turno_blancas(jugador):
            if i_0 - i_1 == 1:
                return True
            if mensaje: mensaje_movimiento_invalido(self)
            return False
        elif not turno_blancas(jugador):
            if i_0 - i_1 == -1:
                return True
            if mensaje: mensaje_movimiento_invalido(self)
            return False
        else:
            if mensaje: mensaje_movimiento_invalido(self)
            return False

        def promover(self):
            return General_plateado_promocionado(self.jugador)

class General_plateado_promocionado(Pieza):
    simbolo = "+S"

    def __init__(self, jugador):
        super().__init__(jugador)
        self.pieza = "+S^" if jugador.color == "blancas" else "+Sv"

    def __repr__(self):
        return "el general plateado promocionado"

    def checkear_movimiento(self, i_0, j_0, i_1, j_1, jugador, mensaje):
        if self.jugador != jugador:
            if mensaje: mensaje_pieza_rival(self)
            return False
        elif (abs(i_0 - i_1) == 1 and j_0 == j_1) or (abs(j_0 - j_1) == 1 and i_0 == i_1):
            return True
        elif turno_blancas(jugador):
            if i_0 - i_1 == 1 and abs(j_0 - j_1) == 1:
                return True
            if mensaje: mensaje_movimiento_invalido(self)
            return False
        elif not turno_blancas(jugador):
            if i_0 - i_1 == -1 and abs(j_0 - j_1) == 1:
                return True
            if mensaje: mensaje_movimiento_invalido(self)
            return False

    def involucionar(self, jugador):
        return General_plateado(jugador)

class Caballo(Pieza):
    simbolo = "N"

    def __init__(self, jugador):
        super().__init__(jugador)
        self.pieza = "N ^" if jugador.color == "blancas" else "N v"

    def __repr__(self):
        return "el caballo"

    def checkear_movimiento(self, i_0, j_0, i_1, j_1, jugador, mensaje):
        if self.jugador != jugador:
            if mensaje: mensaje_pieza_rival(self)
            return False
        elif turno_blancas(jugador):
            if i_0 - i_1 == 2 and abs(j_0 - j_1) == 1:
                return True
            else:
                if mensaje: mensaje_movimiento_invalido(self)
                return False
        elif not turno_blancas(jugador):
            if i_0 - i_1 == -2 and abs(j_0 - j_1) == 1:
                return True
            else:
                if mensaje: mensaje_movimiento_invalido(self)
                return False

    def promover(self):
        return Caballo_promocionado(self.jugador)

class Caballo_promocionado(Pieza):
    simbolo = "+N"

    def __init__(self, jugador):
        super().__init__(jugador)
        self.pieza = "+N^" if jugador.color == "blancas" else "+Nv"

    def __repr__(self):
        return "el caballo promocionado"

    def checkear_movimiento(self, i_0, j_0, i_1, j_1, jugador, mensaje):
        if self.jugador != jugador:
            if mensaje: mensaje_pieza_rival(self)
            return False
        elif (abs(i_0 - i_1) == 1 and j_0 == j_1) or (abs(j_0 - j_1) == 1 and i_0 == i_1):
            return True
        elif turno_blancas(jugador):
            if i_0 - i_1 == 1 and abs(j_0 - j_1) == 1:
                return True
            if mensaje: mensaje_movimiento_invalido(self)
            return False
        elif not turno_blancas(jugador):
            if i_0 - i_1 == -1 and abs(j_0 - j_1) == 1:
                return True
            if mensaje: mensaje_movimiento_invalido(self)
            return False

    def involucionar(self, jugador):
        return Caballo(jugador)

class Lancero(Pieza):
    simbolo = "L"

    def __init__(self, jugador):
        super().__init__(jugador)
        self.pieza = "L ^" if jugador.color == "blancas" else "L v"

    def __repr__(self):
        return "el lancero"

    def checkear_movimiento(self, i_0, j_0, i_1, j_1, jugador, mensaje):
        if self.jugador != jugador:
            if mensaje: mensaje_pieza_rival(self)
            return False
        elif turno_blancas(jugador):
            if checkear_columna(j_0, j_1) and i_0 > i_1:
                return True
            if mensaje: mensaje_movimiento_invalido(self)
            return False
        elif not turno_blancas(jugador):
            if checkear_columna(j_0, j_1) and i_0 < i_1:
                return True
            if mensaje: mensaje_movimiento_invalido(self)
            return False
        else:
            if mensaje: mensaje_movimiento_invalido(self)
            return False

    def promover(self, jugador):
        return Lancero_promocionado(jugador)

class Lancero_promocionado(Pieza):
    simbolo = "+L"

    def __init__(self, jugador):
        super().__init__(jugador)
        self.pieza = "+L^" if jugador.color == "blancas" else "+Lv"

    def __repr__(self):
        return "el lancero promocionado"

    def checkear_movimiento(self, i_0, j_0, i_1, j_1, jugador, mensaje):
        if self.jugador != jugador:
            if mensaje: mensaje_pieza_rival(self)
            return False
        elif (abs(i_0 - i_1) == 1 and j_0 == j_1) or (abs(j_0 - j_1) == 1 and i_0 == i_1):
            return True
        elif turno_blancas(jugador):
            if i_0 - i_1 == 1 and abs(j_0 - j_1) == 1:
                return True
            if mensaje: mensaje_movimiento_invalido(self)
            return False
        elif not turno_blancas(jugador):
            if i_0 - i_1 == -1 and abs(j_0 - j_1) == 1:
                return True
            if mensaje: mensaje_movimiento_invalido(self)
            return False

    def involucionar(self, jugador):
        return Lancero(jugador)

class Peon(Pieza):
    simbolo = "P"

    def __init__(self, jugador):
        super().__init__(jugador)
        self.pieza = "P ^" if jugador.color == "blancas" else "P v"

    def __repr__(self):
        return "el peon"


    def checkear_movimiento(self, i_0, j_0, i_1, j_1, jugador, mensaje):
        if self.jugador != jugador:
            if mensaje: mensaje_pieza_rival(self)
            return False
        elif turno_blancas(jugador):
            if i_0 == (i_1 + 1) and j_0 == j_1:
                return True
            else:
                if mensaje: mensaje_movimiento_invalido(self)
                return False
        elif not turno_blancas(jugador):
            if i_0 == (i_1 - 1) and j_0 == j_1:
                return True
            else:
                if mensaje: mensaje_movimiento_invalido(self)
                return False
        return False

    def promover(self):
        return Peon_promocionado(self.jugador)

class Peon_promocionado(Pieza):
    simbolo = "+P"

    def __init__(self, jugador):
        super().__init__(jugador)
        self.pieza = "+P^" if jugador.color == "blancas" else "+Pv"

    def __repr__(self):
        return "el peon promocionado"

    def checkear_movimiento(self, i_0, j_0, i_1, j_1, jugador, mensaje):
        if self.jugador != jugador:
            if mensaje: mensaje_pieza_rival(self)
            return False
        elif (abs(i_0 - i_1) == 1 and j_0 == j_1) or (abs(j_0 - j_1) == 1 and i_0 == i_1):
            return True
        elif turno_blancas(jugador):
            if i_0 - i_1 == 1 and abs(j_0 - j_1) == 1:
                return True
            if mensaje: mensaje_movimiento_invalido(self)
            return False
        elif not turno_blancas(jugador):
            if i_0 - i_1 == -1 and abs(j_0 - j_1) == 1:
                return True
            if mensaje: mensaje_movimiento_invalido(self)
            return False

    def involucionar(self, jugador):
        return Peon(jugador)

def mensaje_pieza_rival(pieza):
    print(mensaje_invalido() + "Ese es " + str(pieza) + " de su rival")

def mensaje_movimiento_invalido(pieza):
    print(mensaje_invalido() + str(pieza) + " no puede realizar ese movimiento")

def mensaje_invalido():
    return "Movimiento invalido!"

def checkear_columna(j_0, j_1):
    return j_0 == j_1

def checkear_fila(i_0, i_1):
    return i_0 == i_1

def checkear_diag1(i_0, j_0, i_1, j_1):
    return abs(i_0 - j_0) == abs(i_1 - j_1)

def checkear_diag2(i_0, j_0, i_1, j_1):
    return i_0 + j_0 == i_1 + j_1

def turno_blancas(jugador):
    return jugador.color == "blancas"