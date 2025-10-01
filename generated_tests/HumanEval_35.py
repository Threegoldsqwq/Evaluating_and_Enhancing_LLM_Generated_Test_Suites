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