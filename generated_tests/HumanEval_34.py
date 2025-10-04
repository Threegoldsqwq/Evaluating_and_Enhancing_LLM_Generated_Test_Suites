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

    def test_unique_only_negative_numbers(self):
            # Test with a list containing only negative integers, including duplicates.
            self.assertEqual(unique([-5, -3, -5, -2, -3, -3, -9]), [-9, -5, -3, -2])
            self.assertEqual(unique([-1, -1, -1]), [-1])
            self.assertEqual(unique([-100]), [-100])

    def test_unique_with_only_zero(self):
            # Test with a list containing only the number zero.
            self.assertEqual(unique([0, 0, 0, 0]), [0])
            self.assertEqual(unique([0]), [0])

    def test_unique_large_number_of_duplicates(self):
            # Test with a very large list dominated by duplicate elements.
            input_list = [5] * 10000 + [1, 2, 3] + [5] * 5000 + [4]
            expected_output = [1, 2, 3, 4, 5]
            self.assertEqual(unique(input_list), expected_output)

    def test_unique_large_number_of_unique_elements_reverse_order(self):
            # Test with a large list of unique elements provided in reverse sorted order.
            input_list = list(range(2000, 0, -1)) # e.g., [2000, 1999, ..., 1]
            expected_output = list(range(1, 2001)) # e.g., [1, 2, ..., 2000]
            self.assertEqual(unique(input_list), expected_output)

    def test_unique_extreme_integer_values(self):
            # Test with very large positive and negative integers.
            # Python integers have arbitrary precision, so these values are handled.
            large_int_pos = 10**100
            large_int_neg = -(10**100)
            input_list = [large_int_pos, 0, large_int_neg, large_int_pos, 1]
            expected_output = [large_int_neg, 0, 1, large_int_pos]
            self.assertEqual(unique(input_list), expected_output)

    def test_unique_with_non_comparable_types_raises_type_error(self):
            # Test case where the input list contains elements of non-comparable types,
            # which should cause sorted() to raise a TypeError. This addresses an
            # implicit branch for error handling in the sorted() call, as the code
            # must handle the case where elements are not sortable, despite the type hint.

            # int and str are not comparable for sorting
            with self.assertRaises(TypeError):
                unique([1, 'a', 2])

            # int and None are not comparable for sorting
            with self.assertRaises(TypeError):
                unique([1, None, 2])

            # int and a dictionary are not comparable for sorting
            with self.assertRaises(TypeError):
                unique([1, {}, 2])
if __name__ == '__main__':
    # This mock 'unique' function is here just to make the test file runnable independently
    # In a real scenario, you would import the actual 'unique' function.
    # def unique(input_list):
    #     return sorted(list(set(input_list)))

    unittest.main(argv=['first-arg-is-ignored'], exit=False)