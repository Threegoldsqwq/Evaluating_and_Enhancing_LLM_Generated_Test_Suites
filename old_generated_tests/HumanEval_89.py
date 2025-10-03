import unittest

# Assume the 'encrypt' function is defined elsewhere, e.g.:
# def encrypt(s: str) -> str:
#     # Placeholder for the actual implementation
#     encrypted_chars = []
#     shift = 2 * 2  # Shift down by two multiplied to two places = 4
#     for char in s:
#         if 'a' <= char <= 'z':
#             start_code = ord('a')
#             original_pos = ord(char) - start_code
#             new_pos = (original_pos + shift) % 26
#             encrypted_chars.append(chr(start_code + new_pos))
#         else:
#             # Keep non-lowercase alphabet characters as they are
#             encrypted_chars.append(char)
#     return "".join(encrypted_chars)


class TestEncrypt(unittest.TestCase):

    def test_example_hi(self):
        self.assertEqual(encrypt('hi'), 'lm')

    def test_example_asdfghjkl(self):
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')

    def test_example_gf(self):
        self.assertEqual(encrypt('gf'), 'kj')

    def test_example_et(self):
        self.assertEqual(encrypt('et'), 'ix')

    def test_empty_string(self):
        self.assertEqual(encrypt(''), '')

    def test_string_with_wrap_around(self):
        # Letters 'x', 'y', 'z' should wrap around to 'b', 'c', 'd'
        self.assertEqual(encrypt('xyz'), 'bcd')

    def test_string_with_spaces_and_non_alpha(self):
        # Spaces and other characters should remain unchanged
        self.assertEqual(encrypt('hello world 123!'), 'lipps asvph 123!')

    def test_mixed_case_string(self):
        # Only lowercase letters should be encrypted, uppercase preserved
        self.assertEqual(encrypt('Hello World'), 'Lipps Asvph')

    def test_all_lowercase_alphabet(self):
        # Encrypting the entire lowercase alphabet
        self.assertEqual(encrypt('abcdefghijklmnopqrstuvwxyz'), 'efghijklmnopqrstuvwxyzabcd')

    def test_string_with_only_non_alpha(self):
        # String with only numbers and symbols
        self.assertEqual(encrypt('12345!@#$%^&*()'), '12345!@#$%^&*()')