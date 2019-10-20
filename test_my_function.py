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



if __name__ == '__main__':

    unittest.main()



