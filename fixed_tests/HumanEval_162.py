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


if __name__ == '__main__':
    unittest.main()