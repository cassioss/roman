import unittest
from roman.number import to_number
from roman.roman import to_roman


class TestRomanAndNumberConversion(unittest.TestCase):

    # Basic test function - it evaluates both conversions at the same time,
    # saving time when checking for valid cases on both algorithms
    def evaluate_pair(self, num, roman):
        self.assertEqual(roman, to_roman(num))
        self.assertEqual(num, to_number(roman))

    def test_basic_cases(self):
        self.evaluate_pair(1,    'I')
        self.evaluate_pair(5,    'V')
        self.evaluate_pair(10,   'X')
        self.evaluate_pair(50,   'L')
        self.evaluate_pair(100,  'C')
        self.evaluate_pair(500,  'D')
        self.evaluate_pair(1000, 'M')

    def test_combos_with_V(self):
        self.evaluate_pair(4, 'IV')
        self.evaluate_pair(5, 'V')
        self.evaluate_pair(6, 'VI')
        self.evaluate_pair(7, 'VII')
        self.evaluate_pair(8, 'VIII')

    def test_combos_with_X(self):
        self.evaluate_pair(9,  'IX')
        self.evaluate_pair(10, 'X')
        self.evaluate_pair(11, 'XI')
        self.evaluate_pair(14, 'XIV')
        self.evaluate_pair(19, 'XIX')

    def test_combos_with_L(self):
        self.evaluate_pair(40, 'XL')
        self.evaluate_pair(49, 'XLIX')
        self.evaluate_pair(51, 'LI')
        self.evaluate_pair(59, 'LIX')
        self.evaluate_pair(70, 'LXX')
        self.evaluate_pair(84, 'LXXXIV')

    def test_combos_with_M(self):
        self.evaluate_pair(3888, 'MMMDCCCLXXXVIII')
        self.evaluate_pair(3999, 'MMMCMXCIX')

    def test_number_out_of_bounds(self):
        with self.assertRaises(ValueError):
            to_roman(0)

        with self.assertRaises(ValueError):
            to_roman(4000)

        with self.assertRaises(ValueError):
            to_roman(9999)


if __name__ == '__main__':
    unittest.main()
