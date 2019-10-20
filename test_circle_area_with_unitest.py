import unittest

import math

import circle


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        """Test area when radius >= 0"""
        self.assertAlmostEqual(circle.circle_area(1), math.pi)
        self.assertAlmostEqual(circle.circle_area(2.1), math.pi*(2.1**2))

    def test_values(self):
        self.assertRaises(ValueError, circle.circle_area, -2)

    def test_type(self):
        self.assertRaises(TypeError, circle.circle_area, 3+5j)
        self.assertRaises(TypeError, circle.circle_area, True)
        self.assertRaises(TypeError, circle.circle_area, 'radius')


if __name__ == '__main__':
    unittest.main()