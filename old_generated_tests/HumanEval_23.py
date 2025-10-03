import unittest

class TestStrlen(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_short_string(self):
        self.assertEqual(strlen('abc'), 3)

    def test_string_with_spaces(self):
        self.assertEqual(strlen('hello world'), 11)

    def test_string_with_numbers(self):
        self.assertEqual(strlen('12345'), 5)

    def test_string_with_special_characters(self):
        self.assertEqual(strlen('!@#$%^&*()'), 10)

    def test_longer_string(self):
        self.assertEqual(strlen('This is a relatively long string.'), 32)

    def test_string_with_unicode_characters(self):
        self.assertEqual(strlen('你好世界'), 4) # Chinese for "Hello World"

    def test_string_with_newline_and_tab(self):
        self.assertEqual(strlen('line1\n\tline2'), 11)

    def test_string_with_only_spaces(self):
        self.assertEqual(strlen('    '), 4)

    def test_mixed_characters(self):
        self.assertEqual(strlen('Pyth0n! is #FUN'), 15)

if __name__ == '__main__':
    unittest.main()