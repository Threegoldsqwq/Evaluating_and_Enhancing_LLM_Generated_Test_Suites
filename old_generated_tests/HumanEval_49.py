import unittest

class TestModp(unittest.TestCase):

    def test_basic_small_n_p(self):
        # 2^1 % 5 = 2
        self.assertEqual(modp(1, 5), 2)

    def test_n_greater_than_p(self):
        # 2^4 % 3 = 16 % 3 = 1
        self.assertEqual(modp(4, 3), 1)

    def test_p_is_power_of_two(self):
        # 2^5 % 4 = 32 % 4 = 0
        self.assertEqual(modp(5, 4), 0)

    def test_large_n_small_prime_p(self):
        # 2^1000 % 7. Using Fermat's Little Theorem: 2^(7-1) = 2^6 = 64 = 1 (mod 7).
        # 2^1000 = 2^(166*6 + 4) = (2^6)^166 * 2^4 = 1^166 * 16 = 16 = 2 (mod 7).
        self.assertEqual(modp(1000, 7), 2)

    def test_small_n_large_p(self):
        # 2^7 % 100 = 128 % 100 = 28
        self.assertEqual(modp(7, 100), 28)

    def test_moderate_n_prime_p(self):
        # 2^200 % 13. Fermat's Little Theorem: 2^(13-1) = 2^12 = 1 (mod 13).
        # 2^200 = 2^(16*12 + 8) = (2^12)^16 * 2^8 = 1^16 * 256 = 256 (mod 13).
        # 256 = 19 * 13 + 9, so 256 = 9 (mod 13).
        self.assertEqual(modp(200, 13), 9)

    def test_result_is_p_minus_one(self):
        # 2^5 % 3 = 32 % 3 = 2 (which is 3-1)
        self.assertEqual(modp(5, 3), 2)

    def test_large_n_composite_p(self):
        # 2^60 % 10. The last digit of powers of 2 cycles: 2, 4, 8, 6, 2, ... (cycle length 4 for n >= 1)
        # 60 % 4 = 0, so it's the last element in the cycle, equivalent to 2^4 % 10 = 16 % 10 = 6.
        self.assertEqual(modp(60, 10), 6)

    def test_p_is_two(self):
        # 2^10 % 2 = 1024 % 2 = 0
        self.assertEqual(modp(10, 2), 0)

    def test_moderate_n_and_p(self):
        # 2^10 % 17 = 1024 % 17.
        # 1024 = 60 * 17 + 4, so 1024 % 17 = 4.
        self.assertEqual(modp(10, 17), 4)

# Assume the modp function is defined elsewhere for these tests to run.
# For example:
# def modp(n, p):
#     return pow(2, n, p)