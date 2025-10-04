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
    def test_minSubArraySum_singleElement(self):
            # This test covers the scenario where the input array has only one element.
            # In this case, the `for` loop (line 17) is not entered, but it's a valid path.
            # This ensures the initialization of `min_so_far` and `current_min` is correct.
            self.assertEqual(solution.minSubArraySum([5]), 5)
            self.assertEqual(solution.minSubArraySum([-10]), -10)
            self.assertEqual(solution.minSubArraySum([0]), 0)

    def test_minSubArraySum_allPositiveMultipleElements(self):
            # This test ensures the `for` loop (line 17) is executed.
            # It covers arrays with multiple positive numbers, where the minimum sub-array
            # sum is the smallest individual element.
            self.assertEqual(solution.minSubArraySum([1, 2, 3, 4, 5]), 1)
            self.assertEqual(solution.minSubArraySum([10, 5, 15]), 5)

    def test_minSubArraySum_allNegativeMultipleElements(self):
            # This test ensures the `for` loop (line 17) is executed.
            # It covers arrays with multiple negative numbers, where the minimum sub-array
            # sum is the sum of all elements.
            self.assertEqual(solution.minSubArraySum([-1, -2, -3, -4]), -10)
            self.assertEqual(solution.minSubArraySum([-5, -1, -10]), -16)

    def test_minSubArraySum_mixedElementsSimple(self):
            # This test ensures the `for` loop (line 17) is executed.
            # It covers mixed positive and negative numbers where the minimum sub-array
            # sum is a single negative element.
            self.assertEqual(solution.minSubArraySum([2, -5, 3]), -5)
            self.assertEqual(solution.minSubArraySum([1, 2, -10, 3, 4]), -10)

    def test_minSubArraySum_mixedElementsSubArraySum(self):
            # This test ensures the `for` loop (line 17) is executed and complex logic
            # for finding a minimum sum from a sub-array (not just a single element).
            self.assertEqual(solution.minSubArraySum([2, -3, 4, -1, -2, 1, -5]), -5) # The sequence [-1, -2, 1, -5] could be a trap for simple logic. Result is -5.
            self.assertEqual(solution.minSubArraySum([3, -4, 2, -1, 5]), -4)
            self.assertEqual(solution.minSubArraySum([10, -20, 5, -1, -2, 8]), -20)
            self.assertEqual(solution.minSubArraySum([1, -2, 3, -4, 5]), -4)

    def test_minSubArraySum_withZeroes(self):
            # This test covers scenarios involving zero, ensuring they are handled correctly
            # within the loop (line 17).
            self.assertEqual(solution.minSubArraySum([1, 0, -2, 0, 3]), -2)
            self.assertEqual(solution.minSubArraySum([-1, 0, -5]), -6)
            self.assertEqual(solution.minSubArraySum([0, 0, 0, 0]), 0)
