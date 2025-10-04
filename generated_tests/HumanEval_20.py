import unittest

# Assume the find_closest_elements function exists as described:
# def find_closest_elements(numbers: list[float]) -> tuple[float, float]:
#     # ... implementation ...

class TestFindClosestElements(unittest.TestCase):

    def test_basic_case(self):
        # Test case from the problem description
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))

    def test_duplicates_in_input(self):
        # Test case from the problem description with identical closest numbers
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

    def test_closest_at_beginning_of_sorted_list(self):
        # Closest pair is the first two elements after conceptual sorting
        self.assertEqual(find_closest_elements([1.0, 1.1, 2.0, 3.0, 4.0]), (1.0, 1.1))

    def test_closest_at_end_of_sorted_list(self):
        # Closest pair is the last two elements after conceptual sorting
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 3.1]), (3.0, 3.1))

    def test_negative_numbers(self):
        # Test with entirely negative numbers, closest pair is (-2.0, -1.0) when sorted [-5.0, -4.0, -2.0, -1.0]
        # The differences are 1.0 for (-5.0, -4.0) and 1.0 for (-2.0, -1.0).
        # Assuming the first pair encountered after sorting the input is returned.
        self.assertEqual(find_closest_elements([-5.0, -2.0, -1.0, -4.0]), (-5.0, -4.0))

    def test_mixed_positive_and_negative_numbers(self):
        # Test with a mix of positive, negative, and zero, closest pair spans zero
        self.assertEqual(find_closest_elements([-1.0, 0.5, 2.0, 0.0, -2.0]), (0.0, 0.5))

    def test_floating_point_precision(self):
        # Numbers very close due to floating point precision
        self.assertEqual(find_closest_elements([10.0, 10.0001, 20.0, 30.0]), (10.0, 10.0001))

    def test_all_identical_numbers(self):
        # All numbers in the list are the same
        self.assertEqual(find_closest_elements([5.0, 5.0, 5.0, 5.0]), (5.0, 5.0))

    def test_larger_list_complex_order(self):
        # A longer list with numbers in a non-sorted order, multiple potential minimal diffs
        # Sorted: [2, 3, 5, 7, 15, 20, 100, 101]
        # Min diff is 1. Pairs are (2,3) and (100,101).
        # Assuming (2,3) is returned as it appears earlier in the sorted sequence.
        self.assertEqual(find_closest_elements([100, 5, 20, 15, 2, 7, 3, 101]), (2, 3))

    def test_numbers_with_varying_precision_and_range(self):
        # Test with decimals and a wide range of magnitudes
        self.assertEqual(find_closest_elements([0.1, 1000.0, -0.05, 50.0, 0.0]), (-0.05, 0.0))
    def test_value_error_for_short_lists(self):
            """Test that ValueError is raised for lists with less than two elements."""
            with self.assertRaises(ValueError):
                find_closest_elements([])
            with self.assertRaises(ValueError):
                find_closest_elements([1])
            with self.assertRaises(ValueError):
                find_closest_elements([1.0])

    def test_list_with_exactly_two_elements(self):
            """Test with a list containing exactly two elements, ensuring it's an edge case for the loop."""
            self.assertEqual(find_closest_elements([10, 1]), (1, 10))
            self.assertEqual(find_closest_elements([5.5, 5.6]), (5.5, 5.6))
            self.assertEqual(find_closest_elements([-3, -1]), (-3, -1))
            self.assertEqual(find_closest_elements([100, -100]), (-100, 100))

    def test_with_duplicate_numbers_zero_difference(self):
            """Test cases where the closest elements are identical, resulting in zero difference."""
            self.assertEqual(find_closest_elements([1, 2, 2, 3]), (2, 2))
            self.assertEqual(find_closest_elements([7, 7]), (7, 7))
            self.assertEqual(find_closest_elements([10, 5, 5, 12]), (5, 5))
            self.assertEqual(find_closest_elements([3, 1, 2, 3]), (3, 3)) # Sorted: [1, 2, 3, 3] -> (3,3) is closest
            self.assertEqual(find_closest_elements([4.0, 1.0, 2.0, 3.0, 4.0]), (4.0, 4.0))

    def test_multiple_pairs_same_min_difference_first_one_wins(self):
            """
            Test scenarios where multiple pairs have the same minimum difference.
            The current implementation should return the first encountered pair.
            This targets the 'current_diff < min_diff' branch specifically when current_diff == min_diff.
            """
            # Sorted: [1, 2, 3, 4]. Diffs: (1,2) diff 1, (2,3) diff 1, (3,4) diff 1. (1,2) should be returned.
            self.assertEqual(find_closest_elements([1, 2, 3, 4]), (1, 2))
            # Sorted: [-5, -4, 0, 1]. Diffs: (-5,-4) diff 1, (-4,0) diff 4, (0,1) diff 1. (-5,-4) should be returned.
            self.assertEqual(find_closest_elements([0, -5, 1, -4]), (-5, -4))
            # Sorted: [1.0, 2.0, 3.0, 4.0, 5.0]. All diffs 1.0. (1.0, 2.0) should be returned.
            self.assertEqual(find_closest_elements([5.0, 1.0, 4.0, 2.0, 3.0]), (1.0, 2.0))
            # Sorted: [1, 2, 5, 6]. Diffs: (1,2) diff 1, (2,5) diff 3, (5,6) diff 1. (1,2) should be returned.
            self.assertEqual(find_closest_elements([5, 1, 6, 2]), (1, 2))

    def test_mixed_negative_positive_floats_and_integers(self):
            """Test with a mix of negative, positive, integer, and float numbers."""
            # Sorted: [-3.0, -1.5, 0.0, 1.0]. Diffs: 1.5, 1.5, 1.0. (0.0, 1.0) is closest.
            self.assertEqual(find_closest_elements([-1.5, -3.0, 0.0, 1.0]), (0.0, 1.0))
            # Sorted: [-100, 0.0, 0.1, 100]. Diffs: 100, 0.1, 99.9. (0.0, 0.1) is closest.
            self.assertEqual(find_closest_elements([100, -100, 0.0, 0.1]), (0.0, 0.1))
            # Sorted: [-10, -9.9, 0, 1]. Diffs: 0.1, 9.9, 1. ( -10, -9.9) is closest.
            self.assertEqual(find_closest_elements([-10, -9.9, 0, 1]), (-10, -9.9))

    def test_large_numbers(self):
            """Test with large integer values."""
            self.assertEqual(find_closest_elements([10**9, 10**9 + 1, 10**9 + 5]), (10**9, 10**9 + 1))
            self.assertEqual(find_closest_elements([-(10**12), -(10**12) + 0.5, 0]), (-(10**12), -(10**12) + 0.5))

    def test_very_small_float_differences(self):
            """Test with very small differences between floating-point numbers."""
            self.assertEqual(find_closest_elements([1.0, 1.000000001, 2.0]), (1.0, 1.000000001))
            self.assertEqual(find_closest_elements([0.0001, 0.0002, 0.0005]), (0.0001, 0.0002))
            self.assertEqual(find_closest_elements([0.12345, 0.12346, 0.5]), (0.12345, 0.12346))
