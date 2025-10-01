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