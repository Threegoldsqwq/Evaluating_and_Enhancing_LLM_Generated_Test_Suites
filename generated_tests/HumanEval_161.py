import unittest

# Assume the solve function is defined elsewhere, e.g.:
# def solve(s: str) -> str:
#     has_letters = any(c.isalpha() for c in s)
#     
#     if not has_letters:
#         return s[::-1]
#     else:
#         result = []
#         for char in s:
#             if char.isalpha():
#                 if char.islower():
#                     result.append(char.upper())
#                 else:
#                     result.append(char.lower())
#             else:
#                 result.append(char)
#         return "".join(result)

class TestSolve(unittest.TestCase):

    def test_no_letters_digits_only(self):
        # String with no letters, only digits. Should be reversed.
        self.assertEqual(solve("1234"), "4321")

    def test_letters_only_lowercase(self):
        # String with only lowercase letters. All should be uppercased.
        self.assertEqual(solve("ab"), "AB")

    def test_mixed_chars_and_case(self):
        # String with letters, symbols, and mixed case. Letters should swap case.
        self.assertEqual(solve("#a@C"), "#A@c")

    def test_empty_string(self):
        # Empty string, no letters. Should be reversed (remains empty).
        self.assertEqual(solve(""), "")

    def test_letters_only_uppercase(self):
        # String with only uppercase letters. All should be lowercased.
        self.assertEqual(solve("HELLO"), "hello")

    def test_mixed_letters_and_digits(self):
        # String with mixed letters (mixed case) and digits. Letters swap case.
        self.assertEqual(solve("Python3"), "pYTHON3")

    def test_letters_only_mixed_case(self):
        # String with only letters, mixed case. All letters should swap case.
        self.assertEqual(solve("rEvErSe"), "ReVeRsE")

    def test_mixed_letters_and_underscore(self):
        # String with letters (mixed case) and an underscore. Letters swap case.
        self.assertEqual(solve("abc_XYZ"), "ABC_xyz")

    def test_no_letters_symbols_only(self):
        # String with no letters, only symbols. Should be reversed.
        self.assertEqual(solve("!@#$"), "$#@!")

    def test_mixed_letters_spaces_and_symbol(self):
        # String with mixed case letters, spaces, and a symbol. Letters swap case, others remain.
        self.assertEqual(solve("Hello World!"), "hELLO wORLD!")
    def test_empty_string(self):
            # Covers the 'has_letters = False' path for an empty input
            self.assertEqual(solve(""), "")

    def test_no_letters_only_digits(self):
            # Covers the 'has_letters = False' path with only digits
            self.assertEqual(solve("12345"), "54321")

    def test_no_letters_only_symbols(self):
            # Covers the 'has_letters = False' path with only symbols
            self.assertEqual(solve("!@#$%"), "%$#@!")

    def test_no_letters_mixed_non_alpha(self):
            # Covers the 'has_letters = False' path with mixed non-alphabetic characters
            self.assertEqual(solve("  123 !@#  "), "  #@! 321  ")

    def test_string_with_only_spaces(self):
            # Covers the 'has_letters = False' path with only spaces
            self.assertEqual(solve("   "), "   ")

    def test_all_lowercase_letters(self):
            # Covers the 'has_letters = True' path, ensuring all lowercase become uppercase
            self.assertEqual(solve("hello"), "HELLO")

    def test_all_uppercase_letters(self):
            # Covers the 'has_letters = True' path, ensuring all uppercase become lowercase
            self.assertEqual(solve("WORLD"), "world")

    def test_mixed_case_letters(self):
            # Covers the 'has_letters = True' path, ensuring mixed case reversal
            self.assertEqual(solve("PyThoN"), "pYtHoN")

    def test_mixed_letters_and_non_letters(self):
            # Covers the 'has_letters = True' path, ensuring non-letters remain unchanged
            self.assertEqual(solve("a1B2c!3D"), "A1b2C!3d")

    def test_single_lowercase_letter(self):
            # Covers 'has_letters = True' for a minimal case (single lowercase letter)
            self.assertEqual(solve("x"), "X")

    def test_single_uppercase_letter(self):
            # Covers 'has_letters = True' for a minimal case (single uppercase letter)
            self.assertEqual(solve("Y"), "y")

    def test_letters_at_start_middle_end(self):
            # Covers 'has_letters = True' path with letters at various positions
            self.assertEqual(solve("a_123_Z_b"), "A_123_z_B")

    def test_string_with_unicode_letters_lower(self):
            # Covers 'has_letters = True' path with unicode lowercase letters
            self.assertEqual(solve("straße"), "STRASSE")

    def test_string_with_unicode_letters_upper(self):
            # Covers 'has_letters = True' path with unicode uppercase letters
            self.assertEqual(solve("CAFÉ"), "café")

    def test_string_with_mixed_unicode_and_ascii_letters(self):
            # Covers 'has_letters = True' path with a mix of unicode and ASCII letters
            self.assertEqual(solve("Python-Grüße"), "pYTHON-gRÜSSE")
