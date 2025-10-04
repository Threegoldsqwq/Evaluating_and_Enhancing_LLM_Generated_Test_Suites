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
            # fizz_buzz(79) considers numbers up to 78.
            # It includes the two '7's from 77 (divisible by 11),
            # and one '7' from 78 (divisible by 13).
            # This matches the example in the function's docstring: fizz_buzz(79) returns 3.
            self.assertEqual(fizz_buzz(79), 3)
    def test_n_includes_117(self):
                # Numbers less than 118 divisible by 11 or 13 containing '7':
                # 77 (divisible by 11): contains '7' twice (count = 2)
                # 78 (divisible by 13): contains '7' once (count = 1)
                # 117 (divisible by 13): contains '7' once (count = 1)
                # 91 (divisible by 13) does NOT contain '7'.
                # Total count = 2 + 1 + 1 = 4.
                self.assertEqual(fizz_buzz(118), 4)
    def test_n_includes_176(self):
            # Numbers to consider:
            # 77 (divisible by 11) contains two '7's.
            # 78 (divisible by 13) contains one '7'.
            # 117 (divisible by 13) contains one '7'.
            # 176 (divisible by 11) contains one '7'.
            # Total '7's: 2 + 1 + 1 + 1 = 5.
            self.assertEqual(fizz_buzz(178), 5)
    def test_n_large_with_multiple_sevens(self):
            # Numbers that contribute '7's within the range [1, 279] and are divisible by 11 or 13:
            # 77 (2 '7's, divisible by 11)
            # 78 (1 '7', divisible by 13)
            # 117 (1 '7', divisible by 13)
            # 176 (1 '7', divisible by 11)
            # 247 (1 '7', divisible by 13)
            # 273 (1 '7', divisible by 13)
            # 275 (1 '7', divisible by 11)
            # Total: 2 + 1 + 1 + 1 + 1 + 1 + 1 = 9
            self.assertEqual(fizz_buzz(280), 9)

    def test_n_negative(self):
            # Test with a negative upper bound; the range should be empty, returning 0.
            self.assertEqual(fizz_buzz(-5), 0)

    def test_n_no_multiples(self):
            # Test with n too small to include any multiples of 11 or 13 (e.g., up to 10).
            self.assertEqual(fizz_buzz(10), 0)

    def test_n_multiples_no_sevens_before_70(self):
            # Test with n large enough to include several multiples of 11 or 13,
            # but none contain '7' (e.g., 11, 13, 22, 26, 33, 39, 44, 52, 55, 65, 66).
            self.assertEqual(fizz_buzz(70), 0)

    def test_n_includes_715_divisible_by_11(self):
            # Test n to include 715 (11*65), which contains one '7'.
            # Previous 7s: 77 (2), 78 (1). Total 3.
            # Adding 715 (1). Expected: 3 + 1 = 4.
            self.assertEqual(fizz_buzz(716), 4)

    def test_n_includes_728_divisible_by_13(self):
            # Test n to include 728 (13*56), which contains one '7'.
            # Previous 7s: 77 (2), 78 (1), 715 (1). Total 4.
            # Adding 728 (1). Expected: 4 + 1 = 5.
            self.assertEqual(fizz_buzz(729), 5)

    def test_n_includes_143_divisible_by_both_no_sevens(self):
            # Test n to include 143 (11*13), which is divisible by both but has no '7's.
            # Numbers up to 143: 77 (2), 78 (1). Total 3. 143 itself adds 0.
            self.assertEqual(fizz_buzz(144), 3)

    def test_n_includes_770_multiple_sevens_divisible_by_11(self):
            # Test n to include 770 (11*70), which contains two '7's.
            # Previous 7s: 77 (2), 78 (1), 715 (1), 728 (1). Total 5.
            # Adding 770 (2). Expected: 5 + 2 = 7.
            self.assertEqual(fizz_buzz(771), 7)

    def test_n_excludes_777_not_divisible(self):
            # Test n such that 777 is in the range, but it's not divisible by 11 or 13,
            # so its '7's should not be counted.
            # Expected: Same as fizz_buzz(771) = 7.
            self.assertEqual(fizz_buzz(778), 7)

    def test_n_large_complex_sum(self):
            # Test with a larger 'n' to ensure the loop and cumulative sum work for many iterations.
            # Expected calculation for up to 999:
            # Numbers with '7's divisible by 11 or 13:
            # 77 (2 '7's)
            # 78 (1 '7')
            # 702 (1 '7', 13*54)
            # 704 (1 '7', 11*64)
            # 715 (1 '7', 11*65)
            # 728 (1 '7', 13*56)
            # 737 (1 '7', 11*67)
            # 748 (1 '7', 11*68)
            # 759 (1 '7', 11*69)
            # 767 (1 '7', 13*59)
            # 770 (2 '7's, 11*70)
            # 780 (1 '7', 13*60)
            # 781 (1 '7', 11*71)
            # 792 (1 '7', 11*72)
            # 793 (1 '7', 13*61)
            # 871 (1 '7', 13*67)
            # 975 (1 '7', 13*75)
            # 979 (1 '7', 11*89)
            # Total = 2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 20
            self.assertEqual(fizz_buzz(1000), 20)
