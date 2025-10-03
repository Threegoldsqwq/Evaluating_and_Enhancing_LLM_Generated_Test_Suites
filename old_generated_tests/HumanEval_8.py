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