<<<<<<< HEAD
 
=======
import unittest
from calculator import Calculator
class TestCalculator(unittest.TestCase):
    def test_add(self):
        calculator =Calculator(4, 5)
        self.assertEqual(calculator.add(), 9)

    def test_sub(self):
        calculator = Calculator(10, 3)
        self.assertEqual(calculator.sub(), 7)

    def test_mul(self):
        calculator = Calculator(7, 6)
        self.assertEqual(calculator.mul(), 42)

    def test_div(self):
        calculator = Calculator(20, 4)
        self.assertEqual(calculator.div(), 5)
    
    def test_division_by_zero(self):
        calculator = Calculator(10, 0)
        self.assertEqual(calculator.div(), "Error: Division by zero!")
    def test_power(self):
        calculator = Calculator(3, 4)
        self.assertEqual(calculator.power(), 81)

    def test_gcd(self):
        calculator = Calculator(24, 36)
        self.assertEqual(calculator.gcd(), 12)

    def test_lcm(self):
        calculator = Calculator(4, 6)
        self.assertEqual(calculator.lcm(), 12)

    def test_lcm_negative(self):
        calculator = Calculator(-4, 6)
        self.assertEqual(calculator.lcm(), 12)

  
if __name__ == '__main__':
    unittest.main()
<<<<<<< HEAD
>>>>>>> 0503bfe (break)
=======

>>>>>>> 17b7558 (break)
