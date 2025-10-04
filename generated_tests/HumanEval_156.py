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
    def test_invalid_inputs_raise_value_error(self):
            # Test cases for num less than the minimum allowed (1)
            with self.assertRaisesRegex(ValueError, "Input number must be between 1 and 1000, inclusive."):
                int_to_mini_roman(0)
            with self.assertRaisesRegex(ValueError, "Input number must be between 1 and 1000, inclusive."):
                int_to_mini_roman(-5)

            # Test cases for num greater than the maximum allowed (1000)
            with self.assertRaisesRegex(ValueError, "Input number must be between 1 and 1000, inclusive."):
                int_to_mini_roman(1001)
            with self.assertRaisesRegex(ValueError, "Input number must be between 1 and 1000, inclusive."):
                int_to_mini_roman(2000)

    def test_missing_single_symbol_conversions(self):
            # Test cases for specific Roman numeral symbols not explicitly covered by docstring examples
            self.assertEqual(int_to_mini_roman(900), 'cm') # CM (900)
            self.assertEqual(int_to_mini_roman(500), 'd')  # D (500)
            self.assertEqual(int_to_mini_roman(90), 'xc')  # XC (90)
            self.assertEqual(int_to_mini_roman(40), 'xl')  # XL (40)
            self.assertEqual(int_to_mini_roman(4), 'iv')   # IV (4)

    def test_various_combinations_and_edge_cases(self):
            # Test cases for numbers that combine various symbols and check repetitions
            self.assertEqual(int_to_mini_roman(2), 'ii')
            self.assertEqual(int_to_mini_roman(3), 'iii')
            self.assertEqual(int_to_mini_roman(6), 'vi')
            self.assertEqual(int_to_mini_roman(7), 'vii')
            self.assertEqual(int_to_mini_roman(8), 'viii')
            self.assertEqual(int_to_mini_roman(11), 'xi')
            self.assertEqual(int_to_mini_roman(14), 'xiv')
            self.assertEqual(int_to_mini_roman(29), 'xxix')
            self.assertEqual(int_to_mini_roman(39), 'xxxix')
            self.assertEqual(int_to_mini_roman(49), 'xlix') # XL + IX
            self.assertEqual(int_to_mini_roman(89), 'lxxxix') # L + XXX + IX
            self.assertEqual(int_to_mini_roman(99), 'xcix')  # XC + IX
            self.assertEqual(int_to_mini_roman(101), 'ci')
            self.assertEqual(int_to_mini_roman(399), 'cccxcix') # CCC + XC + IX
            self.assertEqual(int_to_mini_roman(499), 'cdxcix')  # CD + XC + IX
            self.assertEqual(int_to_mini_roman(899), 'dcccxcix') # D + CCC + XC + IX
            self.assertEqual(int_to_mini_roman(999), 'cmxcix')  # CM + XC + IX
