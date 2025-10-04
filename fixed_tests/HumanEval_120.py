import unittest

# Assume the function find_max_k_numbers(arr, k) exists.
# The problem statement implies a function signature like:
# def find_max_k_numbers(arr: list[int], k: int) -> list[int]:
#     # ... implementation ...


class TestFindMaxKNumbers(unittest.TestCase):

    def test_example_1(self):
        """Test with example 1: all elements are selected."""
        arr = [-3, -4, 5]
        k = 3
        expected_output = [-4, -3, 5]
        self.assertEqual(find_max_k_numbers(arr, k), expected_output)

    def test_example_2(self):
        """Test with example 2: duplicates and positive numbers."""
        arr = [4, -4, 4]
        k = 2
        expected_output = [4, 4]
        self.assertEqual(find_max_k_numbers(arr, k), expected_output)

    def test_example_3(self):
        """Test with example 3: k=1, single largest element."""
        arr = [-3, 2, 1, 2, -1, -2, 1]
        k = 1
        expected_output = [2]
        self.assertEqual(find_max_k_numbers(arr, k), expected_output)

    def test_k_is_zero(self):
        """Test case where k is 0, expecting an empty list."""
        arr = [1, 2, 3, 4, 5]
        k = 0
        expected_output = []
        self.assertEqual(find_max_k_numbers(arr, k), expected_output)

    def test_all_negative_numbers(self):
        """Test with an array of all negative numbers, selecting a subset."""
        arr = [-10, -5, -8, -1]
        k = 2
        expected_output = [-5, -1]  # The two largest are -5 and -1, sorted.
        self.assertEqual(find_max_k_numbers(arr, k), expected_output)

    def test_mixed_numbers_with_zero(self):
        """Test with a mix of positive, negative, and zero, selecting multiple."""
        arr = [-1, -2, 0, 1, 2, 3]
        k = 4
        expected_output = [0, 1, 2, 3]  # The four largest are 0, 1, 2, 3.
        self.assertEqual(find_max_k_numbers(arr, k), expected_output)

    def test_single_element_array(self):
        """Test with an array containing only one element."""
        arr = [7]
        k = 1
        expected_output = [7]
        self.assertEqual(find_max_k_numbers(arr, k), expected_output)

    def test_larger_array_mixed_values(self):
        """Test with a larger array and k selecting elements from the middle."""
        arr = [10, -5, 20, 0, 30, -15, 25, 5]
        k = 3
        expected_output = [20, 25, 30]  # The three largest are 20, 25, 30.
        self.assertEqual(find_max_k_numbers(arr, k), expected_output)

    def test_array_all_same_numbers(self):
        """Test with an array where all elements are identical."""
        arr = [5, 5, 5, 5, 5]
        k = 3
        expected_output = [5, 5, 5]
        self.assertEqual(find_max_k_numbers(arr, k), expected_output)

    def test_k_equals_len_with_duplicates_and_negatives(self):
        """Test case where k equals the length of the array, with duplicates and negatives."""
        arr = [-1, 0, 1, 0, -1]
        k = 5
        expected_output = [-1, -1, 0, 0, 1]  # All elements, sorted.
        self.assertEqual(find_max_k_numbers(arr, k), expected_output)