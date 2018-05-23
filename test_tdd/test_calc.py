import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(4, Calculator.add(2, 2))
        self.assertEqual(7, Calculator.add(3, 4))
        self.assertNotEqual(8, Calculator.add(8, 8))

    def test_substract(self):
        self.assertEqual(8, Calculator.substract(10, 2))
        self.assertEqual(12, Calculator.substract(2, -10))

    def test_divide(self):
        self.assertEqual(5, Calculator.divide(25, 5))

    def test_miltiply(self):
        self.assertEqual(100, Calculator.multiply(10, 10))

if __name__ == '__main__':
    unittest.main()
