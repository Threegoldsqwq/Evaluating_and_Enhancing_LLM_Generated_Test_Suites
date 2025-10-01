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