import unittest

class TestSortArray(unittest.TestCase):

    # Test case 1: Empty array
    # Expect an empty array back.
    def test_empty_array(self):
        arr = []
        expected = []
        self.assertEqual(sort_array(arr), expected)

    # Test case 2: Single element array
    # Expect the same single element array back.
    def test_single_element_array(self):
        arr = [5]
        expected = [5]
        self.assertEqual(sort_array(arr), expected)

    # Test case 3: Sum of first and last elements is ODD - Ascending sort
    # Example from problem: [2, 4, 3, 0, 1, 5]
    # First = 2, Last = 5. Sum = 2 + 5 = 7 (ODD) => Ascending sort
    def test_odd_sum_ascending_example_1(self):
        arr = [2, 4, 3, 0, 1, 5]
        expected = [0, 1, 2, 3, 4, 5]
        self.assertEqual(sort_array(arr), expected)

    # Test case 4: Sum of first and last elements is ODD - Ascending sort
    # Different numbers, first+last results in an odd sum.
    # [1, 9, 3, 7, 5, 0] => First = 1, Last = 0. Sum = 1 + 0 = 1 (ODD) => Ascending sort
    def test_odd_sum_ascending_example_2(self):
        arr = [1, 9, 3, 7, 5, 0]
        expected = [0, 1, 3, 5, 7, 9]
        self.assertEqual(sort_array(arr), expected)

    # Test case 5: Sum of first and last elements is ODD - Ascending sort
    # Array with larger values.
    # [100, 2, 8, 50, 1] => First = 100, Last = 1. Sum = 100 + 1 = 101 (ODD) => Ascending sort
    def test_odd_sum_ascending_large_numbers(self):
        arr = [100, 2, 8, 50, 1]
        expected = [1, 2, 8, 50, 100]
        self.assertEqual(sort_array(arr), expected)

    # Test case 6: Sum of first and last elements is EVEN - Descending sort
    # Example from problem: [2, 4, 3, 0, 1, 5, 6]
    # First = 2, Last = 6. Sum = 2 + 6 = 8 (EVEN) => Descending sort
    def test_even_sum_descending_example_1(self):
        arr = [2, 4, 3, 0, 1, 5, 6]
        expected = [6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(sort_array(arr), expected)

    # Test case 7: Sum of first and last elements is EVEN - Descending sort
    # Different numbers, first+last results in an even sum.
    # [10, 20, 5, 1, 0] => First = 10, Last = 0. Sum = 10 + 0 = 10 (EVEN) => Descending sort
    def test_even_sum_descending_example_2(self):
        arr = [10, 20, 5, 1, 0]
        expected = [20, 10, 5, 1, 0]
        self.assertEqual(sort_array(arr), expected)

    # Test case 8: Sum of first and last elements is EVEN - Descending sort
    # A simple two-element array.
    # [7, 1] => First = 7, Last = 1. Sum = 7 + 1 = 8 (EVEN) => Descending sort
    def test_even_sum_descending_two_elements(self):
        arr = [7, 1]
        expected = [7, 1] # Already sorted descending
        self.assertEqual(sort_array(arr), expected)

    # Test case 9: Sum of first and last elements is EVEN - Descending sort
    # Array with all identical elements.
    # [3, 3, 3, 3] => First = 3, Last = 3. Sum = 3 + 3 = 6 (EVEN) => Descending sort
    def test_even_sum_descending_all_same_elements(self):
        arr = [3, 3, 3, 3]
        expected = [3, 3, 3, 3] # Descending or ascending result is the same
        self.assertEqual(sort_array(arr), expected)

    # Test case 10: Sum of first and last elements is EVEN - Descending sort
    # Larger array with mixed numbers, unsorted.
    # [15, 2, 8, 10, 3, 7] => First = 15, Last = 7. Sum = 15 + 7 = 22 (EVEN) => Descending sort
    def test_even_sum_descending_large_array_mixed(self):
        arr = [15, 2, 8, 10, 3, 7]
        expected = [15, 10, 8, 7, 3, 2]
        self.assertEqual(sort_array(arr), expected)

    def test_sort_array_empty(self):
            # Covers the 'if not arr:' branch (line 5)
            self.assertEqual(self.solution.sort_array([]), [])

    def test_sort_array_odd_sum_first_last(self):
            # Covers the 'if elements_sum % 2 != 0:' branch (line 22)
            # First + Last = 1 + 4 = 5 (odd) -> Ascending sort
            input_array = [4, 1, 3, 2]
            expected_output = [1, 2, 3, 4]
            self.assertEqual(self.solution.sort_array(input_array), expected_output)

    def test_sort_array_even_sum_first_last(self):
            # Covers the 'else:' branch (line 25)
            # First + Last = 5 + 1 = 6 (even) -> Descending sort
            input_array = [5, 2, 8, 1, 3]
            expected_output = [8, 5, 3, 2, 1]
            self.assertEqual(self.solution.sort_array(input_array), expected_output)

    def test_sort_array_single_element(self):
            # Edge case: single element array (sum will always be even)
            # First + Last = 7 + 7 = 14 (even) -> Descending sort
            input_array = [7]
            expected_output = [7]
            self.assertEqual(self.solution.sort_array(input_array), expected_output)
# To run the tests, uncomment the following block
# if __name__ == '__main__':
#     # Assuming sort_array function is defined elsewhere for testing purposes
#     # def sort_array(arr):
#     #     if not arr:
#     #         return []
#     #     if len(arr) == 1:
#     #         return list(arr) # Return a copy as per problem statement
#
#     #     first = arr[0]
#     #     last = arr[-1]
#     #     sum_first_last = first + last
#
#     #     if sum_first_last % 2 != 0: # Odd sum, sort ascending
#     #         return sorted(arr)
#     #     else: # Even sum, sort descending
#     #         return sorted(arr, reverse=True)
#
#     unittest.main(argv=['first-arg-is-ignored'], exit=False)