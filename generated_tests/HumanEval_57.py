import unittest

# Assume the 'monotonic' function is defined elsewhere, e.g.:
# def monotonic(lst):
#     if not lst or len(lst) == 1:
#         return True
#
#     is_increasing = True
#     is_decreasing = True
#
#     for i in range(len(lst) - 1):
#         if lst[i] > lst[i+1]:
#             is_increasing = False
#         if lst[i] < lst[i+1]:
#             is_decreasing = False
#
#     return is_increasing or is_decreasing

class TestMonotonic(unittest.TestCase):

    def test_increasing_positive(self):
        """Test a list that is strictly increasing with positive numbers."""
        self.assertTrue(monotonic([1, 2, 4, 20]))

    def test_decreasing_positive(self):
        """Test a list that is strictly decreasing with positive numbers."""
        self.assertTrue(monotonic([20, 4, 2, 1]))

    def test_mixed_not_monotonic(self):
        """Test a list that is neither increasing nor decreasing."""
        self.assertFalse(monotonic([1, 20, 4, 10]))

    def test_empty_list(self):
        """Test an empty list (should be True)."""
        self.assertTrue(monotonic([]))

    def test_single_element_list(self):
        """Test a list with a single element (should be True)."""
        self.assertTrue(monotonic([5]))

    def test_increasing_negative_and_zero(self):
        """Test a list that is strictly increasing with negative numbers and zero."""
        self.assertTrue(monotonic([-10, -5, -2, 0]))

    def test_decreasing_negative_and_zero(self):
        """Test a list that is strictly decreasing with negative numbers and zero."""
        self.assertTrue(monotonic([0, -2, -5, -10]))

    def test_non_decreasing_with_duplicates(self):
        """Test a list that is non-decreasing (monotonic increasing with duplicates)."""
        self.assertTrue(monotonic([1, 2, 2, 3, 3, 4]))

    def test_non_increasing_with_duplicates(self):
        """Test a list that is non-increasing (monotonic decreasing with duplicates)."""
        self.assertTrue(monotonic([4, 3, 3, 2, 2, 1]))

    def test_not_monotonic_peak(self):
        """Test a list that increases then decreases (not monotonic)."""
        self.assertFalse(monotonic([1, 5, 2, 0]))
    def test_all_elements_identical(self):
            # Test case where all elements are identical, making it both increasing and decreasing
            self.assertTrue(monotonic([7, 7, 7, 7]))
            self.assertTrue(monotonic([0, 0, 0]))
            self.assertTrue(monotonic([-5, -5]))

    def test_float_monotonic_increasing(self):
            # Test with floating-point numbers, increasing
            self.assertTrue(monotonic([1.1, 2.2, 3.3, 4.4]))
            self.assertTrue(monotonic([1.0, 1.0, 2.0, 3.0]))

    def test_float_monotonic_decreasing(self):
            # Test with floating-point numbers, decreasing
            self.assertTrue(monotonic([4.4, 3.3, 2.2, 1.1]))
            self.assertTrue(monotonic([3.0, 2.0, 1.0, 1.0]))

    def test_float_non_monotonic(self):
            # Test with floating-point numbers, non-monotonic
            self.assertFalse(monotonic([1.1, 2.2, 1.5]))
            self.assertFalse(monotonic([5.0, 3.0, 4.0, 1.0]))

    def test_two_element_lists(self):
            # Test edge cases with exactly two elements
            self.assertTrue(monotonic([10, 20]))  # Increasing
            self.assertTrue(monotonic([20, 10]))  # Decreasing
            self.assertTrue(monotonic([15, 15]))  # Identical

    def test_longer_non_monotonic_sequences(self):
            # Test longer sequences that are clearly non-monotonic
            self.assertFalse(monotonic([1, 2, 5, 3, 4]))
            self.assertFalse(monotonic([5, 4, 1, 3, 2]))
