import unittest

class TestIsSimplePower(unittest.TestCase):

    def test_given_example_1(self):
        # x=1 is always a simple power (n**0 = 1 for any n > 0, and 1**0=1)
        self.assertTrue(is_simple_power(1, 4))

    def test_given_example_2(self):
        # x is n itself (n**1 = n)
        self.assertTrue(is_simple_power(2, 2))

    def test_given_example_3(self):
        # Basic true case
        self.assertTrue(is_simple_power(8, 2)) # 2**3 = 8

    def test_given_example_4(self):
        # Basic false case
        self.assertFalse(is_simple_power(3, 2)) # 2**1=2, 2**2=4, 3 is not a power of 2

    def test_given_example_5(self):
        # n=1, x > 1 should always be false (1 raised to any power is 1)
        self.assertFalse(is_simple_power(3, 1))

    def test_x_is_one_and_n_is_one(self):
        # x=1, n=1 is true (1**0 = 1, or 1**1 = 1)
        self.assertTrue(is_simple_power(1, 1))

    def test_x_is_one_and_n_is_large(self):
        # x=1 is true for any n > 0 (n**0 = 1)
        self.assertTrue(is_simple_power(1, 99))

    def test_large_power_case(self):
        # Test a larger number that is a power
        self.assertTrue(is_simple_power(1024, 2)) # 2**10 = 1024

    def test_large_number_not_a_power(self):
        # Test a large number that is not a power
        self.assertFalse(is_simple_power(1023, 2))

    def test_n_greater_than_x_and_not_power_of_zero(self):
        # If n > x and x != 1, it should be false (n**0=1, n**1=n > x)
        self.assertFalse(is_simple_power(5, 10))