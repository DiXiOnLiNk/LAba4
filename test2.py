import unittest
from calculactor import Calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        calc = Calculator(5, 3)
        self.assertEqual(calc.add(), 8)
        calc = Calculator(10.5, -2.5)
        self.assertEqual(calc.add(), 8)

    def test_subtraction(self):
        calc = Calculator(10, 4)
        self.assertEqual(calc.sub(), 6)
        calc = Calculator(7.5, -2.5)
        self.assertEqual(calc.sub(), 10)

    def test_multiplication(self):
        calc = Calculator(3, 4)
        self.assertEqual(calc.mul(), 12)
        calc = Calculator(-5, -2)
        self.assertEqual(calc.mul(), 10)

    def test_division(self):
        calc = Calculator(10, 5)
        self.assertEqual(calc.div(), 2)
        calc = Calculator(8, 0)
        self.assertEqual(calc.div(), "Помилка: Ділення на нуль!")

    def test_power(self):
        calc = Calculator(2, 3)
        self.assertEqual(calc.power(), 8)
        calc = Calculator(5, 0)
        self.assertEqual(calc.power(), 1)

    def test_gcd(self):
        calc = Calculator(24, 36)
        self.assertEqual(calc.gcd(), 12)
        calc = Calculator(17, 23)
        self.assertEqual(calc.gcd(), 1)

    def test_lcm(self):
        calc = Calculator(6, 8)
        self.assertEqual(calc.lcm(), 24)
        calc = Calculator(15, 25)
        self.assertEqual(calc.lcm(), 75)

if __name__ == '__main__':
    unittest.main()
