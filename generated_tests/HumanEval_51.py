import unittest

class TestRemoveVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_all_vowels(self):
        self.assertEqual(remove_vowels('aeiouAEIOU'), '')

    def test_all_consonants(self):
        self.assertEqual(remove_vowels('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'), 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')

    def test_mixed_case_vowels_and_consonants(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_standard_mixed_string(self):
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')

    def test_string_with_newline(self):
        self.assertEqual(remove_vowels('abcdef\nghijklm'), 'bcdf\nghjklm')

    def test_string_with_numbers_and_symbols(self):
        self.assertEqual(remove_vowels('123abc!@#def'), '123bc!@#df')

    def test_string_with_spaces_and_punctuation(self):
        self.assertEqual(remove_vowels('Hello World!'), 'Hll Wrld!')

    def test_single_vowel(self):
        self.assertEqual(remove_vowels('a'), '')

    def test_single_consonant(self):
        self.assertEqual(remove_vowels('z'), 'z')