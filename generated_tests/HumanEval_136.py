import unittest

class TestLargestSmallestIntegers(unittest.TestCase):

    def test_example_only_positives(self):
        # Example from problem description: only positive integers
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

    def test_example_empty_list(self):
        # Example from problem description: empty list
        self.assertEqual(largest_smallest_integers([]), (None, None))

    def test_example_single_zero(self):
        # Example from problem description: list with only zero
        self.assertEqual(largest_smallest_integers([0]), (None, None))

    def test_both_neg_and_pos_present(self):
        # Both negative and positive numbers are present
        self.assertEqual(largest_smallest_integers([-5, -2, 1, 3, -8, 6]), (-2, 1))

    def test_only_negatives(self):
        # Only negative numbers are present
        self.assertEqual(largest_smallest_integers([-10, -5, -1, -7]), (-1, None))

    def test_only_positives_with_zero(self):
        # Only positive numbers are present, with zeros
        self.assertEqual(largest_smallest_integers([0, 0, 10, 5, 1, 0]), (None, 1))

    def test_only_negatives_with_zero(self):
        # Only negative numbers are present, with zeros
        self.assertEqual(largest_smallest_integers([-10, 0, -5, -1, 0, -7]), (-1, None))

    def test_mixed_with_zero(self):
        # Mixed list including zero
        self.assertEqual(largest_smallest_integers([-1, 0, 1]), (-1, 1))

    def test_larger_range_and_multiple_candidates(self):
        # Larger range of numbers, multiple potential candidates
        self.assertEqual(largest_smallest_integers([-100, 200, -50, 10, -1, 5]), (-1, 5))

    def test_multiple_zeros(self):
        # List containing only zeros
        self.assertEqual(largest_smallest_integers([0, 0, 0, 0]), (None, None))