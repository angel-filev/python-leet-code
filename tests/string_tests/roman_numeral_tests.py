import unittest
from strings.roman_numeral import RomanNumeral


class TestRomanToInt(unittest.TestCase):
    def test_roman_to_int_III(self):
        self.assertEqual(RomanNumeral.roman_to_int("III"), 3)

    def test_roman_to_int_LVIII(self):
        self.assertEqual(RomanNumeral.roman_to_int("LVIII"), 58)

    def test_roman_to_int_MCMXCIV(self):
        self.assertEqual(RomanNumeral.roman_to_int("MCMXCIV"), 1994)

    def test_roman_to_int_IV(self):
        self.assertEqual(RomanNumeral.roman_to_int("IV"), 4)

    def test_roman_to_int_IX(self):
        self.assertEqual(RomanNumeral.roman_to_int("IX"), 9)

    def test_roman_to_int_XL(self):
        self.assertEqual(RomanNumeral.roman_to_int("XL"), 40)

    def test_roman_to_int_XC(self):
        self.assertEqual(RomanNumeral.roman_to_int("XC"), 90)

    def test_roman_to_int_CD(self):
        self.assertEqual(RomanNumeral.roman_to_int("CD"), 400)

    def test_roman_to_int_CM(self):
        self.assertEqual(RomanNumeral.roman_to_int("CM"), 900)

    def test_int_to_roman_3(self):
        self.assertEqual(RomanNumeral.int_to_roman(3), 'III')

    def test_int_to_roman_58(self):
        self.assertEqual(RomanNumeral.int_to_roman(58), 'LVIII')

    def test_int_to_roman_1994(self):
        self.assertEqual(RomanNumeral.int_to_roman(1994), 'MCMXCIV')

    def test_int_to_roman_4(self):
        self.assertEqual(RomanNumeral.int_to_roman(4), 'IV')

    def test_int_to_roman_9(self):
        self.assertEqual(RomanNumeral.int_to_roman(9), 'IX')

    def test_int_to_roman_40(self):
        self.assertEqual(RomanNumeral.int_to_roman(40), 'XL')

    def test_int_to_roman_90(self):
        self.assertEqual(RomanNumeral.int_to_roman(90), 'XC')

    def test_int_to_roman_400(self):
        self.assertEqual(RomanNumeral.int_to_roman(400), 'CD')

    def test_int_to_roman_900(self):
        self.assertEqual(RomanNumeral.int_to_roman(900), 'CM')


if __name__ == '__main__':
    unittest.main()
