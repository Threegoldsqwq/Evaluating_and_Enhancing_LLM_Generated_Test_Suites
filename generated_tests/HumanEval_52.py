import unittest

class TestBelowThreshold(unittest.TestCase):

    def test_all_numbers_below_positive_threshold(self):
        # All numbers are strictly below a large positive threshold
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))

    def test_one_number_equal_to_threshold(self):
        # One number is exactly equal to the threshold, should be False
        self.assertFalse(below_threshold([1, 2, 5, 4], 5))

    def test_one_number_above_threshold(self):
        # One number is above the threshold, should be False
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

    def test_all_numbers_below_close_positive_threshold(self):
        # All numbers are strictly below a positive threshold, with the max close to it
        self.assertTrue(below_threshold([1, 2, 3, 4], 5))

    def test_empty_list(self):
        # An empty list should always return True (vacuously true)
        self.assertTrue(below_threshold([], 10))

    def test_list_with_one_element_below(self):
        # List with a single element, which is below the threshold
        self.assertTrue(below_threshold([7], 8))

    def test_list_with_one_element_equal(self):
        # List with a single element, which is equal to the threshold
        self.assertFalse(below_threshold([7], 7))

    def test_all_numbers_below_negative_threshold(self):
        # All numbers are strictly below a negative threshold
        self.assertTrue(below_threshold([-10, -5, -20], -1))

    def test_mixed_numbers_below_positive_threshold(self):
        # Mixed positive and negative numbers, all below a positive threshold
        self.assertTrue(below_threshold([-5, 0, 3, 7], 8))

    def test_mixed_numbers_some_above_negative_threshold(self):
        # Mixed numbers, some above or equal to a negative threshold
        self.assertFalse(below_threshold([-10, -5, 0, 3], -5))
    def test_single_element_below_threshold(self):
            self.assertTrue(below_threshold([5], 6))

    def test_single_element_at_threshold(self):
            self.assertFalse(below_threshold([6], 6))

    def test_single_element_above_threshold(self):
            self.assertFalse(below_threshold([7], 6))

    def test_middle_element_above_threshold(self):
            self.assertFalse(below_threshold([1, 2, 10, 4, 5], 5))

    def test_all_elements_just_below(self):
            self.assertTrue(below_threshold([9, 9, 9], 10))

    def test_all_elements_at_threshold(self):
            self.assertFalse(below_threshold([10, 10, 10], 10))

    def test_negative_numbers_all_below(self):
            self.assertTrue(below_threshold([-3, -2, -1], 0))

    def test_negative_numbers_at_threshold(self):
            self.assertFalse(below_threshold([-5, -2, -1], -2))

    def test_negative_numbers_above_threshold(self):
            self.assertFalse(below_threshold([-5, -1, 0], -2))

    def test_positive_numbers_negative_threshold(self):
            # All numbers are above the negative threshold, so it should be False
            self.assertFalse(below_threshold([1, 5, 10], -5))

    def test_zero_in_list_threshold_zero(self):
            self.assertFalse(below_threshold([-1, 0, 1], 0))
