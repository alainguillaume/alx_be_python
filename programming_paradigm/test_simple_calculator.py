import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
         self.assertEqual(self.calc.add(2, 3), 5)
         self.assertEqual(self.calc.add(-1, 1), 0)
         self.assertEqual(self.calc.add(-1, -1), -2)


    def test_subStract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)




    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)


    def test_devide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(-1, -1), 1)

        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)
        



if __name__ == "__main__":
    unittest.main()

