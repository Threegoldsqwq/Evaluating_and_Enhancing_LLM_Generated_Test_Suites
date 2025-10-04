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


# To run these tests, you would typically have the generate_integers function defined
# and then use:
# if __name__ == '__main__':
#     unittest.main()