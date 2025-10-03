import unittest

# Assume the function count_palindrome_parity exists and is imported or defined here.
# For the purpose of these tests, we are assuming its signature and behavior.
# def count_palindrome_parity(n: int) -> tuple[int, int]:
#     """
#     Given a positive integer n, return a tuple that has the number of even and odd
#     integer palindromes that fall within the range(1, n), inclusive.
#     """
#     # Placeholder implementation for testing purposes if needed locally,
#     # otherwise assume it's provided by the problem context.
#     even_count = 0
#     odd_count = 0
#
#     def is_palindrome(num):
#         s = str(num)
#         return s == s[::-1]
#
#     for i in range(1, n + 1):
#         if is_palindrome(i):
#             if i % 2 == 0:
#                 even_count += 1
#             else:
#                 odd_count += 1
#     return (even_count, odd_count)


class TestCountPalindromeParity(unittest.TestCase):

    def test_n_equals_1_smallest_input(self):
        """Test with the smallest possible input n=1."""
        self.assertEqual(count_palindrome_parity(1), (0, 1))

    def test_n_equals_2_first_even_palindrome(self):
        """Test when the first even palindrome is included."""
        self.assertEqual(count_palindrome_parity(2), (1, 1))

    def test_n_equals_3_example_1(self):
        """Test with the first example provided (n=3)."""
        self.assertEqual(count_palindrome_parity(3), (1, 2))

    def test_n_equals_9_max_single_digit(self):
        """Test with the largest single-digit number (all single-digit palindromes)."""
        self.assertEqual(count_palindrome_parity(9), (4, 5))

    def test_n_equals_12_example_2(self):
        """Test with the second example provided (n=12)."""
        self.assertEqual(count_palindrome_parity(12), (4, 6))

    def test_n_equals_50_mid_range_two_digit(self):
        """Test with a mid-range two-digit number, includes some 2-digit palindromes."""
        # Palindromes up to 50:
        # 1,2,3,4,5,6,7,8,9 (4 even, 5 odd)
        # 11,22,33,44 (2 even, 2 odd)
        # Total: (4+2=6 even, 5+2=7 odd)
        self.assertEqual(count_palindrome_parity(50), (6, 7))

    def test_n_equals_101_first_three_digit_palindrome(self):
        """Test including the first three-digit palindrome."""
        # Palindromes up to 99: (8 even, 10 odd)
        # Add 101 (odd)
        # Total: (8 even, 10+1=11 odd)
        self.assertEqual(count_palindrome_parity(101), (8, 11))

    def test_n_equals_250_mid_range_three_digit(self):
        """Test with a number that includes several three-digit palindromes."""
        # Up to 99: (8 even, 10 odd)
        # 1xx palindromes (101, 111, ..., 191): 10 odd
        # 2xx palindromes (202, 212, 222, 232, 242): 5 even (252 is > 250)
        # Total even: 8 + 5 = 13
        # Total odd: 10 + 10 = 20
        self.assertEqual(count_palindrome_parity(250), (13, 20))

    def test_n_equals_999_max_three_digit_palindrome(self):
        """Test with the largest three-digit palindrome (includes all 1,2,3 digit palindromes)."""
        # 1-digit: 4 even, 5 odd
        # 2-digit: 4 even, 5 odd
        # 3-digit: 40 even (2xx, 4xx, 6xx, 8xx), 50 odd (1xx, 3xx, 5xx, 7xx, 9xx)
        # Total even: 4 + 4 + 40 = 48
        # Total odd: 5 + 5 + 50 = 60
        self.assertEqual(count_palindrome_parity(999), (48, 60))

    def test_n_equals_1000_max_input(self):
        """Test with the maximum allowed input (1000)."""
        # 1000 is not a palindrome, so counts should be the same as for 999.
        self.assertEqual(count_palindrome_parity(1000), (48, 60))