import unittest

class TestAnyInt(unittest.TestCase):

    def test_positive_integers_sum_match(self):
        # Example 1: One number is the sum of the other two, all positive integers.
        self.assertTrue(any_int(5, 2, 7))

    def test_mixed_integers_sum_match(self):
        # Example 3: One number is the sum of the other two, mixed positive and negative integers.
        self.assertTrue(any_int(3, -2, 1))

    def test_integers_no_sum_match(self):
        # Example 2: All integers, but no number is the sum of the other two.
        self.assertFalse(any_int(3, 2, 2))

    def test_float_input(self):
        # Example 4: One or more inputs are floats.
        self.assertFalse(any_int(3.6, -2.2, 2))

    def test_zero_and_positive_sum_match(self):
        # Test with zero, where sum condition is met.
        self.assertTrue(any_int(0, 5, 5))

    def test_negative_integers_sum_match(self):
        # Test with negative integers where sum condition is met.
        self.assertTrue(any_int(-5, -2, -3))

    def test_all_equal_integers_no_sum_match(self):
        # All integers are equal, sum condition not met.
        self.assertFalse(any_int(5, 5, 5))

    def test_all_different_integers_no_sum_match(self):
        # All different integers, no sum condition met.
        self.assertFalse(any_int(4, 5, 6))

    def test_one_float_with_integer_value(self):
        # One number is a float, even if its value is an integer (e.g., 7.0).
        self.assertFalse(any_int(5, 2, 7.0))

    def test_mixed_types_no_sum_match(self):
        # Mixed types with floats, no sum condition met.
        self.assertFalse(any_int(1.0, 2, 3.5))