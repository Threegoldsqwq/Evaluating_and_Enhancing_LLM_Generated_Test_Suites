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