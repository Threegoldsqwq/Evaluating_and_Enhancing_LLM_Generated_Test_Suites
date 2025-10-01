import unittest

class TestBelowZero(unittest.TestCase):

    def test_all_positive_operations(self):
        # Balance starts at 0, only positive operations.
        # Expected: False (never goes below zero)
        self.assertFalse(below_zero([1, 2, 3]))

    def test_mixed_operations_stays_positive(self):
        # Balance starts at 0, mixed operations, but never dips below zero.
        # Expected: False (never goes below zero)
        self.assertFalse(below_zero([10, -5, 3, -8])) # 0 -> 10 -> 5 -> 8 -> 0

    def test_starts_with_negative_operation(self):
        # Balance starts at 0, first operation is a withdrawal that makes it negative.
        # Expected: True (immediately goes below zero)
        self.assertTrue(below_zero([-1, 2, 3]))

    def test_goes_below_zero_in_middle(self):
        # Balance goes below zero after some initial positive operations.
        # Expected: True
        self.assertTrue(below_zero([1, 2, -4, 5])) # 0 -> 1 -> 3 -> -1

    def test_ends_at_zero_but_never_below(self):
        # Balance ends at zero, but never dipped below zero during operations.
        # Expected: False
        self.assertFalse(below_zero([5, -2, -3])) # 0 -> 5 -> 3 -> 0

    def test_empty_operations_list(self):
        # No operations, balance remains 0.
        # Expected: False
        self.assertFalse(below_zero([]))

    def test_only_zero_operations(self):
        # Operations are all zeros, balance remains 0.
        # Expected: False
        self.assertFalse(below_zero([0, 0, 0]))

    def test_large_numbers_going_below_zero(self):
        # Test with larger numbers where a large withdrawal makes it negative.
        # Expected: True
        self.assertTrue(below_zero([100, -50, -60])) # 0 -> 100 -> 50 -> -10

    def test_large_numbers_staying_above_zero(self):
        # Test with large numbers where it stays positive.
        # Expected: False
        self.assertFalse(below_zero([1000, -500, -499])) # 0 -> 1000 -> 500 -> 1

    def test_multiple_dips_first_is_below_zero(self):
        # Balance goes below zero, then recovers, then potentially goes below again.
        # The function should return True at the first instance it goes below.
        # Expected: True
        self.assertTrue(below_zero([5, -10, 20, -30])) # 0 -> 5 -> -5 (returns True here)