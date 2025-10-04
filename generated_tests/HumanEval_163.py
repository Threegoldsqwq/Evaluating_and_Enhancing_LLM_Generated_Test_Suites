import unittest

class TestGenerateIntegers(unittest.TestCase):

    def test_basic_range(self):
        # Example case: a < b, includes multiple even digits
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_basic_range_reversed(self):
        # Example case: a > b, includes multiple even digits
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_no_even_digits_in_range(self):
        # Example case: range does not contain any single-digit even numbers
        self.assertEqual(generate_integers(10, 14), [])

    def test_no_even_digits_in_range_reversed(self):
        # Similar to above, but with a > b
        self.assertEqual(generate_integers(14, 10), [])



    def test_single_even_digit_in_range(self):
        # Range contains only one even digit
        self.assertEqual(generate_integers(3, 5), [4])

    def test_start_and_end_are_same_even_digit(self):
        # Both a and b are the same even digit
        self.assertEqual(generate_integers(6, 6), [6])

    def test_start_and_end_are_same_odd_digit(self):
        # Both a and b are the same odd digit, no even digits found
        self.assertEqual(generate_integers(7, 7), [])


    def test_equal_bounds_digit_found(self):
            # Test case where 'a' and 'b' are equal, and that value is one of the even digits.
            # This exercises the 'a == b' branch for the min and max functions on line 1.
            self.assertEqual(self.solution.generate_integers(4, 4), [4])
            self.assertEqual(self.solution.generate_integers(2, 2), [2])
            self.assertEqual(self.solution.generate_integers(6, 6), [6])
            self.assertEqual(self.solution.generate_integers(8, 8), [8])

    def test_equal_bounds_no_digit_found(self):
            # Test case where 'a' and 'b' are equal, but that value is not an even digit
            # within the target range [2, 8].
            # This also exercises the 'a == b' branch for the min and max functions on line 1.
            self.assertEqual(self.solution.generate_integers(1, 1), [])
            self.assertEqual(self.solution.generate_integers(3, 3), [])
            self.assertEqual(self.solution.generate_integers(9, 9), [])
            # Test for values outside the target even digits range [2, 8]
            self.assertEqual(self.solution.generate_integers(10, 10), [])
            self.assertEqual(self.solution.generate_integers(100, 100), [])
# To run these tests, you would typically have the generate_integers function defined
# and then use:
# if __name__ == '__main__':
#     unittest.main()