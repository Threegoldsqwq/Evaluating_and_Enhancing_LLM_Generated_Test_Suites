import unittest

class TestIncrList(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

    def test_example_2(self):
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

    def test_empty_list(self):
        self.assertEqual(incr_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(incr_list([7]), [8])

    def test_list_with_zeros(self):
        self.assertEqual(incr_list([0, 0, 0]), [1, 1, 1])

    def test_list_with_negative_numbers(self):
        self.assertEqual(incr_list([-1, -5, -10]), [0, -4, -9])

    def test_list_with_mixed_numbers(self):
        self.assertEqual(incr_list([-2, 0, 5, -1, 100]), [-1, 1, 6, 0, 101])

    def test_list_with_large_numbers(self):
        self.assertEqual(incr_list([999999, 123456789]), [1000000, 123456790])

    def test_list_with_duplicate_numbers(self):
        self.assertEqual(incr_list([1, 1, 2, 2, 3, 3]), [2, 2, 3, 3, 4, 4])

    def test_list_with_floating_point_numbers(self):
        # Assuming integers based on examples, but good to check if it handles floats or raises error.
        # If the problem statement strictly implies integers, this might be outside scope.
        # However, a robust implementation should handle them or specify type constraints.
        # For this exercise, I'll assume it handles numeric types generally.
        self.assertEqual(incr_list([1.0, 2.5, 3.7]), [2.0, 3.5, 4.7])