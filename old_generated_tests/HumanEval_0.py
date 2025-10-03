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