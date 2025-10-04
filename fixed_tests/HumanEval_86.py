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
            # 'What a Wonderful Day!' -> 'Waht a Wdeflnoru !Day'
            # 'What' (W=87, h=104, a=97, t=116) -> 'Waht' (sorted: W, a, h, t)
            # 'a' -> 'a' (already sorted)
            # 'Wonderful' (W=87, o=111, n=110, d=100, e=101, r=114, f=102, u=117, l=108) -> 'Wdeflnoru' (sorted: W, d, e, f, l, n, o, r, u)
            # 'Day!' (D=68, a=97, y=121, !=33) -> '!Day' (sorted: !, D, a, y)
            self.assertEqual(anti_shuffle('What a Wonderful Day!'), 'Waht a Wdeflnoru !Day')
    def test_string_with_numbers_and_punctuation(self):
            # Test case including numbers, punctuation, and mixed case.
            # Original input: 'Python 3.9 is Cool!'
            #
            # Word analysis by anti_shuffle logic:
            # 1. 'Python' (P=80, y=121, t=116, h=104, o=111, n=110)
            #    - Is not ASCII sorted (e.g., 't' (116) < 'y' (121) is true at index 2 vs 1,
            #      meaning ord(word_str[2]) < ord(word_str[1]) is true, so it returns False).
            #    - Sorted: 'Phnoty' (P=80, h=104, n=110, o=111, t=116, y=121)
            # 2. '3.9' (3=51, .=46, 9=57)
            #    - Is not ASCII sorted (e.g., '.' (46) < '3' (51) is true at index 1 vs 0,
            #      meaning ord(word_str[1]) < ord(word_str[0]) is true, so it returns False).
            #    - Sorted: '.39' (.=46, 3=51, 9=57)
            # 3. 'is' (i=105, s=115)
            #    - Is ASCII sorted (115 < 105 is false).
            #    - Remains: 'is'
            # 4. 'Cool!' (C=67, o=111, o=111, l=108, !=33)
            #    - Is not ASCII sorted (e.g., 'l' (108) < 'o' (111) is true at index 3 vs 2,
            #      meaning ord(word_str[3]) < ord(word_str[2]) is true, so it returns False).
            #    - Sorted: '!Cloo' (!=33, C=67, l=108, o=111, o=111)
            #
            # Expected combined result: 'Phnoty .39 is !Cloo'
            self.assertEqual(anti_shuffle('Python 3.9 is Cool!'), 'Phnoty .39 is !Cloo')
