import unittest

# Assume the function 'count_n_digit_numbers' exists globally or is imported.
# For example:
# def count_n_digit_numbers(n: int) -> int:
#     if n == 1:
#         return 1
#     elif n >= 2:
#         return 18 * (10**(n - 2))
#     else:
#         # As n is a positive integer, this case should not be reached.
#         # However, a robust implementation might handle it (e.g., raise ValueError).
#         return 0

class TestCountNDigitNumbers(unittest.TestCase):

    def test_n_is_1(self):
        # For n=1, the only 1-digit number is '1'. It starts and ends with 1.
        self.assertEqual(count_n_digit_numbers(1), 1)

    def test_n_is_2(self):
        # For n=2 (numbers 10-99):
        # Starts with 1: 10, 11, ..., 19 (10 numbers)
        # Ends with 1: 11, 21, ..., 91 (9 numbers)
        # Starts AND ends with 1: 11 (1 number)
        # Total = 10 + 9 - 1 = 18
        self.assertEqual(count_n_digit_numbers(2), 18)

    def test_n_is_3(self):
        # For n=3 (numbers 100-999):
        # Based on pattern: 18 * 10^(n-2) = 18 * 10^(3-2) = 18 * 10^1 = 180
        self.assertEqual(count_n_digit_numbers(3), 180)

    def test_n_is_4(self):
        # For n=4: 18 * 10^(4-2) = 18 * 10^2 = 1800
        self.assertEqual(count_n_digit_numbers(4), 1800)

    def test_n_is_5(self):
        # For n=5: 18 * 10^(5-2) = 18 * 10^3 = 18000
        self.assertEqual(count_n_digit_numbers(5), 18000)

    def test_n_is_6(self):
        # For n=6: 18 * 10^(6-2) = 18 * 10^4 = 180000
        self.assertEqual(count_n_digit_numbers(6), 180000)

    def test_n_is_7(self):
        # For n=7: 18 * 10^(7-2) = 18 * 10^5 = 1800000
        self.assertEqual(count_n_digit_numbers(7), 1800000)

    def test_n_is_8(self):
        # For n=8: 18 * 10^(8-2) = 18 * 10^6 = 18000000
        self.assertEqual(count_n_digit_numbers(8), 18000000)

    def test_n_is_10(self):
        # For a larger value of n=10: 18 * 10^(10-2) = 18 * 10^8 = 1,800,000,000
        self.assertEqual(count_n_digit_numbers(10), 1_800_000_000)

    def test_n_is_15(self):
        # For a very large value of n=15: 18 * 10^(15-2) = 18 * 10^13
        self.assertEqual(count_n_digit_numbers(15), 180_000_000_000_000)