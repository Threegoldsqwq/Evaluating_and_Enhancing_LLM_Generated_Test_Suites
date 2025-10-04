import unittest

class TestTruncateNumber(unittest.TestCase):

    def test_positive_number_with_decimals(self):
        # Example given in the problem description
        self.assertAlmostEqual(truncate_number(3.5), 0.5)

    def test_number_less_than_one(self):
        # A positive number where the integer part is 0
        self.assertAlmostEqual(truncate_number(0.75), 0.75)

    def test_exact_integer(self):
        # A positive integer, decimal part should be 0.0
        self.assertAlmostEqual(truncate_number(10.0), 0.0)

    def test_another_number_less_than_one(self):
        # Another positive number less than one
        self.assertAlmostEqual(truncate_number(0.123), 0.123)

    def test_large_number_with_decimals(self):
        # A large positive number with a decimal part
        self.assertAlmostEqual(truncate_number(12345.678), 0.678)

    def test_number_close_to_next_integer(self):
        # A positive number with a decimal part very close to 1
        self.assertAlmostEqual(truncate_number(99.99), 0.99)

    def test_number_with_very_small_decimal_part(self):
        # A positive number with a tiny decimal part
        self.assertAlmostEqual(truncate_number(1.000000000000001), 0.000000000000001)

    def test_another_exact_integer(self):
        # Another positive exact integer
        self.assertAlmostEqual(truncate_number(7.0), 0.0)

    def test_number_with_many_decimal_places(self):
        # A positive number with several decimal places
        self.assertAlmostEqual(truncate_number(5.123456789), 0.123456789)

    def test_number_very_close_to_one_decimal_part(self):
        # A positive number with a decimal part very close to 1, but still less than 1
        self.assertAlmostEqual(truncate_number(0.99999), 0.99999)
    def test_zero_input(self):
            # Test with 0.0, which is an important edge case for positive (non-negative) numbers.
            # This ensures the integer part of 0.0 (which is 0) is handled correctly.
            self.assertAlmostEqual(truncate_number(0.0), 0.0)

    def test_very_small_decimal(self):
            # Test with a very small positive decimal number where the integer part is 0.
            # This covers inputs close to zero but not zero itself.
            self.assertAlmostEqual(truncate_number(0.0000000001), 0.0000000001)

    def test_very_large_number_with_decimal(self):
            # Test with a very large positive floating-point number that has a decimal part.
            # This ensures the function handles large integer and decimal components correctly.
            self.assertAlmostEqual(truncate_number(1234567891234567890123.456789), 0.456789)

    def test_number_with_high_precision_decimal(self):
            # Test a number with many decimal places to check for precision handling.
            self.assertAlmostEqual(truncate_number(7.1234567891234567), 0.1234567891234567)

    def test_another_exact_integer(self):
            # Test another positive number that is exactly an integer (e.g., 100.0),
            # confirming its decimal part is 0.0. This is similar to test_zero_input
            # but for a non-zero integer.
            self.assertAlmostEqual(truncate_number(100.0), 0.0)
