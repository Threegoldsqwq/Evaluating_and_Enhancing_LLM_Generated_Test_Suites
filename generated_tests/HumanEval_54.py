import unittest

# Assume the function same_chars exists and is imported or defined elsewhere.
# For example:
# def same_chars(word1, word2):
#     return set(word1) == set(word2)

class TestSameChars(unittest.TestCase):

    def test_example_case_1_true(self):
        # Original example: complex true case with many repeated characters
        self.assertTrue(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))

    def test_example_case_2_true(self):
        # Original example: simpler true case with repeated characters
        self.assertTrue(same_chars('abcd', 'dddddddabc'))

    def test_example_case_3_true_symmetric(self):
        # Original example's symmetric version for thoroughness
        self.assertTrue(same_chars('dddddddabc', 'abcd'))

    def test_example_case_4_false_missing_char_in_second(self):
        # Original example: false case where second word lacks a character from the first
        self.assertFalse(same_chars('eabcd', 'dddddddabc'))

    def test_example_case_5_false_extra_char_in_second(self):
        # Original example: false case where second word has an extra character
        self.assertFalse(same_chars('abcd', 'dddddddabce'))

    def test_empty_strings(self):
        # Edge case: both strings are empty
        self.assertTrue(same_chars('', ''))

    def test_one_empty_string(self):
        # Edge case: one string is empty, the other is not
        self.assertFalse(same_chars('a', ''))

    def test_simple_anagram_like_true(self):
        # Test with words that are like anagrams, but character counts don't matter
        self.assertTrue(same_chars('listen', 'silent'))

    def test_different_unique_characters_false(self):
        # Test with words having completely different sets of unique characters
        self.assertFalse(same_chars('hello', 'world'))

    def test_repeated_chars_and_order_true(self):
        # Test with varying counts and order, but same unique character set
        self.assertTrue(same_chars('programming', 'gamingroprm'))
    def test_unicode_characters(self):
            # Test with unicode characters
            self.assertTrue(same_chars('你好世界', '世界你好'))
            self.assertFalse(same_chars('你好世界', '你好'))
            self.assertFalse(same_chars('你好', '你好世界'))
            self.assertTrue(same_chars('áéíóú', 'úóíéá'))
            self.assertFalse(same_chars('áéíóú', 'aeiou')) # Different characters entirely

    def test_numbers_and_symbols(self):
            # Test with numbers and symbols
            self.assertTrue(same_chars('123!@#', '#@!321'))
            self.assertFalse(same_chars('123!@#', '123'))
            self.assertFalse(same_chars('123', '123!@#'))
            self.assertTrue(same_chars('.,;:', ':;.,')) # Only symbols, same set
            self.assertFalse(same_chars('.,;:', ':;,.!')) # Different sets due to '!'

    def test_strings_with_spaces(self):
            # Test with spaces as characters
            self.assertTrue(same_chars('a b c', ' c b a'))
            self.assertFalse(same_chars('abc', 'a b c')) # 'abc' does not have a space, 'a b c' does
            self.assertTrue(same_chars('Hello World', 'Hello  World')) # Multiple spaces collapse to one ' ' in set
            self.assertFalse(same_chars('test', '   test   ')) # 'test' lacks the space character that '   test   ' contains

    def test_long_strings_with_repetitions(self):
            # Test with very long strings and many repetitions to ensure robustness
            long_word1 = 'a' * 1000 + 'b' * 500 + 'c' * 200
            long_word2 = 'c' * 150 + 'b' * 700 + 'a' * 800
            self.assertTrue(same_chars(long_word1, long_word2))

            long_word3 = 'a' * 1000 + 'b' * 500
            long_word4 = 'a' * 800 + 'b' * 700 + 'd' * 100 # 'd' is an extra unique character
            self.assertFalse(same_chars(long_word3, long_word4))

    def test_single_unique_character_strings(self):
            # Test strings with a single unique character and variations
            self.assertTrue(same_chars('aaaaa', 'a'))
            self.assertTrue(same_chars('b', 'bbbbbb'))
            self.assertFalse(same_chars('a', 'b')) # Disjoint single characters
            self.assertFalse(same_chars('aaaaa', 'ab')) # 'b' is extra unique character

    def test_disjoint_character_sets(self):
            # Test cases where character sets are entirely different (no common characters)
            self.assertFalse(same_chars('abc', 'xyz'))
            self.assertFalse(same_chars('123', '456'))
            self.assertFalse(same_chars('!', '@'))

    def test_case_sensitivity_variants(self):
            # Test more variations of case sensitivity beyond the docstring example
            self.assertFalse(same_chars('aBcD', 'dCbA')) # Sets {'a', 'B', 'c', 'D'} and {'d', 'C', 'b', 'A'} are different
            self.assertFalse(same_chars('aBcD', 'abcd')) # Lowercase vs mixed case
            self.assertTrue(same_chars('Python', 'nohyPt')) # Same characters, same case, different order/frequency
