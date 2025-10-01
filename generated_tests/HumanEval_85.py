import unittest

# Assume the 'add' function is defined elsewhere, e.g.:
# def add(lst):
#     total = 0
#     for i in range(len(lst)):
#         # Check if index is odd AND element at that index is even
#         if i % 2 != 0 and lst[i] % 2 == 0:
#             total += lst[i]
#     return total

class TestAddEvenElementsAtOddIndices(unittest.TestCase):

    def test_example_case(self):
        # Test case provided in the problem description
        self.assertEqual(add([4, 2, 6, 7]), 2)

    def test_no_even_elements_at_odd_indices(self):
        # All elements at odd indices are odd, so no sum
        self.assertEqual(add([1, 3, 5, 7, 9]), 0)

    def test_all_elements_even_some_at_odd_indices(self):
        # All numbers are even, but only those at odd indices contribute
        # Indices: 0  1  2  3   4
        # Elements: [2, 4, 6, 8, 10]
        # Odd indices: 1 (value 4), 3 (value 8)
        self.assertEqual(add([2, 4, 6, 8, 10]), 4 + 8) # Expected: 12

    def test_two_elements_second_is_even(self):
        # Smallest list with a single match
        # Indices: 0  1
        # Elements: [1, 8]
        # Odd index: 1 (value 8)
        self.assertEqual(add([1, 8]), 8)

    def test_two_elements_second_is_odd(self):
        # Smallest list with no matches
        # Indices: 0  1
        # Elements: [1, 7]
        # Odd index: 1 (value 7, which is odd)
        self.assertEqual(add([1, 7]), 0)

    def test_longer_list_multiple_matches(self):
        # A longer list with several even numbers at odd indices
        # Indices:   0   1   2   3   4   5   6
        # Elements: [10, 20, 30, 40, 50, 60, 70]
        # Odd indices with even elements: 20 (idx 1), 40 (idx 3), 60 (idx 5)
        self.assertEqual(add([10, 20, 30, 40, 50, 60, 70]), 20 + 40 + 60) # Expected: 120

    def test_single_element_list(self):
        # A list with only one element has no odd indices
        # Indices: 0
        # Elements: [5]
        self.assertEqual(add([5]), 0)

    def test_list_with_negative_even_numbers(self):
        # Test with negative even numbers at odd indices
        # Indices:   0   1   2   3   4   5
        # Elements: [1, -2, 3, -4, 5, -6]
        # Odd indices with even elements: -2 (idx 1), -4 (idx 3), -6 (idx 5)
        self.assertEqual(add([1, -2, 3, -4, 5, -6]), -2 + -4 + -6) # Expected: -12

    def test_list_with_zeros_at_odd_indices(self):
        # Zeros are even, test if they are correctly added
        # Indices:   0  1  2  3  4
        # Elements: [0, 0, 0, 0, 0]
        # Odd indices with even elements: 0 (idx 1), 0 (idx 3)
        self.assertEqual(add([0, 0, 0, 0, 0]), 0 + 0) # Expected: 0

    def test_complex_mixed_list(self):
        # A more complex mix of even/odd, positive/negative numbers at various indices
        # Indices:   0   1   2   3   4   5   6   7   8   9
        # Elements: [1, 20, -3, 40, 5, -60, 7, 80, -9, 100]
        # Odd indices with even elements:
        # idx 1: 20 (even)
        # idx 3: 40 (even)
        # idx 5: -60 (even)
        # idx 7: 80 (even)
        # idx 9: 100 (even)
        self.assertEqual(add([1, 20, -3, 40, 5, -60, 7, 80, -9, 100]), 20 + 40 - 60 + 80 + 100) # Expected: 180