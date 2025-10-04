import unittest

class TestUniqueDigits(unittest.TestCase):

    def test_example1(self):
        # Example provided in the problem description
        x = [15, 33, 1422, 1]
        expected = [1, 15, 33]
        self.assertEqual(unique_digits(x), expected)

    def test_example2(self):
        # Example provided in the problem description
        x = [152, 323, 1422, 10]
        expected = []
        self.assertEqual(unique_digits(x), expected)

    def test_empty_list(self):
        # Test with an empty input list
        x = []
        expected = []
        self.assertEqual(unique_digits(x), expected)

    def test_all_numbers_valid_and_sorted(self):
        # Test where all numbers are valid and already in sorted order
        x = [1, 3, 5, 11, 13, 19]
        expected = [1, 3, 5, 11, 13, 19]
        self.assertEqual(unique_digits(x), expected)

    def test_all_numbers_invalid(self):
        # Test where all numbers contain at least one even digit
        x = [2, 4, 12, 20, 100, 321]
        expected = []
        self.assertEqual(unique_digits(x), expected)

    def test_single_digit_mix(self):
        # Test with a mix of single-digit odd and even numbers, unsorted
        x = [7, 2, 9, 4, 1, 6, 3, 8]
        expected = [1, 3, 7, 9]
        self.assertEqual(unique_digits(x), expected)

    def test_numbers_containing_zero_digit(self):
        # Test with numbers that contain the digit 0 (which is even)
        x = [101, 305, 15, 3, 179, 90]
        expected = [3, 15, 179]
        self.assertEqual(unique_digits(x), expected)

    def test_mixed_lengths_and_sorting(self):
        # Test with numbers of varying lengths, requiring correct sorting
        x = [135, 1, 3, 15, 179, 24, 5, 113]
        expected = [1, 3, 5, 15, 113, 135, 179]
        self.assertEqual(unique_digits(x), expected)

    def test_duplicates_preserved(self):
        # Test to ensure that duplicate valid numbers are preserved in the output
        x = [1, 15, 33, 1, 1422, 15, 13, 33]
        expected = [1, 1, 13, 15, 15, 33, 33]
        self.assertEqual(unique_digits(x), expected)

    def test_large_numbers_and_complex_mix(self):
        # Test with larger numbers and a more complex mix of valid/invalid
        x = [13579, 24680, 111111, 375, 531, 2, 9, 11]
        expected = [9, 11, 375, 531, 13579, 111111]
        self.assertEqual(unique_digits(x), expected)
    def test_empty_list(self):
            # Covers the scenario where the input list is empty.
            # This ensures the 'for number in x:' loop (line 32) correctly handles no iterations.
            self.assertEqual(self.solution.unique_digits([]), [])

    def test_list_with_zero(self):
            # Addresses uncovered line 21: 'return False' when n == 0 in has_only_odd_digits.
            # Although the problem statement specifies "positive integers",
            # the helper function explicitly handles n=0, and this test covers that path.
            self.assertEqual(self.solution.unique_digits([0]), [])
            # Test with 0 mixed with other numbers
            self.assertEqual(self.solution.unique_digits([1, 0, 3, 2]), [1, 3])

    def test_all_numbers_filtered_out(self):
            # Covers the case where none of the numbers in the input list satisfy the condition.
            # This ensures the 'if has_only_odd_digits(number):' branch is consistently False.
            self.assertEqual(self.solution.unique_digits([2, 4, 6, 12, 20, 24]), [])

    def test_all_numbers_kept_and_sorted(self):
            # Covers the case where all numbers in the input list satisfy the condition.
            # This ensures the 'if has_only_odd_digits(number):' branch is consistently True
            # and verifies the 'result.sort()' functionality with multiple elements.
            self.assertEqual(self.solution.unique_digits([1, 5, 3, 11, 13]), [1, 3, 5, 11, 13])
            # Test with unsorted input to specifically test sorting.
            self.assertEqual(self.solution.unique_digits([13, 5, 1, 11, 3]), [1, 3, 5, 11, 13])

    def test_mixed_numbers_filtering_and_sorting(self):
            # Covers a mixed scenario where some numbers are kept and some are filtered out,
            # verifying both branches of the conditional and the sorting.
            self.assertEqual(self.solution.unique_digits([12, 34, 1, 5, 13, 2, 7]), [1, 5, 7, 13])
            self.assertEqual(self.solution.unique_digits([101, 3, 22, 55, 4]), [3, 55])

    def test_numbers_with_zero_digit(self):
            # Specifically tests numbers containing the digit 0, which is an even digit.
            # This covers the 'if digit % 2 == 0:' branch being true specifically for the digit 0.
            self.assertEqual(self.solution.unique_digits([101, 203, 135]), [135])
            self.assertEqual(self.solution.unique_digits([505, 111, 909]), [111])

    def test_single_digit_numbers(self):
            # Tests the helper function's loop and logic for single-digit numbers.
            self.assertEqual(self.solution.unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 3, 5, 7, 9])

    def test_duplicate_numbers(self):
            # Ensures that duplicate numbers are handled correctly and retained in the result
            # if they meet the odd digits criterion, and sorted appropriately.
            self.assertEqual(self.solution.unique_digits([11, 3, 11, 5, 2, 3]), [3, 3, 5, 11, 11])

    def test_large_numbers(self):
            # Tests the digit extraction logic with larger numbers that have many digits,
            # ensuring the 'while current_num > 0:' loop functions correctly for extended iterations.
            self.assertEqual(self.solution.unique_digits([13579, 24680, 19191]), [13579, 19191])
            self.assertEqual(self.solution.unique_digits([123456789, 97531]), [97531])
