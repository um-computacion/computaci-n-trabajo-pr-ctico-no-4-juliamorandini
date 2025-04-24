import unittest
from flatten import flatten

class PruebasAplanar(unittest.TestCase):
    def test_lista_simple(self):
        lista = [1, 2, 3, 4]
        esperado = [1, 2, 3, 4]
        self.assertEqual(flatten(lista), esperado)

    def test_lista_anidada(self):
        lista = [1, [2, 3], [4, [5, 6]]]
        esperado = [1, 2, 3, 4, 5, 6]
        self.assertEqual(flatten(lista), esperado)

    def test_estructuras_mixtas(self):
        lista = [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]
        esperado = [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]
        self.assertEqual(flatten(lista), esperado)

    def test_lista_vacia(self): #como siempre pedi mas tests para chequear que funcionara
        lista = []
        esperado = []
        self.assertEqual(flatten(lista), esperado)

    def test_lista_con_elementos_vacios(self):
        lista = [[], [1, 2], [], [3, [4, []]]]
        esperado = [1, 2, 3, 4]
        self.assertEqual(flatten(lista), esperado)

    def test_lista_con_tipos_varios(self):
        lista = [1, "texto", [3.14, [True, None]], (5, 6)]
        esperado = [1, "texto", 3.14, True, None, 5, 6]
        self.assertEqual(flatten(lista), esperado)

    def test_lista_con_niveles_profundos(self):
        lista = [1, [2, [3, [4, [5, [6]]]]]]
        esperado = [1, 2, 3, 4, 5, 6]
        self.assertEqual(flatten(lista), esperado)

    def test_lista_con_diccionarios(self):
        lista = [{"a": 1, "b": 2}, [3, {"c": 4}], 5]
        esperado = ["a", 1, "b", 2, 3, "c", 4, 5]
        self.assertEqual(flatten(lista), esperado)

    def test_lista_con_tuplas_anidadas(self):
        lista = [(1, 2), [3, (4, 5)], 6]
        esperado = [1, 2, 3, 4, 5, 6]
        self.assertEqual(flatten(lista), esperado)

    def test_lista_con_elementos_repetidos(self):
        lista = [1, [1, [1, [1]]]]
        esperado = [1, 1, 1, 1]
        self.assertEqual(flatten(lista), esperado)

    def test_lista_con_elementos_no_iterables(self):
        lista = [1, [2, 3], 4, None]
        esperado = [1, 2, 3, 4, None]
        self.assertEqual(flatten(lista), esperado)

if __name__ == "__main__":
    unittest.main()