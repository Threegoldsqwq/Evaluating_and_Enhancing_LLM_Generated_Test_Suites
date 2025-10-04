import unittest

class TestMaxElement(unittest.TestCase):

    def test_positive_integers_simple(self):
        self.assertEqual(max_element([1, 2, 3]), 3)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

    def test_all_negative_integers(self):
        self.assertEqual(max_element([-1, -5, -2, -10]), -1)

    def test_single_element_list(self):
        self.assertEqual(max_element([7]), 7)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            max_element([])

    def test_duplicate_maximums(self):
        self.assertEqual(max_element([10, 5, 10, 3]), 10)

    def test_list_with_zero_and_positives(self):
        self.assertEqual(max_element([-1, 0, 5]), 5)

    def test_descending_list(self):
        self.assertEqual(max_element([10, 9, 8, 1]), 10)

    def test_ascending_list(self):
        self.assertEqual(max_element([1, 2, 3, 10]), 10)

    def test_large_numbers(self):
        self.assertEqual(max_element([1000000, 999999, 1000001]), 1000001)

    def test_single_element_list(self):
            # Test cases for lists containing exactly one element.
            # This ensures the loop `for element in data[1:]` is correctly skipped
            # and the single element is returned.
            self.assertEqual(max_element([42]), 42)
            self.assertEqual(max_element([-7]), -7)
            self.assertEqual(max_element([0]), 0)

    def test_all_elements_equal(self):
            # Test case where all elements in the list are identical.
            # This ensures that `max_val` is not updated when `element > max_val` is false due to equality.
            self.assertEqual(max_element([5, 5, 5, 5]), 5)
            self.assertEqual(max_element([-3, -3]), -3)
            self.assertEqual(max_element([0.0, 0.0, 0.0]), 0.0)

    def test_decreasing_order(self):
            # Test case where elements are in strictly decreasing order.
            # This confirms that `max_val` remains the first element if no larger element is found,
            # ensuring the `if element > max_val` condition is always false.
            self.assertEqual(max_element([10, 8, 6, 4]), 10)
            self.assertEqual(max_element([0, -1, -5]), 0)
            self.assertEqual(max_element([5.5, 4.4, 3.3]), 5.5)

    def test_mixed_floats(self):
            # Test cases involving float numbers to ensure the function handles them correctly.
            # Includes positive, negative, and mixed float scenarios.
            self.assertEqual(max_element([1.2, 3.4, 0.5, 2.1]), 3.4)
            self.assertEqual(max_element([-1.2, -3.4, -0.5, -2.1]), -0.5)
            self.assertEqual(max_element([0.0, -1.0, 1.0]), 1.0)
            self.assertEqual(max_element([-5.0]), -5.0) # Single element float
# Assuming max_element function exists in the same scope or imported
# Example placeholder for max_element to make tests runnable if needed:
# def max_element(numbers):
#     if not numbers:
#         raise ValueError("max_element() arg is an empty sequence")
#     max_val = numbers[0]
#     for num in numbers:
#         if num > max_val:
#             max_val = num
#     return max_val