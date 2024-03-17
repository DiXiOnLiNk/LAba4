<<<<<<< HEAD
 
=======
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator(10, 5)

    def test_add(self):
        self.assertEqual(self.calc.add(), 15)

    def test_sub(self):
        self.assertEqual(self.calc.sub(), 5)

    def test_mul(self):
        self.assertEqual(self.calc.mul(), 50)

    def test_div(self):
        self.assertEqual(self.calc.div(), 2)

    def test_div_by_zero(self):
        calc = Calculator(10, 0)
        self.assertRaises(ZeroDivisionError, calc.div)

    def test_power(self):
        self.assertEqual(self.calc.power(), 100000)

    def test_gcd(self):
        self.assertEqual(self.calc.gcd(), 5)

    def test_add_negative_numbers(self):
        calc = Calculator(-10, -5)
        self.assertEqual(calc.add(), -15)

    def test_sub_negative_numbers(self):
        calc = Calculator(-10, -5)
        self.assertEqual(calc.sub(), -5)

    def test_mul_negative_numbers(self):
        calc = Calculator(-10, -5)
        self.assertEqual(calc.mul(), 50)

    def test_div_negative_numbers(self):
        calc = Calculator(-10, -5)
        self.assertEqual(calc.div(), 2)

    def test_add_zero(self):
        calc = Calculator(0, 5)
        self.assertEqual(calc.add(), 5)

if __name__ == '__main__':
    unittest.main()
>>>>>>> 0503bfe (break)
