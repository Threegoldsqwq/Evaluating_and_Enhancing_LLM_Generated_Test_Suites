import unittest

# Assume the function specialFilter exists and is imported or defined elsewhere.
# For example:
# def specialFilter(arr):
#     count = 0
#     for num in arr:
#         # Condition 1: Number must be greater than 10
#         if num <= 10:
#             continue
        
#         s_num = str(abs(num)) # Use absolute value for digit extraction
        
#         # Condition 2: First digit is odd
#         first_digit = int(s_num[0])
#         if first_digit % 2 == 0:
#             continue
            
#         # Condition 3: Last digit is odd
#         last_digit = int(s_num[-1])
#         if last_digit % 2 == 0:
#             continue
            
#         count += 1
#     return count


class TestSpecialFilter(unittest.TestCase):

    def test_example_1(self):
        # Example from problem description
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)

    def test_example_2(self):
        # Example from problem description
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

    def test_empty_array(self):
        # Test with an empty array
        self.assertEqual(specialFilter([]), 0)

    def test_no_matches_all_less_than_or_equal_to_10(self):
        # All numbers are <= 10, so none should match
        self.assertEqual(specialFilter([1, 2, 3, 10, -5, -100]), 0)

    def test_no_matches_all_greater_than_10_but_fail_digit_conditions(self):
        # Numbers > 10 but fail first or last digit odd condition
        self.assertEqual(specialFilter([12, 21, 45, 100, 246, 888, 1010]), 0)

    def test_all_matching_elements(self):
        # All elements should satisfy all conditions
        self.assertEqual(specialFilter([11, 35, 79, 131, 909, 151]), 6)

    def test_mixed_array_with_various_matches_and_failures(self):
        # A mix of numbers where some match and some don't
        self.assertEqual(specialFilter([11, 13, 20, 35, 40, 57, 100, 101, 120]), 5)
        # Matches: 11, 13, 35, 57, 101

    def test_numbers_with_zero_digits_and_other_failures(self):
            # Test cases involving numbers with '0' digits or other subtle failures
            # Analyzing the input: [101, 123, 205, 307, 411, 513, 1009, 121]
            # 101: >10, first=1 (odd), last=1 (odd) -> Counted
            # 123: >10, first=1 (odd), last=3 (odd) -> Counted
            # 205: >10, first=2 (even), last=5 (odd) -> Not counted (first digit even)
            # 307: >10, first=3 (odd), last=7 (odd) -> Counted
            # 411: >10, first=4 (even), last=1 (odd) -> Not counted (first digit even)
            # 513: >10, first=5 (odd), last=3 (odd) -> Counted
            # 1009: >10, first=1 (odd), last=9 (odd) -> Counted
            # 121: >10, first=1 (odd), last=1 (odd) -> Counted
            # Total counted: 6
            self.assertEqual(specialFilter([101, 123, 205, 307, 411, 513, 1009, 121]), 6)
    def test_large_numbers(self):
        # Test with large numbers
        self.assertEqual(specialFilter([12345, 98765, 1000000000000001, 23456789, 1091, 11111111111111111]), 5)
        # Matches: 12345, 98765, 1000000000000001, 1091, 11111111111111111
        # 23456789 (first digit 2 is even)

    def test_numbers_just_at_or_below_10_boundary_with_odd_digits(self):
            # Test numbers that are <= 10 but have odd first/last digits, ensuring they are not counted
            # Analyze the input: [1, 3, 5, 7, 9, -1, -3, -15, 10, 100, 103, 15]
            # Rules: num > 10 AND first_digit(abs(num)) is odd AND last_digit(abs(num)) is odd
            # 1: Not > 10
            # 3: Not > 10
            # 5: Not > 10
            # 7: Not > 10
            # 9: Not > 10
            # -1: Not > 10
            # -3: Not > 10
            # -15: Not > 10
            # 10: Not > 10
            # 100: num > 10 (True). abs(100) = 100. First digit 1 (odd). Last digit 0 (even). Not counted.
            # 103: num > 10 (True). abs(103) = 103. First digit 1 (odd). Last digit 3 (odd). Counted.
            # 15: num > 10 (True). abs(15) = 15. First digit 1 (odd). Last digit 5 (odd). Counted.
            # Total count should be 2.
            self.assertEqual(specialFilter([1, 3, 5, 7, 9, -1, -3, -15, 10, 100, 103, 15]), 2)
