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
        # Assuming the function ignores spaces and case
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_palindrome_with_mixed_case(self):
        # Assuming the function is case-insensitive
        self.assertTrue(is_palindrome("Racecar"))

    def test_palindrome_with_punctuation(self):
        # Assuming the function ignores punctuation and case
        self.assertTrue(is_palindrome("Madam, I'm Adam!"))

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