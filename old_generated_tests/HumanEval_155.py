import unittest

class TestEvenOddCount(unittest.TestCase):

    def test_example_positive(self):
        # Example from problem description
        self.assertEqual(even_odd_count(123), (1, 2))

    def test_example_negative(self):
        # Example from problem description, digits are counted regardless of sign
        self.assertEqual(even_odd_count(-12), (1, 1))

    def test_zero_input(self):
        # Zero is considered an even digit
        self.assertEqual(even_odd_count(0), (1, 0))

    def test_all_even_digits(self):
        # Number with all even digits
        self.assertEqual(even_odd_count(2468), (4, 0))

    def test_all_odd_digits(self):
        # Number with all odd digits
        self.assertEqual(even_odd_count(13579), (0, 5))

    def test_mixed_digits_with_zeros(self):
        # Number with mixed digits including zeros (0 is even)
        self.assertEqual(even_odd_count(102030), (4, 2))

    def test_single_even_digit(self):
        # Single even digit
        self.assertEqual(even_odd_count(8), (1, 0))

    def test_single_odd_digit(self):
        # Single odd digit
        self.assertEqual(even_odd_count(7), (0, 1))

    def test_negative_all_odd_digits(self):
        # Negative number with all odd digits
        self.assertEqual(even_odd_count(-135), (0, 3))

    def test_large_mixed_number(self):
        # A larger number with a mix of even and odd digits
        self.assertEqual(even_odd_count(9876543210), (5, 5))