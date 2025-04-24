import unittest
from factorial import factorial_iterativo, factorial_recursivo

class TestFactorial_recursivo(unittest.TestCase):
    def test_factorial_recursivo(self):
        self.assertEqual(factorial_recursivo(0), 1)
        self.assertEqual(factorial_recursivo(1), 1)
        self.assertEqual(factorial_recursivo(5), 120)
        self.assertEqual(factorial_recursivo(7), 5040)

    def test_factorial_iterativo(self):
        self.assertEqual(factorial_iterativo(0), 1)
        self.assertEqual(factorial_iterativo(1), 1)
        self.assertEqual(factorial_iterativo(5), 120)
        self.assertEqual(factorial_iterativo(7), 5040)


class TestFactorial_iterativo(unittest.TestCase):
    

    def test_with_20(self):
        n = 20
        result = factorial_iterativo(n)
        self.assertEqual(result, 2432902008176640000)
    def test_with_0(self):
        n = 0
        result = factorial_iterativo(n)
        self.assertEqual(result, 1)
    def test_with_1(self):
        n = 1
        result = factorial_iterativo(n)
        self.assertEqual(result, 1)
    def test_with_more_than_1(self):
        n = 2
        result = factorial_iterativo(n)
        self.assertEqual(result, 2)
        
# mas test para probar otros casos 

class TestFactorial_iterativo(unittest.TestCase):
    def test_with_3(self):
        n = 3
        result = factorial_iterativo(n)
        self.assertEqual(result, 6)

    def test_with_4(self):
        n = 4
        result = factorial_iterativo(n)
        self.assertEqual(result, 24)

    def test_with_6(self):
        n = 6
        result = factorial_iterativo(n)
        self.assertEqual(result, 720)

class TestFactorial_recursivo(unittest.TestCase):
    def test_with_3(self):
        n = 3
        result = factorial_recursivo(n)
        self.assertEqual(result, 6)

    def test_with_4(self):
        n = 4
        result = factorial_recursivo(n)
        self.assertEqual(result, 24)

    def test_with_6(self):
        n = 6
        result = factorial_recursivo(n)
        self.assertEqual(result, 720)

#test para casos especiales de 0 y numeros negativos 
class TestFactorialSpecialCases(unittest.TestCase):
    def test_negative_number_iterativo(self):
        with self.assertRaises(ValueError):
            factorial_iterativo(-5)

    def test_negative_number_recursivo(self):
        with self.assertRaises(ValueError):
            factorial_recursivo(-5)

    def test_zero_iterativo(self):
        self.assertEqual(factorial_iterativo(0), 1)

    def test_zero_recursivo(self):
        self.assertEqual(factorial_recursivo(0), 1)


if __name__ == "__main__":
    unittest.main()