import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Test cases for add()
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(5, 7), 12)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-3, -7), -10)

    # Test cases for subtract()
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -10), 5)

    # Test cases for multiply()
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)

    # Test cases for divide()
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(15, 3), 5)

    def test_divide_non_divisible_numbers(self):
        self.assertEqual(self.calc.divide(7, 2), 3)  # 7 ÷ 2 = 3 remainder 1

    # Test cases for modulo()
    def test_modulo_positive_numbers(self):
        self.assertEqual(self.calc.modulo(10, 4), 2)

    def test_modulo_with_larger_divisor(self):
        self.assertEqual(self.calc.modulo(3, 7), 3)  # 3 % 7 = 3

if __name__ == '__main__':
    unittest.main()
