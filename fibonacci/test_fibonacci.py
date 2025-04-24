import unittest
from fibonacci import fibonacci_recursivo, fibonacci_iterativo

class TestFibonacciRecursivo(unittest.TestCase):
    def test_fibonacci_recursivo(self):
        self.assertEqual(fibonacci_recursivo(0), 0)
        self.assertEqual(fibonacci_recursivo(1), 1)
        self.assertEqual(fibonacci_recursivo(2), 1)
        self.assertEqual(fibonacci_recursivo(3), 2)
        self.assertEqual(fibonacci_recursivo(4), 3)
        self.assertEqual(fibonacci_recursivo(5), 5)
        self.assertEqual(fibonacci_recursivo(6), 8)
        self.assertEqual(fibonacci_recursivo(7), 13)
        self.assertEqual(fibonacci_recursivo(10), 55)

    def test_fibonacci_recursivo_negativo(self):
        with self.assertRaises(ValueError):
            fibonacci_recursivo(-1)
        with self.assertRaises(ValueError):
            fibonacci_recursivo(-5)
        with self.assertRaises(ValueError):
            fibonacci_recursivo(-10)

class TestFibonacciIterativo(unittest.TestCase):
    def test_fibonacci_iterativo(self):
        self.assertEqual(fibonacci_iterativo(0), 0)
        self.assertEqual(fibonacci_iterativo(1), 1)
        self.assertEqual(fibonacci_iterativo(2), 1)
        self.assertEqual(fibonacci_iterativo(3), 2)
        self.assertEqual(fibonacci_iterativo(4), 3)
        self.assertEqual(fibonacci_iterativo(5), 5)
        self.assertEqual(fibonacci_iterativo(6), 8)
        self.assertEqual(fibonacci_iterativo(7), 13)
        self.assertEqual(fibonacci_iterativo(10), 55)

    def test_fibonacci_iterativo_negativo(self):
        with self.assertRaises(ValueError):
            fibonacci_iterativo(-1)
        with self.assertRaises(ValueError):
            fibonacci_iterativo(-5)
        with self.assertRaises(ValueError):
            fibonacci_iterativo(-10)

class TestFibonacciRecursivo(unittest.TestCase): #pedi mas tests para ver que estuviera bien 
    def test_fibonacci_recursivo_numeros_altos(self):
        self.assertEqual(fibonacci_recursivo(15), 610)
        self.assertEqual(fibonacci_recursivo(20), 6765)

    def test_fibonacci_recursivo_edge_cases(self):
        self.assertEqual(fibonacci_recursivo(8), 21)
        self.assertEqual(fibonacci_recursivo(9), 34)
        self.assertEqual(fibonacci_recursivo(11), 89)


class TestFibonacciIterativo(unittest.TestCase):
    def test_fibonacci_iterativo_numeros_altos(self):
        self.assertEqual(fibonacci_iterativo(15), 610)
        self.assertEqual(fibonacci_iterativo(20), 6765)

    def test_fibonacci_iterativo_edge_cases(self):
        self.assertEqual(fibonacci_iterativo(8), 21)
        self.assertEqual(fibonacci_iterativo(9), 34)
        self.assertEqual(fibonacci_iterativo(11), 89)
if __name__ == "__main__":
    unittest.main()

