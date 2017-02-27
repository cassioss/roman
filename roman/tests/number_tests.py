import unittest
from roman.number import *


class TestRomanToNumber(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(1,    to_number('I'))
        self.assertEqual(5,    to_number('V'))
        self.assertEqual(10,   to_number('X'))
        self.assertEqual(50,   to_number('L'))
        self.assertEqual(100,  to_number('C'))
        self.assertEqual(500,  to_number('D'))
        self.assertEqual(1000, to_number('M'))

    def test_combos_with_V(self):
        self.assertEqual(4, to_number('IV'))
        self.assertEqual(5, to_number('V'))
        self.assertEqual(6, to_number('VI'))
        self.assertEqual(7, to_number('VII'))
        self.assertEqual(8, to_number('VIII'))

    def test_combos_with_X(self):
        self.assertEqual(9,  to_number('IX'))
        self.assertEqual(10, to_number('X'))
        self.assertEqual(11, to_number('XI'))
        self.assertEqual(14, to_number('XIV'))
        self.assertEqual(19, to_number('XIX'))

    def test_combos_with_L(self):
        self.assertEqual(40, to_number('XL'))
        self.assertEqual(70, to_number('LXX'))
        self.assertEqual(84, to_number('LXXXIV'))

    def test_combos_with_M(self):
        self.assertEqual(3888, to_number('MMMDCCCLXXXVIII'))
        self.assertEqual(3999, to_number('MMMCMXCIX'))


if __name__ == '__main__':
    unittest.main()
