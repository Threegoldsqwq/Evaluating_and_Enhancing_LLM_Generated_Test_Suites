import unittest

class TestChooseNum(unittest.TestCase):

    def test_example_one(self):
        # Example from problem description: normal case, y is odd
        self.assertEqual(choose_num(12, 15), 14)

    def test_example_two(self):
        # Example from problem description: x > y, no number in range
        self.assertEqual(choose_num(13, 12), -1)

    def test_range_contains_only_odd_numbers(self):
        # Case where both x and y are odd, and no even number exists between them
        self.assertEqual(choose_num(13, 13), -1)

    def test_range_contains_only_even_number_at_start(self):
        # Case where x is even and y is x
        self.assertEqual(choose_num(20, 20), 20)

    def test_range_contains_only_even_number_at_end(self):
        # Case where x is odd and y is even, and y is the only even number
        self.assertEqual(choose_num(1, 2), 2)

    def test_range_contains_multiple_even_numbers_both_odd_bounds(self):
        # Case where both x and y are odd, but multiple even numbers exist
        self.assertEqual(choose_num(13, 17), 16)

    def test_range_contains_multiple_even_numbers_x_even_y_odd(self):
        # Case where x is even, y is odd, multiple even numbers exist
        self.assertEqual(choose_num(20, 25), 24)

    def test_range_contains_multiple_even_numbers_x_odd_y_even(self):
        # Case where x is odd, y is even, multiple even numbers exist
        self.assertEqual(choose_num(5, 8), 8)

    def test_no_even_number_in_small_odd_range(self):
        # Smallest range with no even numbers, x and y are both odd
        self.assertEqual(choose_num(1, 1), -1)

    def test_large_range_with_many_even_numbers(self):
        # Test with a larger range to ensure correct maximum is found
        self.assertEqual(choose_num(100, 201), 200)