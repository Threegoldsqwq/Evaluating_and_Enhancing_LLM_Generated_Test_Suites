import unittest

# Assume the 'unique' function is defined elsewhere, e.g.:
# def unique(input_list):
#     return sorted(list(set(input_list)))

class TestUniqueFunction(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

    def test_empty_list(self):
        self.assertEqual(unique([]), [])

    def test_no_duplicates_already_sorted(self):
        self.assertEqual(unique([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_no_duplicates_unsorted(self):
        self.assertEqual(unique([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])

    def test_all_elements_are_duplicates(self):
        self.assertEqual(unique([7, 7, 7, 7, 7]), [7])

    def test_single_element_list(self):
        self.assertEqual(unique([42]), [42])

    def test_list_with_negative_numbers(self):
        self.assertEqual(unique([-3, -1, -3, -2, 0]), [-3, -2, -1, 0])

    def test_mixed_positive_and_negative_with_duplicates(self):
        self.assertEqual(unique([-5, 10, 0, -5, 2, 10, 1]), [-5, 0, 1, 2, 10])

    def test_large_numbers_and_many_duplicates(self):
        self.assertEqual(unique([1000, 1, 500, 1000, 1, 999, 500, 12345]), [1, 500, 999, 1000, 12345])

    def test_elements_in_descending_order_with_duplicates(self):
        self.assertEqual(unique([10, 8, 10, 6, 8, 4, 2]), [2, 4, 6, 8, 10])

if __name__ == '__main__':
    # This mock 'unique' function is here just to make the test file runnable independently
    # In a real scenario, you would import the actual 'unique' function.
    # def unique(input_list):
    #     return sorted(list(set(input_list)))

    unittest.main(argv=['first-arg-is-ignored'], exit=False)