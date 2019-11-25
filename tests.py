import unittest
from clases.tablero import *

class TestJuego(unittest.TestCase):
    def setUp(self):
        self.blancas = Jugador("blancas")
        self.negras = Jugador("negras")
        self.tablero = Tablero(self.blancas, self.blancas)

    def tests_peon(self):
        self.assertFalse(Peon(self.blancas).checkear_movimiento(1, 2, 2, 3, self.blancas, True), "Movimiento diagonal")
        self.assertTrue(Peon(self.negras).checkear_movimiento(1,2,2,2, self.negras, True), "Movimiento hacia abajo")
        self.assertTrue(Peon(self.blancas).checkear_movimiento(3, 5, 2, 5, self.blancas, True), "Movimiento hacia arriba")
        self.assertFalse(Peon(self.blancas).checkear_movimiento(3, 7, 4, 2, self.negras, True), "Peon rival")

    def tests_alfil(self):
        self.assertTrue(Alfil(self.blancas).checkear_movimiento(1, 2, 4, 5, self.blancas, True), "Movimiento diagonal")
        self.assertFalse(Alfil(self.negras).checkear_movimiento(1, 2, 2, 2, self.negras, True), "Movimiento hacia abajo")
        self.assertFalse(Alfil(self.blancas).checkear_movimiento(3, 5, 2, 5, self.blancas, True), "Movimiento hacia arriba")

    def tests_torre(self):
        self.assertTrue(Torre(self.blancas).checkear_movimiento(0, 0, 0, 8, self.blancas, True), "Movimiento horizontal")
        self.assertTrue(Torre(self.negras).checkear_movimiento(1, 1, 7, 1, self.negras, True), "Movimiento vertical")
        self.assertFalse(Torre(self.blancas).checkear_movimiento(1, 2, 3, 6, self.blancas, True), "Movimiento invalido")

    def test_caballo(self):
        self.assertTrue(Caballo(self.blancas).checkear_movimiento(8, 7, 6, 6, self.blancas, True), "Movimiento en L")
        self.assertTrue(Caballo(self.negras).checkear_movimiento(0, 3, 2, 4, self.negras, True), "Movimiento en L")
        self.assertFalse(Caballo(self.blancas).checkear_movimiento(2, 3, 6, 7, self.blancas, True), "Movimiento en diagonal")

    def tests_pieza_bloqueando_paso(self):
        self.assertFalse(self.tablero.checkear_camino(0, 0, 2, 2), "Torre bloqueando el paso")
        self.assertTrue(self.tablero.checkear_camino(3, 3, 5, 3), "Camino libre")

    def casillas_fuera_rango(self):
        self.assertTrue(self.tablero.checkear_limites(0,2,5,7), "Casilla dentro de los limites")
        self.assertFalse(self.tablero.checkear_limites(10,15,0,7), "Casilla fuera de los limites")






