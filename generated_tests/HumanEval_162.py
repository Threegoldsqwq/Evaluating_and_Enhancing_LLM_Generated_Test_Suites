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


    def test_empty_string_returns_none(self):
            """
            Tests the edge case of an empty string, which should return None.
            This covers the 'if not text:' branch (True path) and the subsequent 'return None'.
            """
            self.assertIsNone(string_to_md5(''))

    def test_basic_alphanumeric_string(self):
            """
            Tests a basic alphanumeric string to ensure the MD5 hash is correctly generated.
            This covers the 'if not text:' branch (False path) and the MD5 hashing logic.
            """
            self.assertEqual(string_to_md5('teststring'), '5d41402abc4b2a76b9719d911017c592')

    def test_string_with_whitespace(self):
            """
            Tests a string containing various whitespace characters.
            """
            self.assertEqual(string_to_md5('  hello world  '), '4c1d2e230327f2f1839e99a844855a53')
            self.assertEqual(string_to_md5('\tnewline\n'), 'f089694116c4c69811f5d72f9ff0d1a4')

    def test_string_with_only_whitespace(self):
            """
            Tests a string that consists only of whitespace characters.
            """
            self.assertEqual(string_to_md5('   '), '379d75069b7636e053d2d24d2621c168')

    def test_string_with_unicode_characters(self):
            """
            Tests a string containing non-ASCII (Unicode) characters to ensure UTF-8 encoding is handled correctly.
            """
            self.assertEqual(string_to_md5('你好世界'), '211e4f45143a44f9f74358de711202e2')
            self.assertEqual(string_to_md5('résumé'), '034e403d526e3c32729a8a728d8b4e7e')
            self.assertEqual(string_to_md5('😂🤷‍♀️👍'), '6b127393282b13286082987dd5a14d59')

    def test_long_string(self):
            """
            Tests a relatively long string to ensure the hashing handles larger inputs efficiently.
            """
            long_text = "This is a very long string that should be hashed correctly by the MD5 algorithm. " * 10
            self.assertEqual(string_to_md5(long_text), '70f2b3802e9ee4c2293b036ce85c1ec8')
if __name__ == '__main__':
    unittest.main()