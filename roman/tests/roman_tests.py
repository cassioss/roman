import unittest
from roman.roman import *


class TestNumberToRoman(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual('I', to_roman(1))
        self.assertEqual('V', to_roman(5))
        self.assertEqual('X', to_roman(10))
        self.assertEqual('L', to_roman(50))
        self.assertEqual('C', to_roman(100))
        self.assertEqual('D', to_roman(500))
        self.assertEqual('M', to_roman(1000))

    def test_out_of_bounds(self):
        with self.assertRaises(ValueError):
            to_roman(0)

        with self.assertRaises(ValueError):
            to_roman(4000)

        with self.assertRaises(ValueError):
            to_roman(9999)

    def test_combos_with_I(self):
        self.assertEqual('II', to_roman(2))
        self.assertEqual('III', to_roman(3))

    def test_combos_with_V(self):
        self.assertEqual('IV', to_roman(4))
        self.assertEqual('V', to_roman(5))
        self.assertEqual('VI', to_roman(6))
        self.assertEqual('VII', to_roman(7))
        self.assertEqual('VIII', to_roman(8))

    def test_combos_with_X(self):
        self.assertEqual('IX', to_roman(9))
        self.assertEqual('X', to_roman(10))
        self.assertEqual('XI', to_roman(11))
        self.assertEqual('XIV', to_roman(14))
        self.assertEqual('XIX', to_roman(19))

    def test_combos_with_L(self):
        self.assertEqual('XL', to_roman(40))
        self.assertEqual('LXX', to_roman(70))
        self.assertEqual('LXXXIV', to_roman(84))

    def test_combos_with_M(self):
        self.assertEqual('MMMDCCCLXXXVIII', to_roman(3888))
        self.assertEqual('MMMCMXCIX', to_roman(3999))


if __name__ == '__main__':
    unittest.main()
