# OOP de piezas.
# Logica de juegoA
# tablero
# Restricciones
# checkeo de estados(ganador y jaques(?))

from clases.jugador import Jugador
from clases.tablero import Tablero

jugador_negras = Jugador("German", "negras")
jugador_blancas = Jugador("Asd", "blancas")
tablero = Tablero(jugador_negras, jugador_blancas)


while not tablero.checkear_ganador():
    tablero.jugar()
