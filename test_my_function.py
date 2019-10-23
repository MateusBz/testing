import unittest

import my_functions


class TestAdd(unittest.TestCase):
    def test_add_int(self):
        self.assertEqual(my_functions.add(3, 5), 8)
        self.assertEqual(my_functions.add(5, 5), 10)

    def test_add_float(self):
        self.assertAlmostEqual(my_functions.add(2.25, 3.13), 5.38)
        self.assertAlmostEqual(my_functions.add(1.15, 2.15), 3.3)

    def test_add_string(self):
        self.assertEqual(my_functions.add('adc', 'de'), 'adcde')
        self.assertEqual(my_functions.add('', ''), '')
        self.assertEqual(my_functions.add('3', '3'), '33')


class TestDivide(unittest.TestCase):
    def test_value_error(self):
        """Test if value error is rised needed"""
        self.assertRaises(ValueError, my_functions.divide, 3, 0)
        self.assertRaises(ValueError, my_functions.divide, 0, 0)

    def test_divide_int(self):
        self.assertEqual(my_functions.divide(10, 5), 2)
        self.assertEqual(my_functions.divide(10, 20), 0.5)
        self.assertAlmostEqual(my_functions.divide(10, 3), 3.33333333333)

    def test_divide_float(self):
        self.assertAlmostEqual(my_functions.divide(2.2, 1.1), 2)
        self.assertAlmostEqual(my_functions.divide(3.5, 1.1), 3.18181818)
        self.assertAlmostEqual(my_functions.divide(5.3, 3.4), 1.55882353)


class TestSubtract(unittest.TestCase):
    def test_subtract_int(self):
        self.assertEqual(my_functions.subtract(2, 5), 10)
        self.assertEqual(my_functions.subtract(2, 3), 6)
        self.assertEqual(my_functions.subtract(10, 3), 30)

    def test_subtract_float(self):
        self.assertAlmostEqual(my_functions.subtract(2.2, 3.6), 7.92)
        self.assertAlmostEqual(my_functions.subtract(7.7, 2.3), 17.71)

    def test_subtract_string_and_int(self):
        self.assertEqual(my_functions.subtract('aka', 3), 'akaakaaka')
        self.assertEqual(my_functions.subtract('ak', 3), 'akakak')

    def test_subtract_value_error(self):
        self.assertRaises(TypeError, my_functions.subtract, 'ala', 'kot')
        self.assertRaises(TypeError, my_functions.subtract, 'abc', 'kba')


class TestSquare(unittest.TestCase):
    def test_value_error(self):
        self.assertRaises(ValueError, my_functions.square, -1)
        self.assertRaises(ValueError, my_functions.square, -12)

    def test_square_int(self):
        self.assertEqual(my_functions.square(4), 2)
        self.assertEqual(my_functions.square(100), 10)

    def test_square_float(self):
        self.assertAlmostEqual(my_functions.square(9.3), 3.04959014)
        self.assertAlmostEqual(my_functions.square(100.89), 10.0444014)

    def test_square_string(self):
        self.assertRaises(TypeError, my_functions.square, 'ala', 'kot')
        self.assertRaises(TypeError, my_functions.square, 'pies', 'kot')


if __name__ == '__main__':

    unittest.main()



