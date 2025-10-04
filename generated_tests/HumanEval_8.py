import unittest

class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        # Test case for an empty list, should return (0, 1) as per requirements.
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_positive_element(self):
        # Test case for a list with a single positive integer.
        self.assertEqual(sum_product([5]), (5, 5))

    def test_multiple_positive_elements(self):
        # Test case for a list with multiple positive integers.
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_single_negative_element(self):
        # Test case for a list with a single negative integer.
        self.assertEqual(sum_product([-7]), (-7, -7))

    def test_multiple_negative_elements(self):
        # Test case for a list with multiple negative integers.
        self.assertEqual(sum_product([-1, -2, -3]), (-6, -6))

    def test_mixed_positive_and_negative_elements(self):
        # Test case for a list containing both positive and negative integers.
        self.assertEqual(sum_product([-1, 2, -3, 4]), (2, 24))

    def test_list_with_zero(self):
        # Test case for a list containing a zero. Product should be zero.
        self.assertEqual(sum_product([1, 0, 3, 5]), (9, 0))

    def test_list_with_multiple_zeros(self):
        # Test case for a list containing multiple zeros. Product should be zero.
        self.assertEqual(sum_product([0, 2, 0, 4]), (6, 0))

    def test_large_numbers(self):
        # Test case with larger numbers to ensure correct calculations.
        self.assertEqual(sum_product([100, 20, 5]), (125, 10000))

    def test_all_same_numbers(self):
        # Test case where all numbers in the list are identical.
        self.assertEqual(sum_product([3, 3, 3, 3]), (12, 81))
    def test_empty_list(self):
            # This covers the base case of an empty list, ensuring the initial sum (0) and product (1) are returned.
            # This also exercises the 'for' loop not being entered.
            self.assertEqual(self.solution_function([]), (0, 1))

    def test_single_zero_element(self):
            # Tests the specific edge case of a list containing only a single zero.
            self.assertEqual(self.solution_function([0]), (0, 0))

    def test_all_negative_integers(self):
            # Tests a list composed solely of negative integers to verify sum and product behavior.
            self.assertEqual(self.solution_function([-1, -2, -3]), (-6, -6))

    def test_list_with_multiple_zeros(self):
            # Ensures correct behavior when multiple zeros are present within the list, making the product zero.
            self.assertEqual(self.solution_function([1, 0, 2, 0, 3]), (6, 0))

    def test_large_positive_numbers(self):
            # Tests with larger numbers to ensure Python's arbitrary-precision integers are handled correctly.
            self.assertEqual(self.solution_function([100000, 200000]), (300000, 20000000000))

    def test_mixed_zero_positive_negative_sum_is_zero(self):
            # Tests a scenario with mixed positive, negative, and zero values where the sum is zero.
            self.assertEqual(self.solution_function([-5, 0, 5, 10]), (10, 0))
