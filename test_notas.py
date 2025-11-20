import unittest
from notas import calcular_promedio, estado_estudiante, obtener_letra

class TestSistemaNotas(unittest.TestCase):

    def test_calculo_promedio_simple(self):
        mis_notas = [3.0, 4.0, 5.0]
        self.assertEqual(calcular_promedio(mis_notas), 4.0)

    def test_promedio_vacio(self):
        self.assertEqual(calcular_promedio([]), 0.0)

    def test_estado_aprobado(self):
        self.assertEqual(estado_estudiante(3.5), "APROBADO")

    def test_estado_reprobado(self):
        self.assertEqual(estado_estudiante(2.9), "REPROBADO")

    def test_letra_excelente(self):
        self.assertEqual(obtener_letra(4.8), 'A')

if __name__ == '__main__':
    unittest.main()