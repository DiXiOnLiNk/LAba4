import unittest
from calculactor import Calculator  # Припускаю, що клас Calculator знаходиться в файлі calculator.py

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator(5, 3)
        self.assertEqual(calc.add(), 8)

    def test_sub(self):
        calc = Calculator(5, 3)
        self.assertEqual(calc.sub(), 2)

    def test_mul(self):
        calc = Calculator(5, 3)
        self.assertEqual(calc.mul(), 15)

    def test_div(self):
        calc = Calculator(6, 3)
        self.assertEqual(calc.div(), 2)

    def test_div_by_zero(self):
        calc = Calculator(6, 0)
        self.assertEqual(calc.div(), "Error: Division by zero!")

    def test_power(self):
        calc = Calculator(2, 3)
        self.assertEqual(calc.power(), 8)

    def test_power_with_zero_exponent(self):
        calc = Calculator(5, 0)
        self.assertEqual(calc.power(), 1)

    def test_gcd(self):
        calc = Calculator(24, 36)
        self.assertEqual(calc.gcd(), 12)

    def test_lcm(self):
        calc = Calculator(24, 36)
        self.assertEqual(calc.lcm(), 72)

    def test_lcm_with_negative_numbers(self):
        calc = Calculator(-24, 36)
        self.assertEqual(calc.lcm(), 72)

    def test_lcm_with_zero(self):
        calc = Calculator(24, 0)
        self.assertEqual(calc.lcm(), 0)

if __name__ == '__main__':
    unittest.main()
