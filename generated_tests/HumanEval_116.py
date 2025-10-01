import unittest

# Assume sort_array function exists and is imported or defined elsewhere.
# For clarity and to generate expected outputs, a helper key function is defined.
def _get_sort_key(n):
    """
    Helper function to determine the sorting key for an integer n.
    Sort by number of '1's in binary representation (ascending).
    If '1's count is equal, sort by decimal value (ascending).
    For negative numbers, bin(n) yields '-0b...', so count '1's from the absolute part.
    """
    return (bin(n).count('1'), n)

class TestSortArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sort_array([]), [])

    def test_single_element_array(self):
        self.assertEqual(sort_array([42]), [42])

    def test_basic_positive_integers_with_ties(self):
        # Input based on problem description's first example, but with correct expected output
        # 1 (0b1): 1 one, 1 dec
        # 5 (0b101): 2 ones, 5 dec
        # 2 (0b10): 1 one, 2 dec
        # 3 (0b11): 2 ones, 3 dec
        # 4 (0b100): 1 one, 4 dec
        # Sorted order: (1 one, 1), (1 one, 2), (1 one, 4), (2 ones, 3), (2 ones, 5)
        input_array = [1, 5, 2, 3, 4]
        expected_output = sorted(input_array, key=_get_sort_key)
        self.assertEqual(sort_array(input_array), expected_output) # Expected: [1, 2, 4, 3, 5]

    def test_numbers_with_zero_and_powers_of_two(self):
        # 0 (0b0): 0 ones, 0 dec
        # 1 (0b1): 1 one, 1 dec
        # 2 (0b10): 1 one, 2 dec
        # 4 (0b100): 1 one, 4 dec
        # 8 (0b1000): 1 one, 8 dec
        # Sorted order: (0 ones, 0), (1 one, 1), (1 one, 2), (1 one, 4), (1 one, 8)
        input_array = [8, 0, 1, 2, 4]
        expected_output = sorted(input_array, key=_get_sort_key)
        self.assertEqual(sort_array(input_array), expected_output) # Expected: [0, 1, 2, 4, 8]

    def test_larger_positive_integers_more_ones(self):
        # 7 (0b111): 3 ones, 7 dec
        # 15 (0b1111): 4 ones, 15 dec
        # 6 (0b110): 2 ones, 6 dec
        # 13 (0b1101): 3 ones, 13 dec
        # Sorted order: (2 ones, 6), (3 ones, 7), (3 ones, 13), (4 ones, 15)
        input_array = [7, 15, 6, 13]
        expected_output = sorted(input_array, key=_get_sort_key)
        self.assertEqual(sort_array(input_array), expected_output) # Expected: [6, 7, 13, 15]

    def test_array_with_negative_integers(self):
        # Input based on problem description's second example, but with correct expected output
        # -2 ('-0b10'): 1 one, -2 dec
        # -3 ('-0b11'): 2 ones, -3 dec
        # -4 ('-0b100'): 1 one, -4 dec
        # -5 ('-0b101'): 2 ones, -5 dec
        # -6 ('-0b110'): 2 ones, -6 dec
        # Sorted order: (1 one, -4), (1 one, -2), (2 ones, -6), (2 ones, -5), (2 ones, -3)
        input_array = [-2, -3, -4, -5, -6]
        expected_output = sorted(input_array, key=_get_sort_key)
        self.assertEqual(sort_array(input_array), expected_output) # Expected: [-4, -2, -6, -5, -3]

    def test_mixed_positive_zero_and_negative_integers(self):
        # 0 (0b0): 0 ones, 0 dec
        # -1 ('-0b1'): 1 one, -1 dec
        # 1 (0b1): 1 one, 1 dec
        # -2 ('-0b10'): 1 one, -2 dec
        # 2 (0b10): 1 one, 2 dec
        # Sorted order: (0 ones, 0), (1 one, -2), (1 one, -1), (1 one, 1), (1 one, 2)
        input_array = [0, -1, 1, -2, 2]
        expected_output = sorted(input_array, key=_get_sort_key)
        self.assertEqual(sort_array(input_array), expected_output) # Expected: [0, -2, -1, 1, 2]

    def test_array_with_duplicate_values(self):
        # 1 (0b1): 1 one, 1 dec
        # 2 (0b10): 1 one, 2 dec
        # 3 (0b11): 2 ones, 3 dec
        # Sorted order: (1 one, 1), (1 one, 1), (1 one, 2), (1 one, 2), (2 ones, 3)
        input_array = [1, 2, 1, 3, 2]
        expected_output = sorted(input_array, key=_get_sort_key)
        self.assertEqual(sort_array(input_array), expected_output) # Expected: [1, 1, 2, 2, 3]

    def test_array_already_sorted_by_rule(self):
        # This input is already sorted according to the rules (and _get_sort_key)
        # 0 (0b0): 0 ones, 0 dec
        # 1 (0b1): 1 one, 1 dec
        # 2 (0b10): 1 one, 2 dec
        # 4 (0b100): 1 one, 4 dec
        # 3 (0b11): 2 ones, 3 dec
        # 5 (0b101): 2 ones, 5 dec
        input_array = [0, 1, 2, 4, 3, 5]
        expected_output = sorted(input_array, key=_get_sort_key)
        self.assertEqual(sort_array(input_array), expected_output) # Expected: [0, 1, 2, 4, 3, 5]

    def test_array_in_reverse_decimal_order(self):
        # 10 (0b1010): 2 ones, 10 dec
        # 9 (0b1001): 2 ones, 9 dec
        # 8 (0b1000): 1 one, 8 dec
        # 7 (0b111): 3 ones, 7 dec
        # 6 (0b110): 2 ones, 6 dec
        # 5 (0b101): 2 ones, 5 dec
        # Sorted order: (1 one, 8), (2 ones, 5), (2 ones, 6), (2 ones, 9), (2 ones, 10), (3 ones, 7)
        input_array = [10, 9, 8, 7, 6, 5]
        expected_output = sorted(input_array, key=_get_sort_key)
        self.assertEqual(sort_array(input_array), expected_output) # Expected: [8, 5, 6, 9, 10, 7]

# If you want to run these tests directly from this file
if __name__ == '__main__':
    # This is a placeholder for the actual function.
    # In a real scenario, `sort_array` would be imported from the solution file.
    # For testing purposes, we define a dummy that uses the helper key.
    # The actual implementation of `sort_array` would be similar to:
    # def sort_array(arr):
    #     return sorted(arr, key=lambda n: (bin(n).count('1'), n))
    
    # Using the helper key to simulate the expected behavior for testing
    # def sort_array(arr):
    #     return sorted(arr, key=_get_sort_key)
        
    unittest.main(argv=['first-arg-is-ignored'], exit=False)