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
    def test_non_integer_types_ignored(self):
            # Test that floats are correctly ignored
            self.assertEqual(double_the_difference([1, 2.5, 3, 4.0, 5]), 1*1 + 3*3 + 5*5) # Only integers 1, 3, 5 are considered. Result: 1 + 9 + 25 = 35
            self.assertEqual(double_the_difference([2.0, 4.0, 6.0]), 0) # All floats, should be ignored

            # Test that strings are correctly ignored
            self.assertEqual(double_the_difference([1, "foo", 3, "bar", 5]), 1*1 + 3*3 + 5*5) # Only integers 1, 3, 5 are considered. Result: 1 + 9 + 25 = 35
            self.assertEqual(double_the_difference(["a", "b", "c"]), 0) # All strings, should be ignored

            # Test that None is correctly ignored
            self.assertEqual(double_the_difference([1, None, 3]), 1*1 + 3*3) # Only integers 1, 3 are considered. Result: 1 + 9 = 10
            self.assertEqual(double_the_difference([None, None]), 0) # All None, should be ignored

            # Test with a mix of various non-integer types
            self.assertEqual(double_the_difference([1, 2.5, "abc", None, -3, 5]), 1*1 + 5*5) # Only 1 and 5 are odd, non-negative integers. Result: 1 + 25 = 26

    def test_booleans_as_integers(self):
            # Test that True (which is 1) is treated as an odd integer and False (which is 0) as an even integer
            self.assertEqual(double_the_difference([True, False]), 1*1) # True (1) is odd, False (0) is even. Result: 1
            self.assertEqual(double_the_difference([False, False]), 0) # Both False (0) are even. Result: 0
            self.assertEqual(double_the_difference([True, True]), 1*1 + 1*1) # Both True (1) are odd. Result: 2

    def test_comprehensive_mixed_inputs(self):
            # This test combines all types of inputs to ensure all branches are hit
            # - Negative integers (-10, -5): Ignored by num >= 0
            # - Even non-negative integers (0, 2): Ignored by num % 2 != 0
            # - Floats (3.14, 2.0): Ignored by isinstance(num, int)
            # - Strings ('hello', 'world'): Ignored by isinstance(num, int)
            # - None: Ignored by isinstance(num, int)
            # - Boolean True (1): Processed as odd, non-negative integer
            # - Odd positive integers (1, 7, 9): Processed
            test_list = [-10, 0, 2, 3.14, 'hello', 1, 7, None, -5, True, 9, 2.0, 'world']
            expected_result = 1*1 + 7*7 + True*True + 9*9 # 1 (from 1) + 49 (from 7) + 1 (from True) + 81 (from 9)
            self.assertEqual(double_the_difference(test_list), expected_result) # Result: 1 + 49 + 1 + 81 = 132
