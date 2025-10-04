import unittest

# Assume the flip_case function exists in the same scope or is imported
# For demonstration purposes, a dummy function is provided:
# def flip_case(text):
#     flipped_chars = []
#     for char in text:
#         if 'a' <= char <= 'z':
#             flipped_chars.append(char.upper())
#         elif 'A' <= char <= 'Z':
#             flipped_chars.append(char.lower())
#         else:
#             flipped_chars.append(char)
#     return "".join(flipped_chars)

class TestFlipCase(unittest.TestCase):

    def test_hello_example(self):
        # Test the given example
        self.assertEqual(flip_case('Hello'), 'hELLO')

    def test_all_lowercase(self):
        # Test a string with all lowercase characters
        self.assertEqual(flip_case('python'), 'PYTHON')

    def test_all_uppercase(self):
        # Test a string with all uppercase characters
        self.assertEqual(flip_case('JAVASCRIPT'), 'javascript')

    def test_mixed_case_only_letters(self):
        # Test a string with mixed case letters
        self.assertEqual(flip_case('mIxEdCaSe'), 'MiXeDcAsE')

    def test_empty_string(self):
        # Test with an empty string
        self.assertEqual(flip_case(''), '')

    def test_string_with_numbers_and_symbols(self):
        # Test a string containing only non-alphabetic characters
        self.assertEqual(flip_case('123!@#$'), '123!@#$')

    def test_mixed_alpha_non_alpha(self):
        # Test a string with a mix of letters, numbers, and symbols
        self.assertEqual(flip_case('Foo Bar 123!'), 'fOO bAR 123!')

    def test_single_character_lowercase(self):
        # Test a single lowercase character
        self.assertEqual(flip_case('a'), 'A')

    def test_single_character_uppercase(self):
        # Test a single uppercase character
        self.assertEqual(flip_case('Z'), 'z')

    def test_leading_trailing_spaces(self):
        # Test with leading/trailing spaces and mixed content
        self.assertEqual(flip_case('  Test me  '), '  tEST ME  ')
    def test_single_characters(self):
            # Test with single lowercase letter
            self.assertEqual(self.solution.flip_case('a'), 'A')
            # Test with single uppercase letter
            self.assertEqual(self.solution.flip_case('Z'), 'z')
            # Test with single digit
            self.assertEqual(self.solution.flip_case('5'), '5')
            # Test with single symbol
            self.assertEqual(self.solution.flip_case('!'), '!')
            # Test with single space
            self.assertEqual(self.solution.flip_case(' '), ' ')

    def test_only_non_alphabetic_characters(self):
            # String containing only digits
            self.assertEqual(self.solution.flip_case('1234567890'), '1234567890')
            # String containing only symbols
            self.assertEqual(self.solution.flip_case('!@#$%^&*()'), '!@#$%^&*()')
            # String containing only spaces
            self.assertEqual(self.solution.flip_case('   '), '   ')
            # String containing mixed digits, symbols, and spaces
            self.assertEqual(self.solution.flip_case('1 2 3 ! @ #'), '1 2 3 ! @ #')

    def test_unicode_letters(self):
            # Test with lowercase Unicode letters
            self.assertEqual(self.solution.flip_case('résumé'), 'RÉSUMÉ')
            # Test with uppercase Unicode letters
            self.assertEqual(self.solution.flip_case('GRÜßE'), 'grüSSe') # 'ß' becomes 'SS' when upper() is applied to lower()
            # Test with mixed case Unicode letters
            self.assertEqual(self.solution.flip_case('Ça Va?'), 'cA vA?')
            # Test with letters that have no case equivalent (should remain unchanged, though unlikely for most script letters)
            self.assertEqual(self.solution.flip_case('こんにちは'), 'こんにちは') # Japanese hiragana are not cased

    def test_unicode_symbols_and_emojis(self):
            # Test with strings containing emojis
            self.assertEqual(self.solution.flip_case('Hello World 👋'), 'hELLO wORLD 👋')
            self.assertEqual(self.solution.flip_case('PYTHON 😊'), 'python 😊')
            # Test with mathematical symbols
            self.assertEqual(self.solution.flip_case('π r² = Area'), 'π R² = aREA')
            # Test with other non-alphabetic unicode characters
            self.assertEqual(self.solution.flip_case('© 2023 ABC'), '© 2023 abc')

    def test_mixed_complex_strings(self):
            # A more complex string combining various types of characters
            self.assertEqual(self.solution.flip_case('MiXeD-cAsE_sTrInG 123!@# ÅÄÖüß 😊'), 'mIxEd-CaSe_StRiNg 123!@# åäöÜSS 😊')
            # String starting and ending with non-alphabetic characters
            self.assertEqual(self.solution.flip_case('!_PyThOn_!'), '!_pYtHoN_!')
