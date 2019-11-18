class Pieza():

    piezas_capturadas = []

    def __init__(self, jugador):
        self.jugador = jugador
        self.mensaje_invalido = "Movimiento invalido!"

    def checkear_y(self, y_0, y_1):
        return y_0 == y_1

    def checkear_x(self, x_0, x_1):
        return x_0 == x_1


class Rey(Pieza):

    pieza = "K "

    def __init__(self, jugador):
        super().__init__(jugador)


class Torre(Pieza):

    pieza = "R "

    def __init__(self, jugador):
        super().__init__(jugador)

    def checkear_movimiento(self, x_0, y_0, x_1, y_1, jugador):
        if self.jugador != jugador:
            print(self.mensaje_invalido + " La torre que quiere mover es de su rival!")
            return False
        elif (super().checkear_y(y_0, y_1) and not super().checkear_x(x_0, x_1)) or (not super().checkear_y(y_0, y_1) and super().checkear_x(x_0, x_1)):
            return True
        else:
            print("La torre no puede realizar ese movimiento")
            return False

class Torre_promocionada(Pieza):

    pieza = "+R"

    def __init__(self, jugador):
        super().__init__(jugador)

class Alfil(Pieza):

    pieza = "B "

    def __init__(self, jugador):
        super().__init__(jugador)

class Alfil_promocionado(Pieza):

    pieza = "+B"

    def __init__(self, jugador):
        super().__init__(jugador)

class General_dorado(Pieza):

    pieza = "G "

    def __init__(self, jugador):
        super().__init__(jugador)

class General_plateado(Pieza):

    pieza = "S "

    def __init__(self, jugador):
        super().__init__(jugador)

class General_plateado_promocionado(Pieza):

    pieza = "+S"

    def __init__(self, jugador):
        super().__init__(jugador)

class Caballo(Pieza):

    pieza = "N "

    def __init__(self, jugador):
        super().__init__(jugador)

class Caballo_promocionado(Pieza):

    pieza = "+N"

    def __init__(self, jugador):
        super().__init__(jugador)

class Lancero(Pieza):

    pieza = "L "

    def __init__(self, jugador):
        super().__init__(jugador)

class Lancero_promocionado(Pieza):

    pieza = "+L"

    def __init__(self, jugador):
        super().__init__(jugador)


class Peon(Pieza):

    pieza = "P "

    def __init__(self, jugador):
        super().__init__(jugador)


    def checkear_movimiento(self, x_0, y_0, x_1, y_1, jugador):
        if self.jugador != jugador:
            print(self.mensaje_invalido + " El peon que quiere mover es de su rival!")
            return False
        elif(self.jugador.color == "blancas"):
            if x_0 == (x_1 + 1) and y_0 == y_1:
                return True
            else:
                print(self.mensaje_invalido + " El peon no puede realizar ese movimiento")
                return False
        elif(self.jugador.color == "negras"):
            if x_0 == (x_1 - 1) and y_0 == y_1:
                return True
            else:
                print(self.mensaje_invalido + " El peon no puede realizar ese movimiento")
                return False
        return False


class Peon_promocionado(Pieza):

    pieza = "+P"

    def __init__(self, jugador):
        super().__init__(jugador)
