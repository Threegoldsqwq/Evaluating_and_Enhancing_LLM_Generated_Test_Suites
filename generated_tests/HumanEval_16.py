import unittest

# Assume the function count_distinct_characters exists elsewhere, e.g.:
# def count_distinct_characters(s: str) -> int:
#     seen_chars = set()
#     for char in s:
#         if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
#             seen_chars.add(char.lower())
#         else:
#             seen_chars.add(char)
#     return len(seen_chars)


class TestCountDistinctCharacters(unittest.TestCase):

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertEqual(count_distinct_characters(''), 0)

    def test_single_lowercase_character(self):
        """Test with a single lowercase character."""
        self.assertEqual(count_distinct_characters('a'), 1)

    def test_single_uppercase_character(self):
        """Test with a single uppercase character."""
        self.assertEqual(count_distinct_characters('Z'), 1)

    def test_all_same_character_mixed_case(self):
        """Test with a string containing the same character in mixed cases."""
        # 'a', 'A', 'a', 'A' should all be counted as one distinct character 'a'
        self.assertEqual(count_distinct_characters('AaAaA'), 1)

    def test_all_distinct_lowercase_characters(self):
        """Test with a string of distinct lowercase characters."""
        self.assertEqual(count_distinct_characters('abcdefg'), 7)

    def test_all_distinct_mixed_case_characters(self):
        """Test with a string of distinct characters in mixed cases."""
        # 'A', 'b', 'C', 'd', 'E', 'f', 'G' should be counted as 7 distinct characters (a, b, c, d, e, f, g)
        self.assertEqual(count_distinct_characters('AbCdEfG'), 7)

    def test_string_with_repeated_characters_mixed_case(self):
        """Test with a string containing repeated characters and mixed cases."""
        # 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g' -> distinct are {p, r, o, g, a, m, i, n} -> 8
        self.assertEqual(count_distinct_characters('Programming'), 8)

    def test_string_with_numbers_only(self):
        """Test with a string containing only numbers."""
        # Numbers are distinct characters and do not have case.
        self.assertEqual(count_distinct_characters('12345'), 5)

    def test_string_with_symbols_only(self):
        """Test with a string containing only symbols."""
        # Symbols are distinct characters and do not have case.
        self.assertEqual(count_distinct_characters('!@#$%^'), 6)

    def test_string_with_mixed_alphanumeric_symbols_and_repetitions(self):
        """Test with a complex string containing mixed character types and repetitions."""
        # Input: 'HelLo W0rLd!123'
        # Distinct characters (case-insensitive for letters):
        # h, e, l, o (from 'HelLo')
        #   (space)
        # w (from 'W')
        # 0 (from '0')
        # r, d (from 'rLd')
        # ! (from '!')
        # 1, 2, 3 (from '123')
        # Total distinct: {h, e, l, o, ' ', w, 0, r, d, !, 1, 2, 3} -> 13
        self.assertEqual(count_distinct_characters('HelLo W0rLd!123'), 13)
    def test_empty_string(self):
            # Test case for an empty string, ensuring 0 distinct characters.
            self.assertEqual(count_distinct_characters(''), 0)

    def test_all_lowercase_unique(self):
            # Test case with all unique lowercase characters.
            self.assertEqual(count_distinct_characters('abcdefgh'), 8)

    def test_all_uppercase_unique(self):
            # Test case with all unique uppercase characters.
            self.assertEqual(count_distinct_characters('ABCDEFGH'), 8)

    def test_all_same_character_lowercase(self):
            # Test case with all identical characters (lowercase).
            self.assertEqual(count_distinct_characters('aaaaa'), 1)

    def test_all_same_character_uppercase(self):
            # Test case with all identical characters (uppercase).
            self.assertEqual(count_distinct_characters('AAAAA'), 1)

    def test_mixed_case_same_character(self):
            # Test case with characters that are the same when case is ignored.
            self.assertEqual(count_distinct_characters('aAaAaA'), 1)

    def test_string_with_numbers(self):
            # Test case including numeric characters.
            self.assertEqual(count_distinct_characters('12345'), 5)
            self.assertEqual(count_distinct_characters('111223'), 3) # 1, 2, 3

    def test_string_with_symbols(self):
            # Test case including special characters/symbols.
            self.assertEqual(count_distinct_characters('!@#$%^'), 6)
            self.assertEqual(count_distinct_characters('!@#!@#'), 3) # !, @, #

    def test_string_with_spaces(self):
            # Test case including space characters.
            self.assertEqual(count_distinct_characters('   '), 1) # Only ' ' is distinct
            self.assertEqual(count_distinct_characters('hello world'), 8) # h, e, l, o, ' ', w, r, d

    def test_complex_string_mixed_chars(self):
            # Test case with a mix of alphabetic, numeric, symbol, and space characters.
            self.assertEqual(count_distinct_characters('PyThon 3.9!'), 10) # p, y, t, h, o, n, ' ', 3, ., 9, !

    def test_unicode_characters(self):
            # Test case including Unicode characters.
            self.assertEqual(count_distinct_characters('résumé'), 5) # r, é, s, u, m
            self.assertEqual(count_distinct_characters('你好世界'), 4) # All unique
            self.assertEqual(count_distinct_characters('café CAFÉ'), 5) # c, a, f, é, ' '
