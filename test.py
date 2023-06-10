# test_negative.py

import unittest
from negative import Negative

class TestNegative(unittest.TestCase):
    def setUp(self):
        self.negative = Negative()

    def test_negative_one(self):
        result = self.negative.negate(1)
        self.assertEqual(result, -1)

    def test_negative_zero(self):
        result = self.negative.negate(0)
        self.assertEqual(result, 0)

    def test_negative_negative(self):
        result = self.negative.negate(-5)
        self.assertEqual(result, 5)

    def test_negative_float(self):
        result = self.negative.negate(3.14)
        self.assertEqual(result, -3.14)

if __name__ == '__main__':
    unittest.main()
