import unittest

# Assume the next_smallest function exists in a module, e.g., 'your_module'
# from your_module import next_smallest 

class TestNextSmallest(unittest.TestCase):

    def test_empty_list(self):
        # Test case for an empty list
        self.assertIsNone(next_smallest([]))

    def test_single_element_list(self):
        # Test case for a list with only one element
        self.assertIsNone(next_smallest([42]))

    def test_all_elements_same_multiple(self):
        # Test case where all elements are identical
        self.assertIsNone(next_smallest([5, 5, 5, 5]))

    def test_two_identical_elements(self):
        # Test case for a list with two identical elements (should return None)
        self.assertIsNone(next_smallest([7, 7]))

    def test_basic_sorted_unique_elements(self):
        # Test case for a sorted list with distinct elements
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)

    def test_unsorted_unique_elements(self):
        # Test case for an unsorted list with distinct elements
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)

    def test_duplicates_smallest_is_unique(self):
        # Test case with duplicates where the smallest is unique, and 2nd smallest exists
        self.assertEqual(next_smallest([1, 1, 2, 3, 4]), 2)

    def test_negative_numbers(self):
        # Test case involving negative numbers
        self.assertEqual(next_smallest([-5, -1, -4, -3, -2]), -4)

    def test_mixed_numbers_with_zero(self):
        # Test case with mixed positive, negative, and zero
        self.assertEqual(next_smallest([-10, 0, 5, -2, 1]), -2)

    def test_two_unique_elements_smallest_duplicated(self):
        # Test case with only two unique numbers, where the smallest is duplicated
        self.assertEqual(next_smallest([10, 10, 10, 20]), 20)

# To run these tests, you would typically have the next_smallest function defined
# and then use:
# if __name__ == '__main__':
#     unittest.main()