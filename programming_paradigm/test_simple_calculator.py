import unittest
from simple_calculator import SimpleCalculator

class testCalculation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(SimpleCalculator.add(self, 10,5), 15)


    def test_substract(self):
        self.assertEqual(SimpleCalculator.subtract(self, 10,5), 5)


    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(self, 10,5), 50)


    def test_devide(self):
        self.assertEqual(SimpleCalculator.divide(self, 10,5), 2)
        



if __name__ == "__main__":
    unittest.main()

