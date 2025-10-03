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