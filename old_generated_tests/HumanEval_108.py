import unittest

# Assume the 'count_nums' function is defined elsewhere and available for testing.
# For context, a possible implementation that adheres to the problem description
# regarding signed digits for negative numbers could involve a helper function:
#
# def _sum_digits_signed(n):
#     """Calculates the sum of digits with the specified rule for negative numbers."""
#     s = 0
#     if n == 0:
#         return 0
#     elif n > 0:
#         for digit_char in str(n):
#             s += int(digit_char)
#     else: # n < 0
#         str_n = str(n)
#         # The first digit is negative
#         s += int(str_n[1]) * -1
#         # Subsequent digits are positive
#         for digit_char in str_n[2:]:
#             s += int(digit_char)
#     return s
#
# def count_nums(arr):
#     """
#     Counts the number of elements in an array whose sum of digits (with
#     special handling for negative numbers) is greater than 0.
#     """
#     count = 0
#     for num in arr:
#         if _sum_digits_signed(num) > 0:
#             count += 1
#     return count


class TestCountNums(unittest.TestCase):

    def test_all_positive_all_sum_gt_zero(self):
        """Test case with all positive numbers where all sums of digits are greater than 0."""
        # 10 (sum=1>0), 20 (sum=2>0), 30 (sum=3>0)
        self.assertEqual(count_nums([10, 20, 30]), 3)

    def test_all_negative_all_sum_le_zero(self):
        """Test case with all negative numbers where all sums of digits are less than or equal to 0."""
        # -5 (sum=-5<=0), -10 (sum=-1+0=-1<=0), -100 (sum=-1+0+0=-1<=0)
        self.assertEqual(count_nums([-5, -10, -100]), 0)

    def test_mixed_signs_and_sums(self):
        """Test case with a mix of positive, negative numbers, and zero, with varied sum outcomes."""
        # 12 (sum=3>0) -> count
        # -12 (sum=-1+2=1>0) -> count
        # 0 (sum=0)
        # 9 (sum=9>0) -> count
        # -9 (sum=-9<=0)
        self.assertEqual(count_nums([12, -12, 0, 9, -9]), 3)

    def test_numbers_summing_to_zero(self):
        """Test case specifically including numbers whose signed digit sum is exactly zero."""
        # 100 (sum=1>0) -> count
        # -11 (sum=-1+1=0)
        # 23 (sum=5>0) -> count
        # -23 (sum=-2+3=1>0) -> count
        self.assertEqual(count_nums([100, -11, 23, -23]), 3)

    def test_large_positive_numbers(self):
        """Test case with large positive numbers."""
        # 99999 (sum=45>0) -> count
        # 1000000 (sum=1>0) -> count
        self.assertEqual(count_nums([99999, 1000000]), 2)

    def test_large_negative_numbers_mixed_results(self):
        """Test case with large negative numbers, some passing and some failing the sum condition."""
        # -9876 (sum=-9+8+7+6=12>0) -> count
        # -12345 (sum=-1+2+3+4+5=13>0) -> count
        # -100000 (sum=-1+0+0+0+0+0=-1<=0)
        self.assertEqual(count_nums([-9876, -12345, -100000]), 2)

    def test_single_digit_numbers(self):
        """Test case with single-digit numbers, including positive, negative, and zero."""
        # 5 (sum=5>0) -> count
        # -3 (sum=-3<=0)
        # 0 (sum=0)
        # 7 (sum=7>0) -> count
        self.assertEqual(count_nums([5, -3, 0, 7]), 2)

    def test_all_elements_sum_gt_zero_mixed_signs(self):
        """Test case where all elements should result in a sum of digits greater than 0, with mixed signs."""
        # 1 (sum=1>0) -> count
        # -123 (sum=-1+2+3=4>0) -> count
        # 4 (sum=4>0) -> count
        # -987 (sum=-9+8+7=6>0) -> count
        # 5 (sum=5>0) -> count
        self.assertEqual(count_nums([1, -123, 4, -987, 5]), 5)

    def test_all_elements_sum_le_zero_mixed_signs(self):
        """Test case where all elements should result in a sum of digits less than or equal to 0, with mixed signs."""
        # -1 (sum=-1<=0)
        # 0 (sum=0)
        # -50 (sum=-5+0=-5<=0)
        # -9 (sum=-9<=0)
        self.assertEqual(count_nums([-1, 0, -50, -9]), 0)

    def test_numbers_with_many_zeros(self):
        """Test case for numbers containing multiple zeros, both positive and negative."""
        # 1000 (sum=1+0+0+0=1>0) -> count
        # -1000 (sum=-1+0+0+0=-1<=0)
        # 200 (sum=2+0+0=2>0) -> count
        # -200 (sum=-2+0+0=-2<=0)
        self.assertEqual(count_nums([1000, -1000, 200, -200]), 2)