import unittest

# Assume the function is_equal_to_sum_even(n) is defined elsewhere.
# For evaluation purposes, the logic is:
# A number n can be written as the sum of exactly 4 positive even numbers
# if and only if n is an even number and n >= 8.
# (e.g., n = 2 + 2 + 2 + (n - 6). For this to work, n-6 must be a positive even number.
# If n is even, n-6 is even. If n >= 8, then n-6 >= 2, making it positive.)

class TestIsEqualToSumEven(unittest.TestCase):

    def test_example_four_false(self):
        """Test with n=4, which should be False as per example."""
        self.assertFalse(is_equal_to_sum_even(4))

    def test_example_six_false(self):
        """Test with n=6, which should be False as per example."""
        self.assertFalse(is_equal_to_sum_even(6))

    def test_example_eight_true(self):
        """Test with n=8, which should be True as per example (minimum valid sum: 2+2+2+2)."""
        self.assertTrue(is_equal_to_sum_even(8))

    def test_zero_false(self):
        """Test with n=0, which is less than 8."""
        self.assertFalse(is_equal_to_sum_even(0))

    def test_small_even_below_minimum_false(self):
        """Test with n=2, which is less than 8."""
        self.assertFalse(is_equal_to_sum_even(2))

    def test_odd_below_minimum_false(self):
        """Test with n=7, which is odd and less than 8."""
        self.assertFalse(is_equal_to_sum_even(7))

    def test_odd_above_minimum_false(self):
        """Test with n=9, which is above 8 but is odd."""
        self.assertFalse(is_equal_to_sum_even(9))

    def test_valid_case_ten_true(self):
        """Test with n=10, a valid case (e.g., 2+2+2+4)."""
        self.assertTrue(is_equal_to_sum_even(10))

    def test_valid_case_twelve_true(self):
        """Test with n=12, a valid case (e.g., 2+2+4+4)."""
        self.assertTrue(is_equal_to_sum_even(12))

    def test_large_even_true(self):
        """Test with a larger even number n=100."""
        self.assertTrue(is_equal_to_sum_even(100))

    def test_n_less_than_8(self):
            # Test cases for n < 8 (should all return False)
            self.assertFalse(is_equal_to_sum_even(0), "n=0 should return False (too small)")
            self.assertFalse(is_equal_to_sum_even(2), "n=2 should return False (too small)")
            self.assertFalse(is_equal_to_sum_even(6), "n=6 should return False (too small and even)")
            self.assertFalse(is_equal_to_sum_even(7), "n=7 should return False (too small and odd)")
            self.assertFalse(is_equal_to_sum_even(-4), "n=-4 should return False (negative and too small)")

    def test_n_odd_and_greater_than_or_equal_to_8(self):
            # Test cases for n >= 8 but n is odd (should all return False)
            self.assertFalse(is_equal_to_sum_even(9), "n=9 should return False (odd number)")
            self.assertFalse(is_equal_to_sum_even(15), "n=15 should return False (odd number)")
            self.assertFalse(is_equal_to_sum_even(101), "n=101 should return False (odd number)")

    def test_n_even_and_greater_than_or_equal_to_8(self):
            # Test cases for n >= 8 and n is even (should all return True)
            self.assertTrue(is_equal_to_sum_even(8), "n=8 should return True (minimum valid sum)")
            self.assertTrue(is_equal_to_sum_even(10), "n=10 should return True")
            self.assertTrue(is_equal_to_sum_even(12), "n=12 should return True")
            self.assertTrue(is_equal_to_sum_even(100), "n=100 should return True (large even number)")
            self.assertTrue(is_equal_to_sum_even(2000), "n=2000 should return True (very large even number)")
# To run these tests, you would typically have the is_equal_to_sum_even function defined.
# For instance:
# def is_equal_to_sum_even(n):
#     return n >= 8 and n % 2 == 0

# if __name__ == '__main__':
#     unittest.main()