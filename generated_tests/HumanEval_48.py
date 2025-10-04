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

    def test_is_palindrome_single_character(self):
            self.assertTrue(is_palindrome('a'))
            self.assertTrue(is_palindrome('Z'))

    def test_is_palindrome_even_length_true(self):
            self.assertTrue(is_palindrome('abba'))
            self.assertTrue(is_palindrome('noon'))

    def test_is_palindrome_even_length_false(self):
            self.assertFalse(is_palindrome('abca'))
            self.assertFalse(is_palindrome('book'))

    def test_is_palindrome_case_sensitivity(self):
            # 'Racecar' is not a palindrome because 'Racecar' != 'racecaR'
            self.assertFalse(is_palindrome('Racecar'))
            self.assertFalse(is_palindrome('Madam'))
            self.assertTrue(is_palindrome('AaA')) # This is a palindrome

    def test_is_palindrome_with_spaces(self):
            # Spaces are treated as regular characters
            self.assertTrue(is_palindrome('a b a'))
            self.assertFalse(is_palindrome('race car')) # 'race car' != 'rac ecar'
            self.assertFalse(is_palindrome('test tset')) # leading/trailing spaces would make it not a palindrome

    def test_is_palindrome_with_numbers(self):
            self.assertTrue(is_palindrome('121'))
            self.assertFalse(is_palindrome('123'))
            self.assertTrue(is_palindrome('12321'))

    def test_is_palindrome_with_special_characters(self):
            self.assertTrue(is_palindrome('!@!'))
            self.assertFalse(is_palindrome('!@#'))
            self.assertTrue(is_palindrome('$_$'))
# To run these tests, you would typically have the is_palindrome function defined:
# def is_palindrome(s):
#     return s == s[::-1]

# if __name__ == '__main__':
#     unittest.main(argv=['first-arg-is-ignored'], exit=False)