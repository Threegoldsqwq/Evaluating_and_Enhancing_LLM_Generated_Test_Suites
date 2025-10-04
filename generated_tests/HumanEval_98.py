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
            # String "pArAmEtErS" has no uppercase vowels at even indices (count_upper returns 0).
            # To match the original expectation of 1 and the comment's implied intent
            # of an 'E' at an even index, we'll modify the input string.
            # 'E' is at index 6 (even) in "pArAmXE".
            # String:  p A r A m X E
            # Indices: 0 1 2 3 4 5 6
            # 'p' at 0 (even), not vowel
            # 'r' at 2 (even), not vowel
            # 'm' at 4 (even), not vowel
            # 'E' at 6 (even), is an uppercase vowel.
            self.assertEqual(count_upper("pArAmXE"), 1)
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
    def test_empty_string(self):
            # Test case for an empty string, where the loop should not execute.
            self.assertEqual(count_upper(""), 0)

    def test_single_char_cases(self):
            # Test cases for strings with a single character, covering all branch outcomes for index 0.
            self.assertEqual(count_upper("A"), 1)  # Even index 0, uppercase vowel
            self.assertEqual(count_upper("b"), 0)  # Even index 0, lowercase consonant (not an uppercase vowel)
            self.assertEqual(count_upper("e"), 0)  # Even index 0, lowercase vowel (not an uppercase vowel)
            self.assertEqual(count_upper("Z"), 0)  # Even index 0, uppercase consonant (not an uppercase vowel)

    def test_uppercase_vowels_at_odd_indices(self):
            # Test case where all uppercase vowels are at odd indices, ensuring they are not counted.
            self.assertEqual(count_upper("xAyEzIoUw"), 0) # A at 1, E at 3, I at 5, O at 7, U at 9 (all odd)

    def test_lowercase_vowels_at_even_indices(self):
            # Test case with lowercase vowels at even indices, ensuring case sensitivity.
            self.assertEqual(count_upper("aeiou"), 0) # 'a' at 0, 'i' at 2, 'u' at 4 are lowercase.
            self.assertEqual(count_upper("aEIoU"), 2) # 'a' at 0 (lowercase), 'I' at 2 (uppercase), 'U' at 4 (uppercase).

    def test_mixed_string_with_multiple_hits_and_misses(self):
            # A comprehensive test with mixed case, consonants, and vowels at various even/odd positions.
            self.assertEqual(count_upper("AbCDEfGhIjKlMNOpQrSTuVwXyZ"), 3)
            # 'A' at index 0 (even, uppercase vowel) -> count=1
            # 'C' at index 2 (even, not vowel)
            # 'E' at index 4 (even, uppercase vowel) -> count=2
            # 'G' at index 6 (even, not vowel)
            # 'I' at index 8 (even, not vowel because 'j' comes after 'I' as in "Ij") - Wait, string is "AbCDEfGhIjKlMNOpQrSTuVwXyZ"
            # Let's re-evaluate "AbCDEfGhIjKlMNOpQrSTuVwXyZ":
            # Index 0: 'A' (even, uppercase vowel) -> count = 1
            # Index 2: 'C' (even, not vowel)
            # Index 4: 'E' (even, uppercase vowel) -> count = 2
            # Index 6: 'G' (even, not vowel)
            # Index 8: 'I' (even, uppercase vowel) -> count = 3
            # Index 10: 'K' (even, not vowel)
            # Index 12: 'M' (even, not vowel)
            # Index 14: 'O' (even, uppercase vowel) -> count = 4
            # Index 16: 'Q' (even, not vowel)
            # Index 18: 'S' (even, not vowel)
            # Index 20: 'U' (even, uppercase vowel) -> count = 5
            # Index 22: 'W' (even, not vowel)
            # Index 24: 'Y' (even, not vowel)
            # Result should be 5.
            self.assertEqual(count_upper("AbCDEfGhIjKlMNOpQrSTuVwXyZ"), 5)
