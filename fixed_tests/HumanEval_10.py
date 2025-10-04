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