import unittest

class TestIntToMiniRoman(unittest.TestCase):

    def test_single_digit_basic(self):
        self.assertEqual(int_to_mini_roman(1), 'i')

    def test_single_digit_additive(self):
        self.assertEqual(int_to_mini_roman(3), 'iii')

    def test_single_digit_subtractive(self):
        self.assertEqual(int_to_mini_roman(4), 'iv')

    def test_tens_subtractive(self):
        self.assertEqual(int_to_mini_roman(9), 'ix')

    def test_mixed_tens_and_ones(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')

    def test_tens_and_ones_complex(self):
        self.assertEqual(int_to_mini_roman(42), 'xlii')

    def test_complex_double_digit(self):
        self.assertEqual(int_to_mini_roman(99), 'xcix')

    def test_hundreds_and_mixed(self):
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

    def test_nearly_maximum_complex(self):
        self.assertEqual(int_to_mini_roman(999), 'cmxcix')

    def test_maximum_value(self):
        self.assertEqual(int_to_mini_roman(1000), 'm')