import unittest

class TestMinSubArraySum(unittest.TestCase):

    def test_example_one(self):
        # Example from problem description: minimum is a single positive element
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)

    def test_example_two(self):
        # Example from problem description: all negative, minimum is sum of all
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

    def test_single_positive_element(self):
        # Array with just one positive element
        self.assertEqual(minSubArraySum([7]), 7)

    def test_single_negative_element(self):
        # Array with just one negative element
        self.assertEqual(minSubArraySum([-10]), -10)

    def test_all_positive_minimum_is_smallest_element(self):
        # All positive numbers, min sum is the smallest single element
        self.assertEqual(minSubArraySum([5, 8, 2, 10, 1]), 1)

    def test_all_negative_minimum_is_sum_of_all_elements(self):
        # All negative numbers, min sum is the sum of all elements
        self.assertEqual(minSubArraySum([-1, -5, -3, -2]), -11)

    def test_mixed_min_is_single_negative_element(self):
        # Mixed positive and negative, min sum is a single negative element
        self.assertEqual(minSubArraySum([10, -5, 20, 1]), -5)

    def test_mixed_min_is_sum_of_multiple_negative_elements(self):
        # Mixed positive and negative, min sum is a contiguous block of negatives
        self.assertEqual(minSubArraySum([3, -1, -2, -4, 5]), -7) # sub-array [-1, -2, -4]

    def test_mixed_min_in_middle_with_reset(self):
        # Complex mix, min sum is an intermediate negative sum that 'resets'
        self.assertEqual(minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), -5) # sub-array [-5]

    def test_array_with_zeros_and_negatives(self):
        # Array containing zeros and negative numbers
        self.assertEqual(minSubArraySum([0, -1, 0, 2, -3, 0]), -3) # sub-array [-3]