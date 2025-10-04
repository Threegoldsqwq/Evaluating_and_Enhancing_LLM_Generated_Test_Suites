import unittest

class TestPluckNode(unittest.TestCase):
    def placeholder():
        pass

    def test_example_1(self):
            # Basic case, smallest even in the middle.
            self.assertEqual(pluck([4, 2, 3]), [2, 1])
    def test_example_2(self):
            # Basic case, smallest even in the middle, mixed with odds.
            self.assertEqual(pluck([1, 2, 3]), [2, 1])
    def test_example_3(self):
            # Empty array.
            self.assertEqual(pluck([]), [])
    def test_example_4(self):
            # Smallest even is 0, multiple occurrences, choose first.
            self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])
    def test_no_even_numbers(self):
            # Array with no even numbers.
            self.assertEqual(pluck([1, 3, 5, 7, 9]), [])
    def test_only_one_even_number(self):
            # Array with only one even number, which is also the smallest.
            self.assertEqual(pluck([1, 3, 8, 5, 7]), [8, 2])
    def test_smallest_even_at_beginning(self):
            # Smallest even number is at the beginning of the array.
            self.assertEqual(pluck([2, 10, 4, 6, 8]), [2, 0])
    def test_smallest_even_at_end(self):
            # Smallest even number is at the end of the array.
            self.assertEqual(pluck([10, 8, 6, 4, 2]), [2, 4])
    def test_multiple_occurrences_of_smallest_even(self):
            # Multiple occurrences of the same smallest even number, return the one with smallest index.
            self.assertEqual(pluck([10, 4, 2, 6, 2, 8]), [2, 2])
    def test_large_array_with_various_values(self):
            # A larger array with a mix of values, including 0.
            self.assertEqual(pluck([15, 7, 22, 0, 19, 4, 11, 0, 30, 2]), [0, 3])

    def test_empty_list(self):
            self.assertEqual(self.solution.pluck([]), [])

    def test_no_even_numbers(self):
            self.assertEqual(self.solution.pluck([1, 3, 5, 7, 9]), [])

    def test_single_even_number(self):
            self.assertEqual(self.solution.pluck([1, 5, 8, 3, 7]), [8, 2])

    def test_multiple_even_numbers_smallest_unique(self):
            self.assertEqual(self.solution.pluck([10, 4, 20, 2, 30]), [2, 3])

    def test_multiple_even_numbers_smallest_first_occurrence(self):
            # Smallest even value 4 appears at index 1 and index 4. Should return the one at index 1.
            self.assertEqual(self.solution.pluck([10, 4, 20, 6, 4, 30]), [4, 1])

    def test_smallest_even_is_zero(self):
            self.assertEqual(self.solution.pluck([5, 0, 3, 2, 1]), [0, 1])

    def test_smallest_even_at_beginning(self):
            self.assertEqual(self.solution.pluck([2, 8, 4, 10]), [2, 0])

    def test_smallest_even_at_end(self):
            self.assertEqual(self.solution.pluck([10, 8, 4, 2]), [2, 3])

    def test_mixed_odd_and_even(self):
            self.assertEqual(self.solution.pluck([1, 9, 7, 6, 3, 8]), [6, 3])

    def test_all_numbers_are_even(self):
            self.assertEqual(self.solution.pluck([8, 6, 2, 4]), [2, 2])
# Note: The 'pluck_node' function is assumed to exist as per the problem statement.
# For these tests to run, you would typically define it like this:
#
# def pluck_node(nodes):
#     if not nodes:
#         return []
#
#     smallest_even_value = float('inf')
#     smallest_even_index = -1
#
#     for i, node_value in enumerate(nodes):
#         if node_value % 2 == 0:  # Check if it's an even number
#             if node_value < smallest_even_value:
#                 smallest_even_value = node_value
#                 smallest_even_index = i
#             elif node_value == smallest_even_value:
#                 # If values are equal, keep the one with the smaller index
#                 # Since we iterate from left to right, the first one found
#                 # for a given smallest_even_value will naturally have the smallest index.
#                 # So, no explicit action needed here for 'smallest_even_index'.
#                 pass
#
#     if smallest_even_index == -1:
#         return []
#     else:
#         return [smallest_even_value, smallest_even_index]