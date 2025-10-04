import unittest

class TestPairsSumToZero(unittest.TestCase):

    def test_basic_positive_case(self):
        # Test case with a clear pair summing to zero (5 and -5)
        self.assertTrue(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))

    def test_basic_negative_case(self):
        # Test case where no pair sums to zero, including a zero element
        self.assertFalse(pairs_sum_to_zero([1, 3, 5, 0]))

    def test_empty_list(self):
        # Test with an empty list
        self.assertFalse(pairs_sum_to_zero([]))

    def test_single_element_list(self):
        # Test with a list containing only one element
        self.assertFalse(pairs_sum_to_zero([1]))

    def test_two_distinct_zeroes(self):
        # Test case where two distinct zero elements exist
        self.assertTrue(pairs_sum_to_zero([0, 5, -3, 0]))

    def test_zero_present_no_other_zero_or_opposite(self):
        # Test case where zero is present but no other element forms a sum-to-zero pair
        self.assertFalse(pairs_sum_to_zero([0, 1, 2, 3]))

    def test_all_positive_numbers(self):
        # Test case with only positive numbers
        self.assertFalse(pairs_sum_to_zero([1, 2, 3, 4, 5]))

    def test_all_negative_numbers(self):
        # Test case with only negative numbers
        self.assertFalse(pairs_sum_to_zero([-1, -2, -3, -4, -5]))

    def test_multiple_pairs_sum_to_zero(self):
        # Test case with multiple pairs that sum to zero
        self.assertTrue(pairs_sum_to_zero([1, -1, 2, -2, 3]))

    def test_no_pair_with_duplicate_non_opposite_numbers(self):
        # Test case where numbers might appear multiple times but no distinct pair sums to zero
        self.assertFalse(pairs_sum_to_zero([1, 3, -2, 1]))