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
    def test_mixed_numbers_with_no_update(self):
            """
            Tests a mixed list where sometimes a new number does not update
            largest_negative (because it's smaller) or smallest_positive
            (because it's larger), covering the 'false' branches of update conditions.
            """
            numbers = [-5, 0, -10, 3, 1, 0, -2, 7]
            # -5 -> largest_negative = -5
            # 0 -> ignored
            # -10 -> -10 is not > -5, largest_negative remains -5 (covers branch: num <= largest_negative)
            # 3 -> smallest_positive = 3
            # 1 -> smallest_positive = 1
            # 0 -> ignored
            # -2 -> -2 > -5, largest_negative = -2
            # 7 -> 7 is not < 1, smallest_positive remains 1 (covers branch: num >= smallest_positive)
            self.assertEqual(largest_smallest_integers(numbers), (-2, 1))

    def test_single_negative_number(self):
            """
            Tests a list containing only a single negative number.
            """
            self.assertEqual(largest_smallest_integers([-100]), (-100, None))

    def test_single_positive_number(self):
            """
            Tests a list containing only a single positive number.
            """
            self.assertEqual(largest_smallest_integers([200]), (None, 200))

    def test_all_zeros_multiple(self):
            """
            Tests a list containing multiple zeros.
            """
            self.assertEqual(largest_smallest_integers([0, 0, 0, 0]), (None, None))

    def test_negative_numbers_decreasing_order(self):
            """
            Tests a list of negative numbers where subsequent numbers are smaller,
            ensuring largest_negative doesn't incorrectly update.
            """
            self.assertEqual(largest_smallest_integers([-2, -5, -1, -10]), (-1, None))

    def test_positive_numbers_increasing_order(self):
            """
            Tests a list of positive numbers where subsequent numbers are larger,
            ensuring smallest_positive doesn't incorrectly update.
            """
            self.assertEqual(largest_smallest_integers([10, 50, 5, 100]), (None, 5))
