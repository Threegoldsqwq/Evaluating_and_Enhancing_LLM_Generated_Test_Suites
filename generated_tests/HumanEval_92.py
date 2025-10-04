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
    def test_non_integer_input_one_float(self):
            # Test cases where only one input is a float, ensuring the early exit branch is taken.
            self.assertFalse(any_int(5.0, 2, 3))
            self.assertFalse(any_int(2, 5.0, 3))
            self.assertFalse(any_int(2, 3, 5.0))

    def test_non_integer_input_multiple_floats(self):
            # Test cases with two or three float inputs.
            self.assertFalse(any_int(5.0, 2.0, 3))
            self.assertFalse(any_int(5, 2.0, 3.0))
            self.assertFalse(any_int(5.0, 2, 3.0))
            self.assertFalse(any_int(5.0, 2.0, 3.0))

    def test_non_integer_input_mixed_types(self):
            # Test cases with non-numeric types, which should also trigger the early exit.
            self.assertFalse(any_int("5", 2, 3))
            self.assertFalse(any_int(1, "2", 3))
            self.assertFalse(any_int(1, 2, "3"))
            self.assertFalse(any_int(None, 2, 3))
            self.assertFalse(any_int([1], 2, 3))
            self.assertFalse(any_int({1: 1}, 2, 3))

    def test_all_integers_no_sum_relationship(self):
            # Test cases where all inputs are integers, but none is the sum of the other two.
            self.assertFalse(any_int(1, 2, 4))
            self.assertFalse(any_int(10, 20, 5))
            self.assertFalse(any_int(0, 0, 1)) # None of the zeroes sum up to 1
            self.assertFalse(any_int(1, 0, 0))
            self.assertFalse(any_int(0, 1, 0))
            self.assertFalse(any_int(-1, -2, -4)) # All negatives, no sum
            self.assertFalse(any_int(1, 5, 10))
            self.assertFalse(any_int(-5, -2, 1)) # Mixed signs, no sum

    def test_true_cases_with_zeros_negatives_and_order_variations(self):
            # Test cases that should return True, including various combinations of zeros and negative numbers,
            # and checking all three possible sum arrangements (x=y+z, y=x+z, z=x+y).
            self.assertTrue(any_int(0, 0, 0)) # 0 = 0 + 0
            self.assertTrue(any_int(5, 0, 5)) # 5 = 0 + 5 (x = y+z)
            self.assertTrue(any_int(0, 5, 5)) # 5 = 0 + 5 (y = x+z)
            self.assertTrue(any_int(5, 5, 0)) # 5 = 5 + 0 (z = x+y)

            self.assertTrue(any_int(-5, -2, -3)) # -5 = -2 + -3 (x = y+z)
            self.assertTrue(any_int(-2, -5, -3)) # -5 = -2 + -3 (y = x+z)
            self.assertTrue(any_int(-3, -2, -5)) # -5 = -3 + -2 (z = x+y)

            self.assertTrue(any_int(5, -2, 7))   # 5 = -2 + 7 (x = y+z)
            self.assertTrue(any_int(7, -2, 5))   # 7 = -2 + 5 (y = x+z)
            self.assertTrue(any_int(-2, 5, 7))   # 7 = -2 + 5 (z = x+y)
            self.assertTrue(any_int(10, -5, 5))  # 5 = 10 + -5 (z = x+y)
            self.assertTrue(any_int(1, -2, 3))   # 1 = -2 + 3 (x = y+z)

    def test_boolean_inputs_as_integers(self):
            # Booleans are instances of int (True=1, False=0), so they should pass the type check
            # and be evaluated based on their integer values.
            self.assertTrue(any_int(True, 1, 0)) # True (1) == 1 + 0
            self.assertTrue(any_int(1, True, 0)) # 1 == True (1) + 0
            self.assertTrue(any_int(1, 0, True)) # 1 == 0 + True (1)
            self.assertFalse(any_int(False, 1, 2)) # False (0) != 1 + 2; 1 != 0 + 2; 2 != 0 + 1
            self.assertFalse(any_int(True, 2, 3)) # True (1) != 2 + 3; 2 != 1 + 3; 3 != 1 + 2
