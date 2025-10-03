import unittest

# Assume the function delete_and_check_palindrome exists and is imported or defined elsewhere.
# For the purpose of these tests, we are assuming its signature:
# def delete_and_check_palindrome(s: str, c: str) -> tuple[str, bool]:
#     """
#     Deletes all characters in s that are present in c, then checks if the
#     resulting string is a palindrome.
#     Returns a tuple (result_string, is_palindrome).
#     """
#     # Example implementation (not part of the required output, just for context)
#     chars_to_delete = set(c)
#     result_s = "".join(char for char in s if char not in chars_to_delete)
#
#     is_palindrome = result_s == result_s[::-1]
#
#     return (result_s, is_palindrome)


class TestDeleteAndCheckPalindrome(unittest.TestCase):

    def test_example_1_basic_non_palindrome(self):
        """Test case from the problem description: basic deletion, non-palindrome result."""
        s = "abcde"
        c = "ae"
        expected = ('bcd', False)
        self.assertEqual(delete_and_check_palindrome(s, c), expected)

    def test_example_2_basic_non_palindrome_different_chars(self):
        """Test case from the problem description: different character deletion, non-palindrome."""
        s = "abcdef"
        c = "b"
        expected = ('acdef', False)
        self.assertEqual(delete_and_check_palindrome(s, c), expected)

    def test_example_3_basic_palindrome_result(self):
        """Test case from the problem description: basic deletion, palindrome result."""
        s = "abcdedcba"
        c = "ab"
        expected = ('cdedc', True)
        self.assertEqual(delete_and_check_palindrome(s, c), expected)

    def test_c_is_empty_s_is_palindrome(self):
        """Test case where no characters are deleted, and original string is a palindrome."""
        s = "madam"
        c = ""
        expected = ('madam', True)
        self.assertEqual(delete_and_check_palindrome(s, c), expected)

    def test_s_becomes_empty_string(self):
        """Test case where all characters of s are deleted, resulting in an empty string (which is a palindrome)."""
        s = "test"
        c = "tse"  # 't', 'e', 's' will remove all characters from "test"
        expected = ('', True)
        self.assertEqual(delete_and_check_palindrome(s, c), expected)

    def test_s_becomes_single_character_palindrome(self):
        """Test case where s is reduced to a single character (always a palindrome)."""
        s = "level"
        c = "lev"  # 'l', 'e', 'v' will remove 'l's and 'v' from "level", leaving 'e'
        expected = ('e', True)
        self.assertEqual(delete_and_check_palindrome(s, c), expected)

    def test_s_becomes_palindrome_from_non_palindrome(self):
        """Test case where s is initially not a palindrome, but becomes one after deletion."""
        s = "abca"  # "abca" is not a palindrome
        c = "b"     # Removing 'b' results in "aca"
        expected = ('aca', True)
        self.assertEqual(delete_and_check_palindrome(s, c), expected)

    def test_c_has_chars_not_in_s_no_change(self):
        """Test case where c contains characters not present in s, so s remains unchanged."""
        s = "world"
        c = "xyz"  # 'x', 'y', 'z' are not in "world"
        expected = ('world', False)
        self.assertEqual(delete_and_check_palindrome(s, c), expected)

    def test_s_already_palindrome_remains_palindrome_after_some_deletion(self):
        """Test case where s is already a palindrome, and remains one after some deletions."""
        s = "racecar"
        c = "r"  # Removing 'r's results in "aceca"
        expected = ('aceca', True)
        self.assertEqual(delete_and_check_palindrome(s, c), expected)

    def test_mixed_case_and_spaces_case_sensitive_deletion(self):
        """Test case with mixed case, spaces, and verifies case-sensitive deletion."""
        s = "Hello World"
        c = "lHo"  # Will remove 'l', 'H', 'o' (case-sensitive)
        # H e l l o   W o r l d
        # _ e _ _ _   W _ r _ d
        # Result: "e Wrd"
        expected = ('e Wrd', False)
        self.assertEqual(delete_and_check_palindrome(s, c), expected)