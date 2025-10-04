import unittest

class TestStrangeSortList(unittest.TestCase):

    def test_empty_list(self):
        # Test with an empty list
        self.assertEqual(strange_sort_list([]), [])

    def test_single_element_list(self):
        # Test with a single-element list
        self.assertEqual(strange_sort_list([7]), [7])

    def test_even_elements_simple_increasing(self):
        # Test with an even number of elements, already sorted
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_odd_elements_simple_increasing(self):
        # Test with an odd number of elements, already sorted
        self.assertEqual(strange_sort_list([1, 2, 3, 4, 5]), [1, 5, 2, 4, 3])

    def test_all_same_elements(self):
        # Test with all elements being the same
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_negative_numbers(self):
        # Test with negative numbers, mixed order initially
        # Sorted: [-4, -3, -2, -1] -> Output: [-4, -1, -3, -2]
        self.assertEqual(strange_sort_list([-1, -4, -2, -3]), [-4, -1, -3, -2])

    def test_mixed_numbers_odd_length(self):
        # Test with a mix of positive, negative, and zero, odd length
        # Sorted: [-2, -1, 0, 1, 2] -> Output: [-2, 2, -1, 1, 0]
        self.assertEqual(strange_sort_list([1, -2, 2, 0, -1]), [-2, 2, -1, 1, 0])

    def test_duplicates_even_length(self):
        # Test with duplicate values and even length
        # Sorted: [1, 2, 2, 3] -> Output: [1, 3, 2, 2]
        self.assertEqual(strange_sort_list([1, 3, 2, 2]), [1, 3, 2, 2])

    def test_duplicates_odd_length(self):
        # Test with duplicate values and odd length
        # Sorted: [10, 10, 20, 20, 30] -> Output: [10, 30, 10, 20, 20]
        self.assertEqual(strange_sort_list([20, 10, 30, 10, 20]), [10, 30, 10, 20, 20])

    def test_larger_even_list(self):
        # Test with a larger list of even length, mixed order initially
        # Sorted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> Output: [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        self.assertEqual(strange_sort_list([10, 1, 9, 2, 8, 3, 7, 4, 6, 5]), [1, 10, 2, 9, 3, 8, 4, 7, 5, 6])

    def test_single_element_list(self):
            """Test with lists containing a single element."""
            self.assertEqual(strange_sort_list([42]), [42])
            self.assertEqual(strange_sort_list([0]), [0])
            self.assertEqual(strange_sort_list([-5]), [-5])

    def test_odd_length_lists(self):
            """Test with odd-length lists (more than one element)."""
            self.assertEqual(strange_sort_list([1, 2, 3]), [1, 3, 2])
            self.assertEqual(strange_sort_list([10, 5, 20]), [5, 20, 10])
            self.assertEqual(strange_sort_list([-3, 0, 3]), [-3, 3, 0])
            self.assertEqual(strange_sort_list([100, 1, 50, 5, 10]), [1, 100, 5, 50, 10])

    def test_lists_with_negative_and_zero(self):
            """Test with lists containing negative numbers and zero."""
            # Even length, all negative
            self.assertEqual(strange_sort_list([-1, -2, -3, -4]), [-4, -1, -3, -2])
            # Odd length, all negative
            self.assertEqual(strange_sort_list([-1, -2, -3]), [-3, -1, -2])
            # Mixed positive, negative, zero, odd length
            self.assertEqual(strange_sort_list([-5, 0, 5, -1, 1]), [-5, 5, -1, 1, 0])
            # Mixed positive, negative, zero, even length
            self.assertEqual(strange_sort_list([-2, 0, 2, -1, 1, -3]), [-3, 2, -2, 1, -1, 0])

    def test_lists_with_duplicates_odd_length(self):
            """Test with odd-length lists containing duplicate elements."""
            self.assertEqual(strange_sort_list([7, 7, 7]), [7, 7, 7])
            self.assertEqual(strange_sort_list([1, 1, 2, 2, 2]), [1, 2, 1, 2, 2])
            self.assertEqual(strange_sort_list([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_longer_lists(self):
            """Test with longer lists to ensure scalability and correct logic over many iterations."""
            long_list_even = list(range(1, 11))  # [1, 2, ..., 10]
            expected_even = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
            self.assertEqual(strange_sort_list(long_list_even), expected_even)

            long_list_odd = list(range(1, 10))  # [1, 2, ..., 9]
            expected_odd = [1, 9, 2, 8, 3, 7, 4, 6, 5]
            self.assertEqual(strange_sort_list(long_list_odd), expected_odd)
# To run these tests, you would typically have the strange_sort_list function defined.
# For example:
# def strange_sort_list(integers: list) -> list:
#     if not integers:
#         return []
#
#     sorted_list = sorted(integers)
#     result = []
#     left = 0
#     right = len(sorted_list) - 1
#     is_min_turn = True
#
#     while left <= right:
#         if is_min_turn:
#             result.append(sorted_list[left])
#             left += 1
#         else:
#             result.append(sorted_list[right])
#             right -= 1
#         is_min_turn = not is_min_turn
#
#     return result

if __name__ == '__main__':
    # Placeholder for the function as per the prompt's instruction:
    # "assume the function exist."
    # A basic implementation is included here for the tests to be runnable,
    # but it's not part of the requested output.
    # def strange_sort_list(integers: list) -> list:
    #     if not integers:
    #         return []

    #     sorted_list = sorted(integers)
    #     result = []
    #     left = 0
    #     right = len(sorted_list) - 1
    #     is_min_turn = True

    #     while left <= right:
    #         if is_min_turn:
    #             result.append(sorted_list[left])
    #             left += 1
    #         else:
    #             result.append(sorted_list[right])
    #             right -= 1
    #         is_min_turn = not is_min_turn

    #     return result

    unittest.main(argv=['first-arg-is-ignored'], exit=False)