import unittest

class TestEncodeFunction(unittest.TestCase):

    def test_01_empty_string(self):
        # Test with an empty string
        self.assertEqual(encode(''), '')

    def test_02_single_lowercase_vowel(self):
        # Test a single lowercase vowel 'a'
        # 'a' -> swapped case 'A', 'a' is vowel, 'a'+2='c', apply 'A' case -> 'C'
        self.assertEqual(encode('a'), 'C')

    def test_03_single_uppercase_vowel(self):
        # Test a single uppercase vowel 'U'
        # 'U' -> swapped case 'u', 'U' is vowel, 'u'+2='w', apply 'u' case -> 'w'
        self.assertEqual(encode('U'), 'w')

    def test_04_single_lowercase_consonant(self):
        # Test a single lowercase consonant 'b'
        # 'b' -> swapped case 'B', 'b' is not vowel, result 'B'
        self.assertEqual(encode('b'), 'B')

    def test_05_single_uppercase_consonant(self):
        # Test a single uppercase consonant 'Z'
        # 'Z' -> swapped case 'z', 'Z' is not vowel, result 'z'
        self.assertEqual(encode('Z'), 'z')

    def test_06_mixed_vowels_consonants_no_spaces(self):
            # Test a word with mixed vowels and consonants, no spaces
            # 'Coding'
            # C -> c (Original uppercase, not vowel -> swap to lowercase)
            # o -> Q ('o' is vowel, +2='q'. Original lowercase -> swap to uppercase)
            # d -> D (Original lowercase, not vowel -> swap to uppercase)
            # i -> K ('i' is vowel, +2='k'. Original lowercase -> swap to uppercase)
            # n -> N (Original lowercase, not vowel -> swap to uppercase)
            # g -> G (Original lowercase, not vowel -> swap to uppercase)
            self.assertEqual(encode('Coding'), 'cQDKNG')
    def test_07_sentence_with_all_vowels(self):
            # Test a full sentence with mixed characters and spaces, includes all vowels
            # 'The quick brown fox jumps over the lazy dog'
            # The correct encoding should be:
            # 'tHG QWKCK BRQWN FQX JWMPS QVGR THG LCZY DQG'
            self.assertEqual(encode('The quick brown fox jumps over the lazy dog'), 'tHG QWKCK BRQWN FQX JWMPS QVGR THG LCZY DQG')
    def test_08_uppercase_vowels_with_spaces(self):
        # Test a string with only uppercase vowels and spaces
        # 'A E I O U'
        # A -> c, E -> g, I -> k, O -> q, U -> w (all lowercase as target case is lowercase)
        self.assertEqual(encode('A E I O U'), 'c g k q w')

    def test_09_alphanumeric_and_symbols(self):
        # Test string with numbers, symbols, and letters
        # The problem states "Assume only letters", but examples show spaces preserved.
        # This test checks if non-letter characters are preserved as is.
        # '123test!@#' -> '123TGST!@#'
        self.assertEqual(encode('123test!@#'), '123TGST!@#')

    def test_10_longer_word_multiple_vowels(self):
        # Test a longer word with repeated vowels
        # 'Mississippi'
        # M -> m
        # i -> K (from I)
        # s -> S
        # s -> S
        # i -> K (from I)
        # s -> S
        # s -> S
        # i -> K (from I)
        # p -> P
        # p -> P
        # i -> K (from I)
        self.assertEqual(encode('Mississippi'), 'mKSSKSSKPPK')