import unittest

class TestMedian(unittest.TestCase):

    def test_odd_elements_basic(self):
        # Given example 1
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_even_elements_basic(self):
            # Given example 2
            # The sorted list is [-10, 4, 6, 10, 20, 1000]
            # The two middle elements are 6 and 10.
            # Their average is (6 + 10) / 2 = 16 / 2 = 8.0
            self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 8.0)
    def test_single_element_list(self):
        self.assertEqual(median([42]), 42)

    def test_odd_elements_with_negatives_and_zero(self):
        self.assertEqual(median([-5, 0, 1, -2, 3]), 0)

    def test_even_elements_with_negatives(self):
        self.assertEqual(median([-10, -20, -30, -40]), -25.0)

    def test_all_elements_same_odd_count(self):
        self.assertEqual(median([7, 7, 7, 7, 7]), 7)

    def test_all_elements_same_even_count(self):
        self.assertEqual(median([8, 8, 8, 8]), 8.0)

    def test_large_numbers_mixed(self):
        self.assertEqual(median([1000, 500, 2000, 1500, 0, 2500]), 1250.0)

    def test_list_already_sorted_odd(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)

    def test_list_reverse_sorted_even(self):
        self.assertEqual(median([10, 8, 6, 4]), 7.0)

    def test_median_even_length_lists(self):
            # This test method specifically targets line 22, which handles
            # the calculation for lists with an even number of elements.
            # It also implicitly covers line 1 (function definition) as the function is called.

            # Test with the smallest even-length list
            self.assertEqual(median([1, 2]), 1.5)
            self.assertEqual(median([2, 1]), 1.5) # Test unsorted input

            # Test with a larger even-length list from the docstring example
            self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 8.0)
            self.assertEqual(median([20, 10, 1000, 6, 4, -10]), 8.0) # Unsorted version

            # Test with duplicate values
            self.assertEqual(median([5, 5, 5, 5]), 5.0)
            self.assertEqual(median([10, 20, 20, 10]), 15.0)

            # Test with negative numbers
            self.assertEqual(median([-5, -3]), -4.0)
            self.assertEqual(median([-10, -5, 0, 5]), -2.5)

            # Test with float values
            self.assertEqual(median([1.5, 2.5, 3.5, 4.5]), 3.0)
            self.assertEqual(median([0.1, 0.2, 0.3, 0.4, 0.5, 0.6]), 0.35)
# Assume the 'median' function is defined elsewhere for these tests to run.
# For example:
# def median(l):
#     if not l:
#         raise ValueError("Cannot compute median of an empty list.")
#     sorted_l = sorted(l)
#     n = len(sorted_l)
#     if n % 2 == 1:
#         return sorted_l[n // 2]
#     else:
#         mid1 = sorted_l[n // 2 - 1]
#         mid2 = sorted_l[n // 2]
#         return (mid1 + mid2) / 2.0

if __name__ == '__main__':
    # This dummy median function is just for the tests to be executable
    # in case someone tries to run this file directly without the actual problem function.
    # In a real scenario, the 'median' function would be imported or defined.
    def median(l):
        if not l:
            raise ValueError("Cannot compute median of an empty list.")
        sorted_l = sorted(l)
        n = len(sorted_l)
        if n % 2 == 1:
            return sorted_l[n // 2]
        else:
            mid1 = sorted_l[n // 2 - 1]
            mid2 = sorted_l[n // 2]
            return (mid1 + mid2) / 2.0

    unittest.main(argv=['first-arg-is-ignored'], exit=False)