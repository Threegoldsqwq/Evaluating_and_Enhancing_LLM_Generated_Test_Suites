import unittest

class TestHasCloseElements(unittest.TestCase):

    def test_no_close_elements_basic(self):
        # Basic case: no elements are closer than the threshold
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_has_close_elements_basic(self):
        # Basic case: elements exist that are closer than the threshold
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_empty_list(self):
        # Edge case: empty list should always return False
        self.assertFalse(has_close_elements([], 1.0))

    def test_single_element_list(self):
        # Edge case: list with only one element should always return False
        self.assertFalse(has_close_elements([10.0], 0.1))

    def test_elements_exactly_at_threshold(self):
        # Elements whose difference is exactly equal to the threshold should not count (strict inequality)
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 1.0))
        self.assertFalse(has_close_elements([1.0, 2.0], 1.0))

    def test_elements_just_under_threshold(self):
        # Elements whose difference is just slightly less than the threshold
        self.assertTrue(has_close_elements([1.0, 1.999, 3.0], 1.0))
        self.assertTrue(has_close_elements([5.0, 5.001], 0.002))

    def test_duplicate_elements(self):
        # Duplicate elements have a difference of 0, which is always less than any positive threshold
        self.assertTrue(has_close_elements([1.0, 5.0, 1.0, 8.0], 0.001))
        self.assertTrue(has_close_elements([7.0, 7.0], 100.0))

    def test_negative_numbers_close(self):
        # Test with negative numbers where some are close
        self.assertTrue(has_close_elements([-5.0, -4.8, -3.0], 0.3))
        self.assertTrue(has_close_elements([-10.0, -10.05, -12.0], 0.1))

    def test_mixed_positive_negative_no_close(self):
        # Test with mixed positive and negative numbers, no close elements
        self.assertFalse(has_close_elements([-10.0, -5.0, 0.0, 5.0, 10.0], 1.0))
        self.assertFalse(has_close_elements([-2.0, 0.0, 2.0], 1.0))

    def test_larger_list_complex_values(self):
        # Test with a larger list and more complex float values
        self.assertTrue(has_close_elements([0.1, 0.2, 0.3, 0.4, 0.5, 0.55], 0.06))
        self.assertFalse(has_close_elements([100.0, 100.5, 101.0, 101.5], 0.4))
    def test_diff_equals_threshold_is_false(self):
            # Test case where the absolute difference is exactly equal to the threshold.
            # It should return False because the condition is strictly less than (`<`).
            self.assertFalse(has_close_elements([1.0, 2.0], 1.0))
            self.assertFalse(has_close_elements([5.0, 5.5], 0.5))
            self.assertFalse(has_close_elements([-1.0, 0.0], 1.0))

    def test_diff_just_above_threshold_is_false(self):
            # Test case where the absolute difference is infinitesimally greater than the threshold.
            # Should return False.
            self.assertFalse(has_close_elements([1.0, 2.0000000001], 1.0))
            self.assertFalse(has_close_elements([5.0, 5.5000000001], 0.5))
            self.assertFalse(has_close_elements([-1.0, -1.0 + 1.0000000001], 1.0))

    def test_diff_just_below_threshold_is_true(self):
            # Test case where the absolute difference is infinitesimally less than the threshold.
            # Should return True.
            self.assertTrue(has_close_elements([1.0, 1.9999999999], 1.0))
            self.assertTrue(has_close_elements([5.0, 5.4999999999], 0.5))
            self.assertTrue(has_close_elements([-1.0, -0.0000000001], 1.0)) # Abs diff approx 0.9999... < 1.0

    def test_all_elements_same_returns_true(self):
            # If all elements are identical, their difference is 0, which is less than any positive threshold.
            self.assertTrue(has_close_elements([5.0, 5.0, 5.0], 0.1))
            self.assertTrue(has_close_elements([0.0, 0.0, 0.0, 0.0], 1e-9))

    def test_with_negative_numbers(self):
            # Test with lists containing only negative numbers.
            self.assertTrue(has_close_elements([-1.0, -0.5, -0.6], 0.2)) # Sorted: [-1.0, -0.6, -0.5], |-0.5 - (-0.6)| = 0.1 < 0.2
            self.assertFalse(has_close_elements([-10.0, -8.0, -5.0], 1.0))
            self.assertTrue(has_close_elements([-10.0, -9.9, -5.0], 0.2)) # Sorted: [-10.0, -9.9, -5.0], |-9.9 - (-10.0)| = 0.1 < 0.2

    def test_with_mixed_positive_and_negative_numbers(self):
            # Test with lists containing both positive and negative numbers.
            self.assertTrue(has_close_elements([-2.0, 1.0, -1.5], 0.6)) # Sorted: [-2.0, -1.5, 1.0], |-1.5 - (-2.0)| = 0.5 < 0.6
            self.assertFalse(has_close_elements([-5.0, 0.0, 5.0], 1.0))
            self.assertTrue(has_close_elements([-0.1, 0.1, 0.0], 0.15)) # Sorted: [-0.1, 0.0, 0.1], |0.0 - (-0.1)| = 0.1 < 0.15

    def test_with_large_and_small_numbers(self):
            # Test with very large or very small floating-point numbers.
            self.assertTrue(has_close_elements([1e9, 1e9 + 0.5], 1.0))
            self.assertFalse(has_close_elements([1e18, 1e18 + 10.0], 5.0))
            self.assertTrue(has_close_elements([1.23456789e-5, 1.23456790e-5], 1e-9)) # Diff is 1e-13, Threshold 1e-9. True.
            self.assertTrue(has_close_elements([1.23456789e5, 1.23456790e5], 1.0)) # Diff is 1e-3, Threshold 1.0. True.

    def test_threshold_is_zero(self):
            # If threshold is 0, no two numbers can be closer than 0 (unless their difference is strictly negative, which is impossible for math.fabs).
            # The condition `diff < threshold` means `diff < 0`, which is always False for non-negative diff.
            self.assertFalse(has_close_elements([1.0, 2.0], 0.0))
            self.assertFalse(has_close_elements([1.0, 1.0000000001], 0.0))
            self.assertFalse(has_close_elements([5.0, 5.0, 5.0], 0.0)) # Even if numbers are identical, diff is 0, 0 < 0 is False.

    def test_threshold_is_negative(self):
            # While not typically expected for a threshold, test negative threshold.
            # `diff < negative_threshold` is impossible since `diff` (absolute difference) is always >= 0.
            self.assertFalse(has_close_elements([1.0, 1.1], -0.1))
            self.assertFalse(has_close_elements([1.0, 1.0], -0.1))
            self.assertFalse(has_close_elements([-5.0, -4.5], -0.001))
