import unittest

class TestAntiShuffle(unittest.TestCase):

    def test_empty_string(self):
        # Test case for an empty input string.
        self.assertEqual(anti_shuffle(''), '')

    def test_single_character(self):
        # Test case for a single character string.
        self.assertEqual(anti_shuffle('a'), 'a')

    def test_single_word_already_sorted(self):
        # Test case for a single word that is already in ascending ASCII order.
        self.assertEqual(anti_shuffle('abc'), 'abc')

    def test_single_word_unsorted(self):
        # Test case for a single word that needs sorting.
        self.assertEqual(anti_shuffle('hello'), 'ehllo')

    def test_single_word_mixed_case(self):
        # Test case for a single word with mixed-case characters.
        # 'B' (66) comes before 'a' (97) which comes before 'C' (67) is wrong.
        # 'B' (66), 'C' (67), 'a' (97). So 'BaC' -> 'BCA' is wrong.
        # 'B' (66), 'a' (97), 'C' (67). Sorted: 'B', 'C', 'a' -> 'BCa'
        # Let's recheck this specific example: 'BaC'
        # B = 66, a = 97, C = 67
        # Sorted by ASCII: B (66), C (67), a (97) -> 'BCa'
        self.assertEqual(anti_shuffle('BaC'), 'BCa')

    def test_multiple_words_simple(self):
        # Test case for a string with multiple simple words.
        self.assertEqual(anti_shuffle('cat dog'), 'act dgo')

    def test_multiple_words_with_symbols(self):
        # Test case for a string with multiple words, including symbols and mixed-case.
        # Based on example: 'Hello World!!!' -> 'Hello !!!Wdlor'
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')

    def test_string_with_various_spaces(self):
        # Test case for a string with leading, trailing, and multiple spaces between words.
        self.assertEqual(anti_shuffle('  test  string  '), '  estt  ginrst  ')

    def test_complex_sentence(self):
        # Test case for a more complex sentence with different word types.
        # 'What a Wonderful Day!' -> 'aHtw a deflnoruW !Dya'
        # What -> aHtw (W=87, h=104, a=97, t=116) -> aHtw
        # a -> a
        # Wonderful -> deflnoruW (W=87, o=111, n=110, d=100, e=101, r=114, f=102, u=117, l=108) -> deflnoruW
        # Day! -> !Dya (D=68, a=97, y=121, !=33) -> !Dya
        self.assertEqual(anti_shuffle('What a Wonderful Day!'), 'aHtw a deflnoruW !Dya')

    def test_string_with_numbers_and_punctuation(self):
        # Test case including numbers, punctuation, and mixed case.
        # 'Python 3.9 is Cool!' -> 'Hnopty .39 is !Cloo'
        # Python -> Hnopty (P=80, y=121, t=116, h=104, o=111, n=110) -> Hnopty
        # 3.9 -> .39 (.=46, 3=51, 9=57) -> .39
        # is -> is
        # Cool! -> !Cloo (!=33, C=67, o=111, o=111, l=108) -> !Cloo
        self.assertEqual(anti_shuffle('Python 3.9 is Cool!'), 'Hnopty .39 is !Cloo')