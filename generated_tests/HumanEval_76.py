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
    def test_x_is_one(self):
            # Covers the 'if x == 1: return True' branch.
            self.assertTrue(is_simple_power(1, 5))
            self.assertTrue(is_simple_power(1, 1)) # Edge case for x=1, n=1
            self.assertTrue(is_simple_power(1, 100))

    def test_n_is_one_x_greater_than_one(self):
            # Covers the 'if n == 1: return False' branch when x is not 1.
            self.assertFalse(is_simple_power(5, 1))
            self.assertFalse(is_simple_power(100, 1))

    def test_x_less_than_n(self):
            # Covers the 'if x < n: return False' branch when x > 1 and n > 1.
            self.assertFalse(is_simple_power(2, 5))
            self.assertFalse(is_simple_power(3, 4))
            self.assertFalse(is_simple_power(99, 100))

    def test_perfect_powers(self):
            # Covers the successful 'while' loop and final 'return True'.
            self.assertTrue(is_simple_power(8, 2))  # 2^3
            self.assertTrue(is_simple_power(9, 3))  # 3^2
            self.assertTrue(is_simple_power(7, 7))  # 7^1 (x == n case)
            self.assertTrue(is_simple_power(64, 4)) # 4^3
            self.assertTrue(is_simple_power(2, 2))  # 2^1 (minimal x=n case)
            self.assertTrue(is_simple_power(125, 5)) # 5^3

    def test_not_perfect_power_not_divisible(self):
            # Covers the 'if current_x % n != 0: return False' branch.
            self.assertFalse(is_simple_power(9, 2))   # 9 is not divisible by 2
            self.assertFalse(is_simple_power(10, 3))  # 10 is not divisible by 3
            self.assertFalse(is_simple_power(12, 5))  # 12 is not divisible by 5
            self.assertFalse(is_simple_power(15, 2))  # 15 is not divisible by 2

    def test_not_perfect_power_remainder_not_one(self):
            # Covers cases where initial division is successful, but the remaining
            # current_x is not 1 and not further divisible by n.
            self.assertFalse(is_simple_power(8, 4))   # 8/4 = 2, but 2 is not a power of 4
            self.assertFalse(is_simple_power(16, 8))  # 16/8 = 2, but 2 is not a power of 8
            self.assertFalse(is_simple_power(27, 9))  # 27/9 = 3, but 3 is not a power of 9
