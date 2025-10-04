import unittest

class TestSortThird(unittest.TestCase):

    def test_empty_list(self):
        # Test case 1: An empty list should return an empty list.
        self.assertEqual(sort_third([]), [])

    def test_single_element_list(self):
        # Test case 2: A list with a single element (index 0 is divisible by 3)
        # The value at index 0 is collected, sorted (trivially), and put back.
        self.assertEqual(sort_third([7]), [7])

    def test_small_list_already_sorted_div_by_3(self):
        # Test case 3: A small list where only index 0 is divisible by 3,
        # and its value is already "sorted" (relative to itself).
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])

    def test_multiple_div_by_3_indices_needs_sorting(self):
        # Test case 4: The example from the problem description, where multiple
        # indices divisible by 3 have values that need sorting.
        # Original: [5, 6, 3, 4, 8, 9, 2]
        # Indices div by 3: 0, 3, 6
        # Values at these indices: [5, 4, 2]
        # Sorted values: [2, 4, 5]
        # Result: [2, 6, 3, 4, 8, 9, 5]
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

    def test_div_by_3_indices_sorted_descending(self):
        # Test case 5: Values at indices divisible by 3 are initially in descending order.
        # Original: [9, 1, 2, 6, 3, 4, 3, 5, 7, 0]
        # Indices div by 3: 0, 3, 6, 9
        # Values at these indices: [9, 6, 3, 0]
        # Sorted values: [0, 3, 6, 9]
        # Result: [0, 1, 2, 3, 3, 4, 6, 5, 7, 9]
        self.assertEqual(sort_third([9, 1, 2, 6, 3, 4, 3, 5, 7, 0]), [0, 1, 2, 3, 3, 4, 6, 5, 7, 9])

    def test_div_by_3_indices_already_ascending(self):
        # Test case 6: Values at indices divisible by 3 are already in ascending order.
        # The list should remain unchanged.
        # Original: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Indices div by 3: 0, 3, 6, 9
        # Values at these indices: [1, 4, 7, 10] (already sorted)
        self.assertEqual(sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_list_with_duplicates_at_div_by_3_indices(self):
        # Test case 7: List containing duplicate values, particularly at indices
        # divisible by three. Sorting should handle duplicates correctly.
        # Original: [7, 1, 2, 7, 3, 4, 1, 5, 6, 7]
        # Indices div by 3: 0, 3, 6, 9
        # Values at these indices: [7, 7, 1, 7]
        # Sorted values: [1, 7, 7, 7]
        # Result: [1, 1, 2, 7, 3, 4, 7, 5, 6, 7]
        self.assertEqual(sort_third([7, 1, 2, 7, 3, 4, 1, 5, 6, 7]), [1, 1, 2, 7, 3, 4, 7, 5, 6, 7])

    def test_list_with_negative_numbers_and_zero(self):
        # Test case 8: The list includes negative numbers and zero, checking
        # if sorting works correctly with these values.
        # Original: [-3, 10, -5, 0, 20, -1, -9, 30]
        # Indices div by 3: 0, 3, 6
        # Values at these indices: [-3, 0, -9]
        # Sorted values: [-9, -3, 0]
        # Result: [-9, 10, -5, -3, 20, -1, 0, 30]
        self.assertEqual(sort_third([-3, 10, -5, 0, 20, -1, -9, 30]), [-9, 10, -5, -3, 20, -1, 0, 30])

    def test_longer_list_mixed_order(self):
        # Test case 9: A longer list with a mix of ascending, descending, and random values
        # at divisible-by-3 indices and other positions.
        # Original: [10, 1, 2, 7, 3, 4, 5, 8, 6, 9, 0, 11]
        # Indices div by 3: 0, 3, 6, 9
        # Values at these indices: [10, 7, 5, 9]
        # Sorted values: [5, 7, 9, 10]
        # Result: [5, 1, 2, 7, 3, 4, 9, 8, 6, 10, 0, 11]
        self.assertEqual(sort_third([10, 1, 2, 7, 3, 4, 5, 8, 6, 9, 0, 11]), [5, 1, 2, 7, 3, 4, 9, 8, 6, 10, 0, 11])

    def test_list_with_interspersed_non_div_by_3_changes(self):
        # Test case 10: Checks that values at non-divisible-by-3 indices remain untouched,
        # even if they are identical to values being sorted into divisible-by-3 positions.
        # Original: [4, 1, 2, 1, 5, 6, 0]
        # Indices div by 3: 0, 3, 6
        # Values at these indices: [4, 1, 0]
        # Sorted values: [0, 1, 4]
        # Result: [0, 1, 2, 1, 5, 6, 4] (Note l[1] and l[3] both become 1, but for different reasons)
        self.assertEqual(sort_third([4, 1, 2, 1, 5, 6, 0]), [0, 1, 2, 1, 5, 6, 4])
    def test_empty_list(self):
            # Tests the behavior with an empty input list.
            # Covers the case where loops for collecting and placing values are not entered.
            self.assertEqual(self.solution.sort_third([]), [])

    def test_list_with_few_elements(self):
            # Tests lists with fewer than 3 elements, where only index 0 is divisible by 3.
            # This ensures the logic handles small lists correctly without errors.
            self.assertEqual(self.solution.sort_third([5]), [5])
            self.assertEqual(self.solution.sort_third([5, 2]), [5, 2])
            self.assertEqual(self.solution.sort_third([5, 2, 3]), [5, 2, 3])

    def test_already_sorted_third_indices(self):
            # Verifies correctness when elements at 3-divisible indices are already in sorted order.
            # The function should return the list unchanged in this scenario.
            input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.assertEqual(self.solution.sort_third(input_list), expected_output)

    def test_unsorted_third_indices(self):
            # Core test case where elements at 3-divisible indices need sorting.
            # Covers the sorting logic and re-placement of values.
            input_list = [7, 2, 1, 4, 5, 8, 3, 9, 6, 10]
            # Original values at indices 0, 3, 6, 9: 7, 4, 3, 10
            # Sorted values: 3, 4, 7, 10
            expected_output = [3, 2, 1, 4, 5, 8, 7, 9, 6, 10]
            self.assertEqual(self.solution.sort_third(input_list), expected_output)

    def test_mixed_values_negatives_zeros_duplicates(self):
            # Tests with a diverse set of values including negatives, zeros, and duplicates.
            # This checks the sorting algorithm's robustness with different number types.
            input_list = [0, 1, -1, 2, -2, 3, 0, -5, 5, 4, -10, 11, -15, 13, 14, 15]
            # Indices 0, 3, 6, 9, 12, 15
            # Values at these indices: 0, 2, 0, 4, -15, 15
            # Sorted values: -15, 0, 0, 2, 4, 15
            expected_output = [-15, 1, -1, 0, -2, 3, 0, -5, 5, 2, -10, 11, 4, 13, 14, 15]
            self.assertEqual(self.solution.sort_third(input_list), expected_output)

    def test_single_element_list(self):
            # A specific edge case for a list with just one element.
            self.assertEqual(self.solution.sort_third([42]), [42])
