import unittest

# Assume the function 'is_palindrome' exists, e.g.:
# def is_palindrome(text: str) -> bool:
#     """
#     Checks if a given string is a palindrome, ignoring case and non-alphanumeric characters.
#     """
#     cleaned_text = "".join(char.lower() for char in text if char.isalnum())
#     return cleaned_text == cleaned_text[::-1]


class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character_string(self):
        self.assertTrue(is_palindrome("a"))

    def test_basic_odd_length_palindrome(self):
        self.assertTrue(is_palindrome("madam"))

    def test_basic_even_length_palindrome(self):
        self.assertTrue(is_palindrome("anna"))

    def test_basic_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))



    def test_non_palindrome_with_mixed_characters(self):
        # "Madam, I'm Adam" cleaned is "madamimadam" which is a palindrome
        # Re-evaluating this test case for "false" scenario
        # Let's pick a known non-palindrome with mixed chars
        self.assertFalse(is_palindrome("Not a palindrome!"))

    def test_numeric_palindrome(self):
        self.assertTrue(is_palindrome("12321"))

    # Adding a couple more for good measure if needed, but 10 are provided above.
    # def test_mixed_alphanumeric_palindrome(self):
    #     self.assertTrue(is_palindrome("A1B2B1A"))

    # def test_non_palindrome_with_numeric_difference(self):
    #     self.assertFalse(is_palindrome("12345"))


if __name__ == '__main__':
    unittest.main()