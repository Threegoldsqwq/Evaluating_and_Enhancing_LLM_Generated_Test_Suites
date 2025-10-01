import unittest

# Assume the function 'count_upper' is defined elsewhere, e.g.:
# def count_upper(s: str) -> int:
#     count = 0
#     vowels = "AEIOU"
#     for i, char in enumerate(s):
#         if i % 2 == 0 and char in vowels:
#             count += 1
#     return count

class TestCountUpper(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_upper(""), 0)

    def test_no_uppercase_vowels_at_all(self):
        # Example from problem description
        self.assertEqual(count_upper("abcdefg"), 0)

    def test_uppercase_vowels_only_in_odd_indices(self):
        # I at index 1, U at index 3 (both odd)
        self.assertEqual(count_upper("aIeOu"), 0)

    def test_one_uppercase_vowel_in_even_index(self):
        # Example from problem description (E at index 4)
        self.assertEqual(count_upper("aBCdEf"), 1)

    def test_multiple_uppercase_vowels_in_even_indices(self):
        # A at 0, I at 2, U at 4
        self.assertEqual(count_upper("AEIOU"), 3)

    def test_mixed_case_and_positions(self):
        # E at index 6 (even)
        self.assertEqual(count_upper("pArAmEtErS"), 1)

    def test_all_uppercase_consonants(self):
        self.assertEqual(count_upper("BCDFG"), 0)

    def test_string_with_only_one_char_match(self):
        # A at index 0 (even)
        self.assertEqual(count_upper("A"), 1)

    def test_string_with_only_one_char_no_match(self):
        # B at index 0 (even), but not a vowel
        self.assertEqual(count_upper("B"), 0)

    def test_string_with_example_no_match(self):
        # Example from problem description
        self.assertEqual(count_upper("dBBE"), 0)