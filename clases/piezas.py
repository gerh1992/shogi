class Pieza():

    piezas_capturadas = []

    def __init__(self, jugador):
        self.jugador = jugador


class Rey(Pieza):

    pieza = "K "

    def __init__(self, jugador):
        super().__init__(jugador)


class Torre(Pieza):

    pieza = "R "

    def __init__(self, jugador):
        super().__init__(jugador)

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



class Peon_promocionado(Pieza):

    pieza = "+P"

    def __init__(self, jugador):
        super().__init__(jugador)
