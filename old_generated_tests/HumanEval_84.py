import unittest

# Assume the function 'solve' (or whatever it's named) exists elsewhere.
# For example, it might look like this:
# def solve(N: int) -> str:
#     """
#     Given a positive integer N, return the total sum of its digits in binary.
#     """
#     # Calculate sum of digits
#     s_digits = 0
#     temp_N = N
#     if temp_N == 0:
#         s_digits = 0
#     else:
#         while temp_N > 0:
#             s_digits += temp_N % 10
#             temp_N //= 10
#
#     # Convert sum to binary string
#     if s_digits == 0:
#         return "0"
#     return bin(s_digits)[2:]


class TestSumOfDigitsInBinary(unittest.TestCase):

    def test_case_0(self):
        # Smallest N allowed, sum is 0
        N = 0
        # Sum of digits of 0 is 0
        # Binary of 0 is "0"
        self.assertEqual(solve(N), "0")

    def test_case_1(self):
        # Single digit N, sum is 1
        N = 1
        # Sum of digits of 1 is 1
        # Binary of 1 is "1"
        self.assertEqual(solve(N), "1")

    def test_case_2(self):
        # N with a simple single digit sum
        N = 5
        # Sum of digits of 5 is 5
        # Binary of 5 is "101"
        self.assertEqual(solve(N), "101")

    def test_case_3(self):
        # Example case 1: N = 1000, sum = 1
        N = 1000
        # Sum of digits of 1000 is 1+0+0+0 = 1
        # Binary of 1 is "1"
        self.assertEqual(solve(N), "1")

    def test_case_4(self):
        # Example case 2: N = 150, sum = 6
        N = 150
        # Sum of digits of 150 is 1+5+0 = 6
        # Binary of 6 is "110"
        self.assertEqual(solve(N), "110")

    def test_case_5(self):
        # Example case 3: N = 147, sum = 12
        N = 147
        # Sum of digits of 147 is 1+4+7 = 12
        # Binary of 12 is "1100"
        self.assertEqual(solve(N), "1100")

    def test_case_6(self):
        # N resulting in a sum that is a power of 2
        N = 80
        # Sum of digits of 80 is 8+0 = 8
        # Binary of 8 is "1000"
        self.assertEqual(solve(N), "1000")

    def test_case_7(self):
        # N with two digits, leading to a larger sum
        N = 99
        # Sum of digits of 99 is 9+9 = 18
        # Binary of 18 is "10010"
        self.assertEqual(solve(N), "10010")

    def test_case_8(self):
        # N with multiple digits, leading to a moderately complex sum
        N = 345
        # Sum of digits of 345 is 3+4+5 = 12
        # Binary of 12 is "1100"
        self.assertEqual(solve(N), "1100")

    def test_case_9(self):
        # Maximum N allowed, sum is 1
        N = 10000
        # Sum of digits of 10000 is 1+0+0+0+0 = 1
        # Binary of 1 is "1"
        self.assertEqual(solve(N), "1")