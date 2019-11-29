from clases.jugador import Jugador
from clases.tablero import Tablero

jugador_negras = Jugador("negras")
jugador_blancas = Jugador("blancas")
tablero = Tablero(jugador_negras, jugador_blancas)


while not tablero.checkear_ganador():
    tablero.jugar()
