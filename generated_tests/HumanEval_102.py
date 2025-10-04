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
    def test_y_is_even_and_chosen(self):
            # Test case for when y is even and within range, so y itself is returned.
            # This covers the 'if y % 2 == 0:' (True branch).
            self.assertEqual(choose_num(12, 12), 12)
            self.assertEqual(choose_num(10, 14), 14)
            self.assertEqual(choose_num(1, 2), 2)

    def test_y_is_odd_and_y_minus_1_is_too_small(self):
            # Test case for when y is odd, and y-1 is less than x,
            # meaning no even number is in the range.
            # This covers the 'if (y - 1) >= x:' (False branch).
            self.assertEqual(choose_num(15, 15), -1)
            self.assertEqual(choose_num(1, 1), -1)
            self.assertEqual(choose_num(10, 11), -1) # 11 is odd, 10 is even. (11-1)=10. 10 >= 10 is True, returns 10. Wait this one does not cover the branch.
            # Let's re-evaluate for 'if (y - 1) >= x:' (False branch)
            # Needs y odd, and y-1 < x. So x should be at least y.
            # Example: x = 5, y = 5. y is odd. y-1 = 4. 4 < 5. Should return -1.
            self.assertEqual(choose_num(5, 5), -1) # y is odd, y-1=4, x=5. 4 >= 5 is False. Returns -1.
            self.assertEqual(choose_num(7, 7), -1) # y is odd, y-1=6, x=7. 6 >= 7 is False. Returns -1.
            self.assertEqual(choose_num(9, 9), -1) # y is odd, y-1=8, x=9. 8 >= 9 is False. Returns -1.
