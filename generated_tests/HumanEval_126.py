import unittest

class TestIsSorted(unittest.TestCase):

    def test_empty_list(self):
        # An empty list is considered sorted and has no duplicate issues.
        self.assertTrue(is_sorted([]))

    def test_single_element_list(self):
        # A single-element list is always sorted and has no duplicate issues.
        self.assertTrue(is_sorted([5]))

    def test_perfectly_sorted_no_duplicates(self):
        # A list with unique elements in ascending order.
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))

    def test_unsorted_no_duplicates(self):
        # A list with unique elements, but not in ascending order.
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))

    def test_sorted_with_one_duplicate_allowed(self):
        # A sorted list with exactly two occurrences of one number.
        self.assertTrue(is_sorted([1, 2, 2, 3, 4]))

    def test_sorted_with_multiple_duplicates_not_allowed(self):
        # A sorted list but with more than two occurrences of the same number.
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))

    def test_sorted_with_multiple_different_duplicates_allowed(self):
        # A sorted list with two different pairs of duplicates (each pair is allowed).
        self.assertTrue(is_sorted([1, 1, 2, 3, 3, 4]))

    def test_unsorted_with_one_duplicate(self):
        # An unsorted list where duplicate count would otherwise be allowed.
        self.assertFalse(is_sorted([1, 3, 2, 2, 4]))

    def test_unsorted_with_multiple_duplicates(self):
        # An unsorted list that also has more than two occurrences of a number.
        self.assertFalse(is_sorted([1, 5, 2, 2, 2, 3]))

    def test_all_elements_same_multiple_occurrences(self):
        # A list where all elements are the same, exceeding the allowed duplicate count.
        self.assertFalse(is_sorted([7, 7, 7]))
    def test_has_three_consecutive_duplicates(self):
            """
            Tests the 'if num_count > 2: return False' branch when a number appears exactly three times.
            """
            self.assertFalse(is_sorted([1, 1, 1]))

    def test_has_three_non_consecutive_duplicates(self):
            """
            Tests the 'if num_count > 2: return False' branch with non-consecutive duplicates.
            """
            self.assertFalse(is_sorted([1, 2, 1, 3, 1]))

    def test_has_four_duplicates(self):
            """
            Tests the 'if num_count > 2: return False' branch with a number appearing four times.
            """
            self.assertFalse(is_sorted([7, 7, 7, 7]))

    def test_excessive_duplicates_in_otherwise_sorted_list(self):
            """
            Tests the 'if num_count > 2: return False' branch where the list would
            otherwise be sorted in ascending order.
            """
            self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))

    def test_excessive_duplicates_unsorted_list_short_circuits(self):
            """
            Tests that the duplicate check correctly short-circuits and returns False
            even if the list is also unsorted, prioritizing the duplicate condition.
            """
            self.assertFalse(is_sorted([3, 1, 1, 1, 2]))
