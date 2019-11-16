# OOP de piezas.
# Logica de juego
# tablero
# Restricciones
# checkeo de estados(ganador y jaques(?))

from clases.jugador import  Jugador
from clases.tablero import Tablero

jugador1 = Jugador("German", "blue")
jugador2 = Jugador("Asd", "red")
tablero = Tablero(jugador1, jugador2)
x_0 = int(input("desde x"))
y_0 = int(input("desde y"))
x_1 = int(input("hasta x"))
y_1 = int(input("hasta y"))
print(tablero.checkear_limites(x_0,y_0,x_1,y_1))

tablero.mostrar_tablero()
