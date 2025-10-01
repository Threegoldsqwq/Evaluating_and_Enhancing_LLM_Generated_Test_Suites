import unittest

# Assume the 'rolling_max' function is defined elsewhere, for example:
# def rolling_max(numbers):
#     if not numbers:
#         return []
#     
#     result = []
#     current_max = float('-inf') # Initialize with a very small number
#     for num in numbers:
#         if num > current_max:
#             current_max = num
#         result.append(current_max)
#     return result

class TestRollingMax(unittest.TestCase):

    def test_example_case(self):
        """Test the example given in the problem description."""
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(rolling_max([]), [])

    def test_single_element_list(self):
        """Test with a list containing a single element."""
        self.assertEqual(rolling_max([5]), [5])

    def test_monotonically_increasing(self):
        """Test with a list where numbers are strictly increasing."""
        self.assertEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_monotonically_decreasing(self):
        """Test with a list where numbers are strictly decreasing."""
        self.assertEqual(rolling_max([5, 4, 3, 2, 1]), [5, 5, 5, 5, 5])

    def test_all_elements_same(self):
        """Test with a list where all elements are identical."""
        self.assertEqual(rolling_max([7, 7, 7, 7]), [7, 7, 7, 7])

    def test_with_negative_numbers(self):
        """Test with a list containing negative numbers."""
        self.assertEqual(rolling_max([-1, -5, -2, 0, -3, -1]), [-1, -1, -1, 0, 0, 0])

    def test_with_zeros(self):
        """Test with a list including zero and mixed positive/negative."""
        self.assertEqual(rolling_max([0, -1, 5, 0, 10, -2]), [0, 0, 5, 5, 10, 10])

    def test_large_numbers_and_fluctuations(self):
        """Test with a longer list with significant fluctuations."""
        self.assertEqual(rolling_max([100, 20, 300, 150, 400, 50, 600, 550]), [100, 100, 300, 300, 400, 400, 600, 600])

    def test_initial_max_then_decreasing(self):
        """Test a case where the initial element is the maximum, followed by smaller numbers."""
        self.assertEqual(rolling_max([20, 10, 5, 15, 8]), [20, 20, 20, 20, 20])

if __name__ == '__main__':
    unittest.main()