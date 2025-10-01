import unittest

class TestDecimalToBinary(unittest.TestCase):

    def test_zero(self):
        # Test case for input 0
        self.assertEqual(decimal_to_binary(0), "db0db")

    def test_one(self):
        # Test case for input 1
        self.assertEqual(decimal_to_binary(1), "db1db")

    def test_small_number_two(self):
        # Test case for a small number 2
        self.assertEqual(decimal_to_binary(2), "db10db")

    def test_power_of_two(self):
        # Test case for a power of two (e.g., 32)
        self.assertEqual(decimal_to_binary(32), "db100000db")

    def test_max_n_bits(self):
        # Test case for a number that is (2^n - 1), all ones (e.g., 15)
        self.assertEqual(decimal_to_binary(15), "db1111db")

    def test_another_max_n_bits(self):
        # Another test case for (2^n - 1) (e.g., 7)
        self.assertEqual(decimal_to_binary(7), "db111db")

    def test_medium_number(self):
        # Test case for a medium-sized number with mixed bits (e.g., 10)
        self.assertEqual(decimal_to_binary(10), "db1010db")

    def test_larger_power_of_two(self):
        # Test case for a larger power of two (e.g., 64)
        self.assertEqual(decimal_to_binary(64), "db1000000db")

    def test_complex_number(self):
        # Test case for a more complex number (e.g., 123)
        self.assertEqual(decimal_to_binary(123), "db1111011db")

    def test_large_number_all_ones(self):
        # Test case for a larger number that is (2^n - 1) (e.g., 255)
        self.assertEqual(decimal_to_binary(255), "db11111111db")