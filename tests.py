import unittest
from clases.tablero import *

class TestJuego(unittest.TestCase):
    def setUp(self):
        self.blancas = Jugador("blancas")
        self.negras = Jugador("negras")
        self.tablero = Tablero(self.blancas, self.blancas)

    def test_peon(self):
        self.assertFalse(Peon(self.blancas).checkear_movimiento(1, 2, 2, 3, self.blancas, True), "Movimiento diagonal")
        self.assertTrue(Peon(self.negras).checkear_movimiento(1,2,2,2, self.negras, True), "Movimiento hacia abajo")
        self.assertTrue(Peon(self.blancas).checkear_movimiento(3, 5, 2, 5, self.blancas, True), "Movimiento hacia arriba")
        self.assertFalse(Peon(self.blancas).checkear_movimiento(3, 7, 4, 2, self.negras, True), "Peon rival")

    def test_alfil(self):
        self.assertTrue(Alfil(self.blancas).checkear_movimiento(1, 2, 4, 5, self.blancas, True), "Movimiento diagonal")
        self.assertFalse(Alfil(self.negras).checkear_movimiento(1, 2, 2, 2, self.negras, True), "Movimiento hacia abajo")
        self.assertFalse(Alfil(self.blancas).checkear_movimiento(3, 5, 2, 5, self.blancas, True), "Movimiento hacia arriba")

    def test_torre(self):
        self.assertTrue(Torre(self.blancas).checkear_movimiento(0, 0, 0, 8, self.blancas, True), "Movimiento horizontal")
        self.assertTrue(Torre(self.negras).checkear_movimiento(1, 1, 7, 1, self.negras, True), "Movimiento vertical")
        self.assertFalse(Torre(self.blancas).checkear_movimiento(1, 2, 3, 6, self.blancas, True), "Movimiento invalido")

    def test_caballo(self):
        self.assertTrue(Caballo(self.blancas).checkear_movimiento(8, 7, 6, 6, self.blancas, True), "Movimiento en L")
        self.assertTrue(Caballo(self.negras).checkear_movimiento(0, 3, 2, 4, self.negras, True), "Movimiento en L")
        self.assertFalse(Caballo(self.blancas).checkear_movimiento(2, 3, 6, 7, self.blancas, True), "Movimiento en diagonal")

    def test_pieza_bloqueando_paso(self):
        self.assertFalse(self.tablero.checkear_camino(0, 0, 2, 2), "Torre bloqueando el paso")
        self.assertTrue(self.tablero.checkear_camino(3, 3, 5, 3), "Camino libre")

    def test_casillas_fuera_rango(self):
        self.assertTrue(self.tablero.checkear_limites(0,2,5,7), "Casilla dentro de los limites")
        self.assertFalse(self.tablero.checkear_limites(10,15,0,7), "Casilla fuera de los limites")

    def test_seguimiento_rey(self):
        #Primero muevo el rey a [7,4] para checkear que el tablero lo trackee correctamente
        self.tablero.actualizar_tablero(self.blancas, 8, 4 , 7, 4)
        self.assertTrue(self.tablero.rey_blancas == [7,4], "Posicion rey blancas")
        self.assertFalse(self.tablero.rey_blancas == [2,3], "Aca no esta el rey de las blancas")

    def test_checkear_jaque(self):
        # Creo un alfil para probar que el rey este en jaque
        self.tablero.tablero[2][2] = Alfil(self.blancas)
        self.assertTrue(self.tablero.checkear_jaque(self.negras), "El alfil de la pos 2, 2 pone a las negras en jaque")
        self.assertFalse(self.tablero.checkear_jaque(self.blancas), "Las blancas no estan en ajque")

    def test_promocion(self):
        self.assertTrue(esta_en_zona_promocionable(self.blancas, 6, 2))
        self.assertFalse(esta_en_zona_promocionable(self.negras, 3, 4))

    def test_captura(self):
        ## como un peon de las blancas y dps checkeo si esta siendo trackeado por las negras
        peon = self.tablero.tablero[6][1]
        caballo = self.tablero.tablero[7][1]
        self.tablero.remover_pieza(self.negras, 6, 1)
        self.assertTrue(peon in self.tablero.negras.piezas_capturadas, "Peon recien capturado")
        self.assertFalse(caballo in self.tablero.negras.piezas_capturadas, "Caballo nunca fue capturado")







