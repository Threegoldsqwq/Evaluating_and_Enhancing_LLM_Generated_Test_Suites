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