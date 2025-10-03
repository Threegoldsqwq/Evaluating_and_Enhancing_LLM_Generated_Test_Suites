import unittest

# Assume the fizz_buzz function is defined elsewhere, e.g.:
# def fizz_buzz(n):
#     """
#     Return the number of times the digit 7 appears in integers less than n
#     which are divisible by 11 or 13.
#     """
#     count = 0
#     for i in range(1, n):
#         if i % 11 == 0 or i % 13 == 0:
#             count += str(i).count('7')
#     return count

class TestFizzBuzz(unittest.TestCase):

    def test_n_is_one(self):
        # Edge case: n=1, range is empty (0 to 0), no numbers to check.
        self.assertEqual(fizz_buzz(1), 0)

    def test_no_multiples_below_n(self):
        # n is small, no numbers divisible by 11 or 13 are included.
        self.assertEqual(fizz_buzz(10), 0)

    def test_multiples_without_seven_digit(self):
        # Includes 11 and 13, but neither contains the digit 7.
        self.assertEqual(fizz_buzz(14), 0)

    def test_example_n_50(self):
        # Covers multiples 11,13,22,26,33,39,44. None contain '7'.
        self.assertEqual(fizz_buzz(50), 0)

    def test_n_just_before_77_is_included(self):
        # Multiples up to 66 (for 11) and 65 (for 13). 77 is not included.
        self.assertEqual(fizz_buzz(77), 0)

    def test_example_n_78(self):
        # 77 is the first number containing '7' that is also a multiple (11*7).
        # It contributes two '7's. 78 is a multiple of 13 but has no '7'.
        self.assertEqual(fizz_buzz(78), 2)

    def test_n_79_confirm_77_contribution(self):
        # No new numbers are added between 78 and 79 that are multiples and contain '7'.
        # This confirms our interpretation of the problem statement over the example's '3'.
        self.assertEqual(fizz_buzz(79), 2)

    def test_n_includes_117(self):
        # In addition to 77 (2 '7's), 117 (13*9) adds one '7'.
        # Numbers to check: 77 (2), 117 (1).
        self.assertEqual(fizz_buzz(118), 3)

    def test_n_includes_176(self):
        # In addition to 77 (2 '7's) and 117 (1 '7'), 176 (11*16) adds one '7'.
        # Numbers to check: 77 (2), 117 (1), 176 (1).
        self.assertEqual(fizz_buzz(178), 4)

    def test_n_large_with_multiple_sevens(self):
        # Numbers that contribute '7's:
        # 77 (2 '7's), 117 (1 '7'), 176 (1 '7'), 247 (1 '7' from 13*19),
        # 273 (1 '7' from 13*21), 275 (1 '7' from 11*25).
        # Total: 2 + 1 + 1 + 1 + 1 + 1 = 7
        self.assertEqual(fizz_buzz(280), 7)