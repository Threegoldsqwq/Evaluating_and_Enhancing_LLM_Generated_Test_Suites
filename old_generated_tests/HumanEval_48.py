import unittest

class TestIsPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))

    def test_basic_odd_palindrome(self):
        self.assertTrue(is_palindrome('aba'))

    def test_basic_even_palindrome(self):
        self.assertTrue(is_palindrome('abba'))

    def test_basic_odd_non_palindrome(self):
        self.assertFalse(is_palindrome('abc'))

    def test_basic_even_non_palindrome(self):
        self.assertFalse(is_palindrome('abca'))

    def test_longer_palindrome(self):
        self.assertTrue(is_palindrome('madam'))

    def test_longer_non_palindrome(self):
        self.assertFalse(is_palindrome('python'))

    def test_palindrome_with_repeated_characters(self):
        self.assertTrue(is_palindrome('aaaaa'))

    def test_non_palindrome_with_some_repeated_characters(self):
        self.assertFalse(is_palindrome('abacabaa'))

# To run these tests, you would typically have the is_palindrome function defined:
# def is_palindrome(s):
#     return s == s[::-1]

# if __name__ == '__main__':
#     unittest.main(argv=['first-arg-is-ignored'], exit=False)