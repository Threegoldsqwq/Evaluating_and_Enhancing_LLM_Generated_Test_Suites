import unittest

class TestDigitsProduct(unittest.TestCase):

    def test_single_odd_digit(self):
        self.assertEqual(digits(1), 1)

    def test_single_even_digit(self):
        self.assertEqual(digits(4), 0)

    def test_multiple_all_odd_digits(self):
        self.assertEqual(digits(135), 15)

    def test_multiple_all_even_digits(self):
        self.assertEqual(digits(246), 0)

    def test_mixed_digits_with_odd(self):
        self.assertEqual(digits(235), 15)

    def test_mixed_digits_with_odd_and_one(self):
        self.assertEqual(digits(123), 3)

    def test_number_containing_zero_as_even(self):
        self.assertEqual(digits(103), 3)

    def test_larger_number_mixed(self):
        self.assertEqual(digits(72831), 21) # 7 * 3 * 1

    def test_all_ones(self):
        self.assertEqual(digits(1111), 1)

    def test_number_with_nine(self):
        self.assertEqual(digits(987), 63) # 9 * 7