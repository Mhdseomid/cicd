# test_subtract.py

import unittest
from negative import subtract_numbers

class TestSubtract(unittest.TestCase):

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract_numbers(5, 3), 2)
        self.assertEqual(subtract_numbers(10, 5), 5)
        self.assertEqual(subtract_numbers(0, 5), -5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract_numbers(-2, -3), 1)
        self.assertEqual(subtract_numbers(-5, -10), 5)
        self.assertEqual(subtract_numbers(-2, 4), -6)

if __name__ == '__main__':
    unittest.main()
