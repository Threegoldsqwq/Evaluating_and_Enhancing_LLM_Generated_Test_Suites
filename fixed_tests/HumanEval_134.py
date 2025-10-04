import unittest

# Assume the function check_if_last_char_is_a_letter exists as described:
# def check_if_last_char_is_a_letter(s: str) -> bool:
#     """
#     Returns True if the last character of a given string is an alphabetical character
#     and is not a part of a word, and False otherwise.
#     Note: "word" is a group of characters separated by space.
#     """
#     # Based on the examples, "not a part of a word" seems to mean
#     # the last character is a standalone letter, either because it's the only character
#     # or it's preceded by a space.
#     if not s:
#         return False
#     if not s[-1].isalpha():
#         return False
#     # At this point, s is not empty and s[-1] is an alphabet.
#     if len(s) == 1:
#         return True # e.g., "a"
#     if s[-2] == ' ':
#         return True # e.g., "apple pi e", " ab"
#     return False


class TestCheckIfLastCharIsALetter(unittest.TestCase):

    def test_01_example_apple_pie(self):
        # Last char 'e' is alpha, but part of the word "pie".
        self.assertFalse(check_if_last_char_is_a_letter("apple pie"))

    def test_02_example_apple_pi_e(self):
        # Last char 'e' is alpha and preceded by a space, considered "not part of a word".
        self.assertTrue(check_if_last_char_is_a_letter("apple pi e"))

    def test_03_example_apple_pi_e_with_trailing_space(self):
        # Last char is a space, not alphabetical.
        self.assertFalse(check_if_last_char_is_a_letter("apple pi e "))

    def test_04_example_empty_string(self):
        # Empty string case.
        self.assertFalse(check_if_last_char_is_a_letter(""))

    def test_05_single_alphabet_char(self):
        # Single character string, which is alphabetical.
        self.assertTrue(check_if_last_char_is_a_letter("a"))

    def test_06_single_non_alphabet_char(self):
        # Single character string, not alphabetical.
        self.assertFalse(check_if_last_char_is_a_letter("1"))

    def test_07_word_ending_with_alpha_no_preceding_space(self):
        # Last char 'o' is alpha, but part of the word "hello".
        self.assertFalse(check_if_last_char_is_a_letter("hello"))

    def test_08_multiple_words_ending_with_isolated_alpha(self):
        # Last char 'z' is alpha and preceded by a space.
        self.assertTrue(check_if_last_char_is_a_letter("hello world z"))

    def test_09_string_starting_with_space_ending_with_isolated_alpha(self):
            # String starts with a space, last char 'b' is alpha and preceded by a space.
            # The original input " ab" has 'b' preceded by 'a', not a space.
            # Changing the input to " a b" makes 'b' preceded by a space, matching the test description.
            self.assertTrue(check_if_last_char_is_a_letter(" a b"))
    def test_10_last_char_is_punctuation(self):
        # Last char '!' is not alphabetical.
        self.assertFalse(check_if_last_char_is_a_letter("end!"))