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
    def test_single_even_digit_other_than_4(self):
            # Test case: Smallest positive integer with only an even digit (other than 4)
            self.assertEqual(self.solution.digits(2), 0)

    def test_number_with_zero_and_odd_digits(self):
            # Test case: Number contains zero (which is even) and other odd digits
            self.assertEqual(self.solution.digits(103), 3)
            self.assertEqual(self.solution.digits(501), 5)
            self.assertEqual(self.solution.digits(207), 7)

    def test_number_with_zero_and_all_even_digits(self):
            # Test case: Number contains zero and all other digits are even
            self.assertEqual(self.solution.digits(204), 0)
            self.assertEqual(self.solution.digits(806), 0)

    def test_all_odd_digits_multi_digit(self):
            # Test case: A number composed entirely of odd digits
            self.assertEqual(self.solution.digits(135), 15)
            self.assertEqual(self.solution.digits(97531), 945)

    def test_all_even_digits_multi_digit(self):
            # Test case: A number composed entirely of even digits
            self.assertEqual(self.solution.digits(246), 0)
            self.assertEqual(self.solution.digits(8642), 0)

    def test_mixed_digits_leading_even_trailing_odd(self):
            # Test case: Mixed even and odd digits, starting with even and ending with odd
            self.assertEqual(self.solution.digits(2345), 15)
            self.assertEqual(self.solution.digits(8123), 3)

    def test_single_odd_digit_in_many_evens(self):
            # Test case: Only one odd digit surrounded by even digits
            self.assertEqual(self.solution.digits(82146), 1)
            self.assertEqual(self.solution.digits(26850), 5)

    def test_product_involving_one_digit(self):
            # Test case: Number contains '1' as an odd digit, ensuring it multiplies correctly
            self.assertEqual(self.solution.digits(1), 1)
            self.assertEqual(self.solution.digits(123), 3) # 1 * 3 = 3
            self.assertEqual(self.solution.digits(11), 1)
