import unittest

# Assume the function 'encode_string' exists and is imported or defined elsewhere.
# For the purpose of running these tests independently, a dummy function is provided.
# In a real scenario, you would remove this dummy and import the actual function.
# def encode_string(text):
#     encoded_chars = []
#     for char in text:
#         if 'a' <= char <= 'z':
#             # Shift lowercase letter by 5, wrap around using modulo arithmetic
#             shifted_char = chr(((ord(char) - ord('a') + 5) % 26) + ord('a'))
#             encoded_chars.append(shifted_char)
#         elif 'A' <= char <= 'Z':
#             # Shift uppercase letter by 5, wrap around
#             shifted_char = chr(((ord(char) - ord('A') + 5) % 26) + ord('A'))
#             encoded_chars.append(shifted_char)
#         else:
#             # Non-alphabetic characters remain unchanged
#             encoded_chars.append(char)
#     return "".join(encoded_chars)


class TestEncodeString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(encode_string(""), "")

    def test_only_lowercase_letters(self):
        self.assertEqual(encode_string("abc"), "fgh")

    def test_only_uppercase_letters(self):
        self.assertEqual(encode_string("ABC"), "FGH")

    def test_lowercase_wrap_around(self):
        self.assertEqual(encode_string("xyz"), "cde")

    def test_uppercase_wrap_around(self):
        self.assertEqual(encode_string("XYZ"), "CDE")

    def test_mixed_case_with_spaces(self):
        self.assertEqual(encode_string("Hello World"), "Mjqqt Btwqi")

    def test_non_alphabetic_characters(self):
        self.assertEqual(encode_string("123!@# $"), "123!@# $")

    def test_mixed_alphanumeric_and_symbols(self):
        self.assertEqual(encode_string("Test123!"), "Yjxy123!")

    def test_long_sentence_with_wrap_around(self):
        self.assertEqual(encode_string("The quick brown fox jumps over the lazy dog."),
                         "Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl.")

    def test_single_character_wrap_z(self):
        self.assertEqual(encode_string("z"), "e")

# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)