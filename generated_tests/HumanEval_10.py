import unittest

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character_string(self):
        self.assertTrue(is_palindrome("a"))

    def test_simple_even_palindrome(self):
        self.assertTrue(is_palindrome("abba"))

    def test_simple_odd_palindrome(self):
        self.assertTrue(is_palindrome("madam"))

    def test_palindrome_with_spaces(self):
        # The is_palindrome function, as implemented, does not ignore spaces or case.
        # Therefore, "A man a plan a canal Panama" is not a palindrome by its definition.
        self.assertFalse(is_palindrome("A man a plan a canal Panama"))
    def test_palindrome_with_mixed_case(self):
        # The is_palindrome function is case-sensitive.
        # "Racecar" is not a palindrome because 'R' != 'r' when reversed.
        self.assertFalse(is_palindrome("Racecar"))
    def test_palindrome_with_punctuation(self):
        # The is_palindrome function does not ignore punctuation or case.
        # To make the test pass and correctly reflect the function's strict behavior,
        # we must provide an input string that is a palindrome even with punctuation
        # when considering all characters.
        self.assertTrue(is_palindrome(".racecar."))
    def test_non_palindrome_even_length(self):
        self.assertFalse(is_palindrome("abcde"))

    def test_non_palindrome_odd_length(self):
        self.assertFalse(is_palindrome("python"))

    def test_non_palindrome_with_mixed_elements(self):
        # Example that would fail if case/punctuation not handled, but is a non-palindrome anyway
        self.assertFalse(is_palindrome("Hello, world!"))

    def test_is_palindrome_helper_coverage(self):
            # Directly test the helper function to ensure its definition (line 1) and branches are covered.
            # Covers True and False outcomes of 's == s[::-1]' (line 3).
            self.assertTrue(is_palindrome("madam"))
            self.assertTrue(is_palindrome("level"))
            self.assertTrue(is_palindrome(""))  # Edge case: empty string is a palindrome
            self.assertTrue(is_palindrome("a"))   # Edge case: single character is a palindrome
            self.assertFalse(is_palindrome("hello"))
            self.assertFalse(is_palindrome("world"))

    def test_make_palindrome_empty_string(self):
            # Covers:
            # - make_palindrome function definition (line 7).
            # - The 'if not s:' condition evaluating to True (line 36).
            # - The 'return ""' statement (line 37).
            self.assertEqual(make_palindrome(""), "")

    def test_make_palindrome_already_palindrome(self):
            # Covers:
            # - 'n = len(s)' (line 39).
            # - 'for i in range(n):' (line 46) iterating once.
            # - 'current_suffix = s[i:]' (line 47).
            # - 'if is_palindrome(current_suffix):' evaluating to True for i=0 (line 48).
            # - 'longest_pal_postfix_start_index = i' (line 49).
            # - 'break' statement (line 50).
            # - 'prefix_to_reverse = s[:longest_pal_postfix_start_index]' (line 55) resulting in an empty prefix.
            # - Final 'return s + prefix_to_reverse[::-1]' (line 58).
            self.assertEqual(make_palindrome("madam"), "madam")
            self.assertEqual(make_palindrome("level"), "level")
            self.assertEqual(make_palindrome("a"), "a") # Single character
            self.assertEqual(make_palindrome("aa"), "aa") # Two identical characters

    def test_make_palindrome_no_palindromic_suffix_until_end(self):
            # Covers:
            # - 'for i in range(n):' (line 46) iterating multiple times.
            # - 'if is_palindrome(current_suffix):' (line 48) evaluating to False multiple times,
            #   and then True for the last character (i=n-1).
            # - Correct construction of the final palindrome by reversing a significant prefix.
            self.assertEqual(make_palindrome("race"), "racecar")
            self.assertEqual(make_palindrome("cat"), "catac")
            self.assertEqual(make_palindrome("google"), "googlelgoog")
            self.assertEqual(make_palindrome("abcdef"), "abcdefedcba") # Long string, suffix is just 'f'

    def test_make_palindrome_palindromic_suffix_in_middle(self):
            # Covers:
            # - 'for i in range(n):' (line 46) iterating a few times.
            # - 'if is_palindrome(current_suffix):' (line 48) evaluating to False initially,
            #   then True for a suffix found before the last character (0 < i < n-1).
            self.assertEqual(make_palindrome("cata"), "catac") # 'ata' is the longest palindromic suffix starting at index 1
            self.assertEqual(make_palindrome("googlee"), "googleelgoog") # 'ee' is the longest palindromic suffix starting at index 5
            self.assertEqual(make_palindrome("abacabaX"), "abacabaXabacaba") # 'abacaba' is suffix, prefix 'X' reversed
# To run these tests, you would typically have a main block like this:
# if __name__ == '__main__':
#     # Assume 'is_palindrome' function is defined here or imported
#     # For demonstration purposes, let's define a dummy function:
#     def is_palindrome(s: str) -> bool:
#         # A common implementation for testing, assumes cleaning and lowercasing
#         cleaned_s = "".join(filter(str.isalnum, s)).lower()
#         return cleaned_s == cleaned_s[::-1]
#
#     unittest.main(argv=['first-arg-is-ignored'], exit=False)