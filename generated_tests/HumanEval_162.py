import unittest
import hashlib

# Assume the function 'string_to_md5' is defined elsewhere.
# For reference, here's a possible implementation (NOT part of the required output):
# def string_to_md5(text: str) -> str | None:
#     if not text:
#         return None
#     return hashlib.md5(text.encode('utf-8')).hexdigest()

class TestStringToMD5(unittest.TestCase):

    def test_empty_string(self):
        """Test with an empty string, should return None."""
        self.assertIsNone(string_to_md5(""))

    def test_example_string(self):
        """Test the example string provided in the problem description."""
        self.assertEqual(string_to_md5("Hello world"), "3e25960a79dbc69b674cd4ec67a72c62")

    def test_simple_lowercase_string(self):
        """Test with a simple lowercase string."""
        self.assertEqual(string_to_md5("test"), "098f6bcd4621d373cade4e832627b4f6")

    def test_uppercase_string(self):
        """Test with an uppercase string."""
        self.assertEqual(string_to_md5("PYTHON"), "1ffcc91409951675a29d8a356a84d209")

    def test_string_with_numbers(self):
        """Test with a string containing only numbers."""
        self.assertEqual(string_to_md5("1234567890"), "d174ab98d277d9f5a051fd6027ac5ba0")

    def test_string_with_special_characters(self):
        """Test with a string containing special characters."""
        self.assertEqual(string_to_md5("!@#$%^&*()"), "0c6cf7a19237ec9b578c7921a415ff5e")

    def test_long_string(self):
        """Test with a relatively long string."""
        long_text = "This is a much longer string that should still produce a valid MD5 hash. It contains various characters and spaces to ensure the hashing algorithm works correctly with diverse inputs."
        self.assertEqual(string_to_md5(long_text), "24a18018d963554b73b53c7a6595d2c0")

    def test_string_with_leading_trailing_spaces(self):
        """Test a string with leading and trailing spaces."""
        self.assertEqual(string_to_md5("  padded string  "), "aa9e001851e5e01b38f8319f6368d9f4")

    def test_unicode_string(self):
        """Test with a Unicode string (non-ASCII characters)."""
        self.assertEqual(string_to_md5("你好世界"), "b80e8e04058d84400e28f20b36873b13")

    def test_string_with_newline_and_tab(self):
        """Test with a string containing newline and tab characters."""
        self.assertEqual(string_to_md5("line1\n\tline2"), "94b9f33333065b93d3b7623910f225e3")

if __name__ == '__main__':
    unittest.main()