import unittest

class TestDoubleTheDifference(unittest.TestCase):

    def test_example_basic_mixed(self):
        # Example from the problem description: positive odd and even integers
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)

    def test_empty_list(self):
        # Edge case: empty list
        self.assertEqual(double_the_difference([]), 0)

    def test_only_positive_odd_integers(self):
        # List containing only valid numbers
        self.assertEqual(double_the_difference([5, 7, 1]), 75) # 25 + 49 + 1

    def test_only_positive_even_integers(self):
        # List containing only even integers, should return 0
        self.assertEqual(double_the_difference([2, 4, 0, 8]), 0)

    def test_with_negative_integers(self):
        # Negative numbers should be ignored
        self.assertEqual(double_the_difference([-1, -3, -2, 5]), 25) # only 5 is valid

    def test_mixed_all_conditions(self):
        # A complex list with positive, negative, odd, even, and non-integers
        self.assertEqual(double_the_difference([9, -2, 1, 4, -5, 3.5, 7.0]), 82) # 9*9 + 1*1 = 81 + 1

    def test_list_with_zero_only(self):
        # Zero is even, so it should not contribute to the sum
        self.assertEqual(double_the_difference([0]), 0)

    def test_list_with_non_integer_values(self):
        # Floats and other non-integers should be ignored
        self.assertEqual(double_the_difference([1.5, 3.0, 2, 5, "hello"]), 25) # only 5 is valid

    def test_single_positive_odd_number(self):
        # Single valid number
        self.assertEqual(double_the_difference([7]), 49) # 7*7

    def test_single_negative_odd_number(self):
        # Single negative number, should be ignored
        self.assertEqual(double_the_difference([-9]), 0)