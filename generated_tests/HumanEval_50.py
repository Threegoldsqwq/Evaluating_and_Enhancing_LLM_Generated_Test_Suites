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
            self.assertEqual(encode_shift(""), "")
    def test_only_lowercase_letters(self):
            self.assertEqual(encode_shift("abc"), "fgh")

    def test_lowercase_wrap_around(self):
            self.assertEqual(encode_shift("xyz"), "cde")

    def test_mixed_case_with_spaces(self):
            self.assertEqual(encode_shift("Hello World"), "Mjqqt Btwqi")
    def test_non_alphabetic_characters(self):
            self.assertEqual(encode_shift("123!@# $"), "123!@# $")
    def test_mixed_alphanumeric_and_symbols(self):
            self.assertEqual(encode_shift("Test123!"), "Yjxy123!")
    def test_long_sentence_with_wrap_around(self):
            self.assertEqual(encode_shift("The quick brown fox jumps over the lazy dog."),
                             "Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl.")

    def test_empty_string(self):
            """Tests encoding and decoding of an empty string."""
            self.assertEqual(encode_shift(""), "")
            self.assertEqual(decode_shift(""), "")

    def test_non_alphabetic_characters(self):
            """Tests strings containing only non-alphabetic characters,
            including specific characters from partial coverage feedback."""
            non_alpha_text = "123047!@#$%^&*()_+-=[]{}|;:'\",.<>/?`~ "
            self.assertEqual(encode_shift(non_alpha_text), non_alpha_text)
            self.assertEqual(decode_shift(non_alpha_text), non_alpha_text)

            # Specifically target characters indicated by partial coverage: ',', '-', '0', '1', '2', '4', '7'
            self.assertEqual(encode_shift(",-01247"), ",-01247")
            self.assertEqual(decode_shift(",-01247"), ",-01247")
            self.assertEqual(encode_shift(" "), " ")
            self.assertEqual(decode_shift(" "), " ")

    def test_lowercase_full_wrap_around(self):
            """Tests lowercase characters that wrap from the end to the beginning of the alphabet."""
            # Encoding 'v' (21) + 5 = 26 % 26 = 0 -> 'a'
            # Encoding 'z' (25) + 5 = 30 % 26 = 4 -> 'e'
            self.assertEqual(encode_shift("uvwxyz"), "zabcde")
            self.assertEqual(decode_shift("zabcde"), "uvwxyz")
            self.assertEqual(encode_shift("xyz"), "cde") # Specific check for 'xyz'
            self.assertEqual(decode_shift("cde"), "xyz") # Specific check for 'cde'

    def test_uppercase_full_wrap_around(self):
            """Tests uppercase characters that wrap from the end to the beginning of the alphabet."""
            # Encoding 'V' (21) + 5 = 26 % 26 = 0 -> 'A'
            # Encoding 'Z' (25) + 5 = 30 % 26 = 4 -> 'E'
            self.assertEqual(encode_shift("UVWXYZ"), "ZABCDE")
            self.assertEqual(decode_shift("ZABCDE"), "UVWXYZ")
            self.assertEqual(encode_shift("XYZ"), "CDE") # Specific check for 'XYZ'
            self.assertEqual(decode_shift("CDE"), "XYZ") # Specific check for 'CDE'

    def test_single_character_strings(self):
            """Tests encoding and decoding of single character strings across different types."""
            self.assertEqual(encode_shift("a"), "f")
            self.assertEqual(encode_shift("z"), "e")
            self.assertEqual(encode_shift("A"), "F")
            self.assertEqual(encode_shift("Z"), "E")
            self.assertEqual(encode_shift("7"), "7") # Numeric character
            self.assertEqual(encode_shift("!"), "!") # Symbol

            self.assertEqual(decode_shift("f"), "a")
            self.assertEqual(decode_shift("e"), "z")
            self.assertEqual(decode_shift("F"), "A")
            self.assertEqual(decode_shift("E"), "Z")
            self.assertEqual(decode_shift("7"), "7")
            self.assertEqual(decode_shift("!"), "!")

    def test_mixed_string_roundtrip_with_all_partial_targets(self):
            """Tests a complex string with mixed case, numbers, symbols, and wrap-around characters.
            Ensures a full roundtrip (encode then decode) restores the original string."""
            original_text = "ThIs Is A MiXeD sTrInG wItH 0123456789!@#$%^&*()_+=-[]{}|;:'\",.<>/?`~ And Some XYZ-abc."
            encoded_text = encode_shift(original_text)
            decoded_text = decode_shift(encoded_text)
            self.assertEqual(decoded_text, original_text)

            # Verify a specific portion of the encoded text for sanity check
            self.assertEqual(encoded_text, "YmNx Nx F RnCjI xYwNsL bNyM 0123456789!@#$%^&*()_+=-[]{}|;:'\",.<>/?`~ Fqi Xtrj CDE-fgh.")
# This allows running the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)