import unittest

class TestCommon(unittest.TestCase):

    def test_example_1(self):
        # Example from the problem description
        list1 = [1, 4, 3, 34, 653, 2, 5]
        list2 = [5, 7, 1, 5, 9, 653, 121]
        expected = [1, 5, 653]
        self.assertEqual(common(list1, list2), expected)

    def test_example_2(self):
        # Another example from the problem description
        list1 = [5, 3, 2, 8]
        list2 = [3, 2]
        expected = [2, 3]
        self.assertEqual(common(list1, list2), expected)

    def test_no_common_elements(self):
        # Lists with no shared elements
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        expected = []
        self.assertEqual(common(list1, list2), expected)

    def test_one_common_element(self):
        # Lists sharing only one element
        list1 = [10, 20, 30]
        list2 = [30, 40, 50]
        expected = [30]
        self.assertEqual(common(list1, list2), expected)

    def test_empty_first_list(self):
        # One of the lists is empty
        list1 = []
        list2 = [1, 2, 3]
        expected = []
        self.assertEqual(common(list1, list2), expected)

    def test_empty_second_list(self):
        # One of the lists is empty
        list1 = [1, 2, 3]
        list2 = []
        expected = []
        self.assertEqual(common(list1, list2), expected)

    def test_both_empty_lists(self):
        # Both lists are empty
        list1 = []
        list2 = []
        expected = []
        self.assertEqual(common(list1, list2), expected)

    def test_duplicates_in_input(self):
        # Ensure duplicates in input lists are handled and output is unique and sorted
        list1 = [1, 1, 2, 3, 3, 4]
        list2 = [1, 2, 2, 5, 3]
        expected = [1, 2, 3]
        self.assertEqual(common(list1, list2), expected)

    def test_all_elements_common(self):
        # Both lists contain the same elements, possibly in different order
        list1 = [5, 2, 8, 1]
        list2 = [8, 1, 5, 2]
        expected = [1, 2, 5, 8]
        self.assertEqual(common(list1, list2), expected)

    def test_negative_numbers_and_zero(self):
        # Test with negative numbers and zero
        list1 = [-5, 0, 1, -2, 7]
        list2 = [0, -2, 9, -5, 3]
        expected = [-5, -2, 0]
        self.assertEqual(common(list1, list2), expected)
    def test_no_common_elements(self):
            """Test with two lists that have no common elements."""
            list1 = [1, 2, 3]
            list2 = [4, 5, 6]
            self.assertEqual(self.solution.common(list1, list2), [])

    def test_all_elements_common(self):
            """Test with two identical lists."""
            list1 = [10, 20, 30]
            list2 = [10, 20, 30]
            self.assertEqual(self.solution.common(list1, list2), [10, 20, 30])

    def test_all_elements_common_different_order(self):
            """Test with two lists containing the same elements but in different order."""
            list1 = [30, 10, 20]
            list2 = [20, 30, 10]
            self.assertEqual(self.solution.common(list1, list2), [10, 20, 30])

    def test_both_lists_empty(self):
            """Test with both input lists being empty."""
            self.assertEqual(self.solution.common([], []), [])

    def test_with_negative_numbers(self):
            """Test with lists containing negative numbers and zero."""
            list1 = [-1, -5, 0, 3]
            list2 = [0, -5, 2, -1]
            self.assertEqual(self.solution.common(list1, list2), [-5, -1, 0])

    def test_with_strings(self):
            """Test with lists containing string elements."""
            list1 = ['apple', 'banana', 'orange']
            list2 = ['grape', 'orange', 'apple']
            self.assertEqual(self.solution.common(list1, list2), ['apple', 'orange'])

    def test_single_common_element(self):
            """Test with lists having only one common element."""
            list1 = [10]
            list2 = [10]
            self.assertEqual(self.solution.common(list1, list2), [10])

    def test_single_non_common_element(self):
            """Test with lists having a single element each, but no common element."""
            list1 = [10]
            list2 = [20]
            self.assertEqual(self.solution.common(list1, list2), [])

    def test_one_list_subset_of_other_with_duplicates(self):
            """Test where one list is a subset of the other, with duplicates in the superset."""
            list1 = [1, 2, 3, 2, 1]
            list2 = [1, 2]
            self.assertEqual(self.solution.common(list1, list2), [1, 2])

    def test_mixed_data_types_with_common(self):
            """Test with lists containing mixed data types (that are hashable and comparable)."""
            list1 = [1, 'a', None, 2.5]
            list2 = [None, 'a', 3, 2.5]
            # None sorts before numbers/strings in Python 3.x if explicitly allowed
            self.assertEqual(self.solution.common(list1, list2), [None, 2.5, 'a'])

    def test_mixed_case_strings_no_common(self):
            """Test with string elements of mixed case where case differences lead to no common elements."""
            list1 = ["Apple", "banana", "Cherry"]
            list2 = ["apple", "BANANA", "cherry"]
            self.assertEqual(self.solution.common(list1, list2), [])

    def test_large_lists_with_many_common_elements(self):
            """Test with large lists that share many elements."""
            list1 = list(range(1, 1000))
            list2 = list(range(500, 1500))
            expected_common = list(range(500, 1000))
            self.assertEqual(self.solution.common(list1, list2), expected_common)
