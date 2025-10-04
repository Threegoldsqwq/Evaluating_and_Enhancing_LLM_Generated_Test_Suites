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

    def test_anti_shuffle_empty_string(self):
            self.assertEqual(anti_shuffle(''), '')

    def test_anti_shuffle_only_spaces(self):
            # Exercises 'if not part' branch multiple times for empty input strings.
            self.assertEqual(anti_shuffle('   '), '   ')
            self.assertEqual(anti_shuffle(' '), ' ')

    def test_anti_shuffle_leading_trailing_and_multiple_internal_spaces_with_sorted_words(self):
            # Covers extensive 'if not part' scenarios where words themselves are already sorted.
            self.assertEqual(anti_shuffle('  a b  c   '), '  a b  c   ')
            self.assertEqual(anti_shuffle('  Hi  World '), '  Hi  Wdlor ') # 'World' is unsorted

    def test_anti_shuffle_leading_trailing_and_multiple_internal_spaces_with_unsorted_words(self):
            # Covers 'if not part' and 'else' (word sorting) branches in combination.
            self.assertEqual(anti_shuffle('  zyx  cba   '), '  xyz  abc   ')
            self.assertEqual(anti_shuffle('   word1   word2!   '), '   dlorw1   !drow2   ')

    def test_anti_shuffle_mixed_case_and_numbers_unsorted_words(self):
            # Covers 'else' branch with various character types that require sorting.
            self.assertEqual(anti_shuffle('bA'), 'Ab') # 'A' (65) < 'b' (98)
            self.assertEqual(anti_shuffle('21'), '12')
            self.assertEqual(anti_shuffle('aBc 321'), 'Bca 123') # 'a'(97), 'B'(66), 'c'(99) -> Bca
            self.assertEqual(anti_shuffle('PiE'), 'Eip') # 'P'(80), 'i'(105), 'E'(69) -> E P i

    def test_anti_shuffle_special_characters_unsorted_words(self):
            # Covers 'else' branch with special characters that require sorting.
            self.assertEqual(anti_shuffle('!^@'), '!@^') # ord('!')=33, ord('^')=94, ord('@')=64 -> !, @, ^
            self.assertEqual(anti_shuffle('Z-a'), '-Za') # ord('Z')=90, ord('-')=45, ord('a')=97 -> -, Z, a

    def test_anti_shuffle_complex_scenario(self):
            # Comprehensive test covering all branches and types of words/spaces.
            input_str = '  Aab  cBa 987 !@#$  '
            # 'Aab' is sorted -> 'Aab'
            # 'cBa' is unsorted ('c'>'B') -> 'Bac'
            # '987' is unsorted ('9'>'8') -> '789'
            # '!@#$' is unsorted ('@'>'#') -> '!#$@'
            expected_str = '  Aab  Bac 789 !#$@  ' 
            self.assertEqual(anti_shuffle(input_str), expected_str)

        # --- Tests for is_sorted_ascii to ensure its branches are fully covered ---

    def test_is_sorted_ascii_empty_string(self):
            # Covers: 'if len(word_str) <= 1:' (True branch)
            self.assertTrue(is_sorted_ascii(''))

    def test_is_sorted_ascii_single_char_string(self):
            # Covers: 'if len(word_str) <= 1:' (True branch)
            self.assertTrue(is_sorted_ascii('a'))
            self.assertTrue(is_sorted_ascii('Z'))
            self.assertTrue(is_sorted_ascii('9'))
            self.assertTrue(is_sorted_ascii('!'))

    def test_is_sorted_ascii_multi_chars_fully_sorted(self):
            # Covers: 'if len(word_str) <= 1:' (False branch), and loop completes without 'return False'.
            self.assertTrue(is_sorted_ascii('abc'))
            self.assertTrue(is_sorted_ascii('ABC'))
            self.assertTrue(is_sorted_ascii('123'))
            self.assertTrue(is_sorted_ascii('!#@')) # ord('!')=33, ord('#')=35, ord('@')=64 - this sequence is sorted by ASCII

    def test_is_sorted_ascii_multi_chars_unsorted_first_pair(self):
            # Covers: 'if len(word_str) <= 1:' (False branch), and 'if ord(word_str[i]) < ord(word_str[i-1]):' (True branch) immediately.
            self.assertFalse(is_sorted_ascii('ba'))
            self.assertFalse(is_sorted_ascii('ZYX'))
            self.assertFalse(is_sorted_ascii('21'))
            self.assertFalse(is_sorted_ascii('@!')) # ord('@')=64, ord('!')=33. 64 is not less than 33.

    def test_is_sorted_ascii_multi_chars_unsorted_middle_or_end(self):
            # Covers: 'if len(word_str) <= 1:' (False branch), and 'if ord(word_str[i]) < ord(word_str[i-1]):' (True branch) after some iterations.
            self.assertFalse(is_sorted_ascii('abac')) # 'a'<'b' is True; 'b'<'a' is False, so return False.
            self.assertFalse(is_sorted_ascii('abzc')) # 'a'<'b' (True), 'b'<'z' (True), 'z'<'c' (False), so return False.
            self.assertFalse(is_sorted_ascii('!#@$')) # ! (33) < # (35) (True), # (35) < @ (64) (True), @ (64) < $ (36) (False), so return False.

    def test_is_sorted_ascii_mixed_char_types_sorted(self):
            self.assertTrue(is_sorted_ascii('1A')) # ord('1')=49, ord('A')=65
            self.assertTrue(is_sorted_ascii('Za')) # ord('Z')=90, ord('a')=97
            self.assertTrue(is_sorted_ascii('A_c')) # ord('A')=65, ord('_')=95, ord('c')=99

    def test_is_sorted_ascii_mixed_char_types_unsorted(self):
            self.assertFalse(is_sorted_ascii('A1')) # ord('A')=65, ord('1')=49
            self.assertFalse(is_sorted_ascii('aZ')) # ord('a')=97, ord('Z')=90
            self.assertFalse(is_sorted_ascii('c_A')) # ord('c')=99, ord('_')=95, ord('A')=65
