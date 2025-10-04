import unittest

# Assume the circular_shift function is defined elsewhere, for example:
# def circular_shift(x: int, shift: int) -> str:
#     s = str(x)
#     n = len(s)
#     if n == 0:
#         return ""
#
#     if shift > n:
#         return s[::-1]
#     else:
#         # Normalize shift for actual rotation (optional, but good practice if shift could be very large)
#         # For the problem, we just need to ensure shift is not > n for this path.
#         actual_shift = shift % n
#         if actual_shift == 0: # A shift of 0 or a multiple of n results in no change
#             return s
#         return s[-actual_shift:] + s[:-actual_shift]


class TestCircularShift(unittest.TestCase):

    def test_basic_single_shift(self):
        # Basic case: single right shift
        self.assertEqual(circular_shift(123, 1), "312")

    def test_shift_equal_to_num_digits(self):
        # Shift by number of digits should result in the original number
        self.assertEqual(circular_shift(123, 3), "123")

    def test_shift_by_zero(self):
        # Shift by zero should return the original number as a string
        self.assertEqual(circular_shift(456, 0), "456")

    def test_shift_greater_than_num_digits(self):
        # Special rule: If shift > number of digits, return digits reversed
        self.assertEqual(circular_shift(123, 4), "321")

    def test_single_digit_number_shift_zero(self):
        # Single digit number, no shift
        self.assertEqual(circular_shift(5, 0), "5")

    def test_single_digit_number_shift_one(self):
        # Single digit number, shift by its length (1)
        self.assertEqual(circular_shift(5, 1), "5")

    def test_single_digit_number_shift_greater_than_one(self):
        # Single digit number, shift > number of digits (1). Should be reversed.
        # Reversed single digit is itself.
        self.assertEqual(circular_shift(5, 2), "5")

    def test_number_with_zeros_single_shift(self):
        # Test with numbers containing zeros and a single shift
        self.assertEqual(circular_shift(102, 1), "210")

    def test_number_with_zeros_shift_greater_than_num_digits(self):
        # Test with numbers containing zeros and shift > number of digits
        self.assertEqual(circular_shift(102, 4), "201")

    def test_longer_number_multiple_shifts(self):
        # Test a longer number with a shift less than its length
        self.assertEqual(circular_shift(12345, 2), "45123")