import unittest

class TestRemoveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        # Test case: An empty list should return an empty list.
        self.assertEqual(remove_duplicates([]), [])

    def test_no_duplicates(self):
        # Test case: A list with no duplicate elements should remain unchanged.
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_duplicates(self):
        # Test case: A list where all elements occur more than once.
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), [])

    def test_mixed_duplicates_simple(self):
        # Test case: Basic example given in problem description.
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_duplicates_at_beginning(self):
        # Test case: Duplicates appearing at the start of the list.
        self.assertEqual(remove_duplicates([5, 5, 1, 2, 3]), [1, 2, 3])

    def test_duplicates_at_end(self):
        # Test case: Duplicates appearing at the end of the list.
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 4]), [1, 2, 3])

    def test_multiple_distinct_duplicates(self):
        # Test case: Multiple different numbers appear more than once.
        self.assertEqual(remove_duplicates([1, 2, 3, 1, 4, 2, 5]), [3, 4, 5])

    def test_with_negative_numbers_and_zero(self):
        # Test case: List contains negative numbers and zero, with duplicates.
        self.assertEqual(remove_duplicates([-1, 0, -1, 2, 0, 3]), [2, 3])

    def test_large_list_complex_duplicates(self):
        # Test case: A larger list with various patterns of duplicates.
        self.assertEqual(remove_duplicates([10, 20, 30, 20, 10, 40, 50, 30, 60, 70, 70]), [40, 50, 60])

    def test_all_elements_are_duplicates_but_distinct(self):
        # Test case: Every element appears exactly twice.
        self.assertEqual(remove_duplicates([1, 2, 1, 3, 2, 3]), [])