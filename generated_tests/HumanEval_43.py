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
    def test_single_zero(self):
            # Test case: List with a single zero, should return False as no distinct pair sums to zero.
            self.assertFalse(pairs_sum_to_zero([0]))

    def test_only_negative_numbers_no_pair(self):
            # Test case: List containing only negative numbers, with no pair summing to zero.
            # Ensures the loop completes and returns False correctly for negative-only inputs.
            self.assertFalse(pairs_sum_to_zero([-1, -2, -3, -4]))

    def test_mixed_numbers_with_zero_no_pair(self):
            # Test case: A diverse list including positive, negative, and a single zero,
            # where no pair sums to zero. This ensures the function handles various number types
            # and correctly returns False after iterating through the whole list.
            self.assertFalse(pairs_sum_to_zero([1, -2, 3, 0, -4, 5]))

    def test_pair_with_duplicates_and_other_numbers(self):
            # Test case: A list with duplicates and other numbers, where a pair sums to zero.
            # This checks that the logic correctly identifies a pair even when other numbers are repeated.
            self.assertTrue(pairs_sum_to_zero([1, 5, -5, 5, 10]))

    def test_pair_at_end_of_long_list(self):
            # Test case: A long list where the pair that sums to zero is found towards the very end.
            # Ensures that the function processes all elements correctly up to the point a pair is found.
            self.assertTrue(pairs_sum_to_zero([10, 20, 30, -1, 5, 8, -5]))

    def test_no_pair_with_duplicates(self):
            # Test case: A list with duplicate numbers, but no pair sums to zero.
            # Ensures duplicates themselves don't trigger a false positive.
            self.assertFalse(pairs_sum_to_zero([1, 1, 2, 2, -3, -3]))
