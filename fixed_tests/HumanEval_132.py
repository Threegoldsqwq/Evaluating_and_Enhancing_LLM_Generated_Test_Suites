import unittest

class TestIsNested(unittest.TestCase):

    # Test cases that should return True (a valid nested subsequence [[]] can be formed)

    def test_01_simple_nested(self):
        # The simplest string that is itself a nested sequence
        self.assertTrue(is_nested('[[]]'))

    def test_02_nested_with_side_by_side_pairs(self):
        # A nested sequence with other valid, non-nested pairs
        self.assertTrue(is_nested('[[][]]'))

    def test_03_deeply_nested(self):
        # A more deeply nested sequence, which still contains a simple [[]] subsequence
        self.assertTrue(is_nested('[[[]]]'))

    def test_04_nested_subsequence_from_spread_brackets(self):
        # The required brackets for [[]] are not contiguous but can be picked
        # s[4], s[5], s[7], s[8] form '[[]]'
        self.assertTrue(is_nested('[]]]][[[[]]]'))

    def test_05_nested_subsequence_mid_string(self):
        # A [[]] subsequence exists somewhere in the middle of the string
        # s[2], s[3], s[4], s[5] form '[[]]'
        self.assertTrue(is_nested('[][[[]]]'))

    # Test cases that should return False (no valid nested subsequence [[]] can be formed)

    def test_06_simple_flat_sequence(self):
        # The simplest valid, but not nested, bracket sequence
        self.assertFalse(is_nested('[]'))

    def test_07_multiple_flat_sequences(self):
        # Multiple valid, but not nested, bracket sequences
        self.assertFalse(is_nested('[][]'))

    def test_08_only_opening_brackets(self):
        # String contains only opening brackets
        self.assertFalse(is_nested('[[[['))

    def test_09_only_closing_brackets_and_one_open(self):
        # String contains mostly closing brackets with one open bracket
        self.assertFalse(is_nested(']]]]]][]'))

    def test_10_complex_unbalanced_no_nested(self):
        # A long, complex string with mixed brackets, but no [[]] subsequence
        # This is one of the examples from the problem description
        self.assertFalse(is_nested('[]]]]]]][[[[[]'))

    # Additional edge cases (not strictly required for 10, but good practice)
    # def test_11_empty_string(self):
    #     self.assertFalse(is_nested(''))
    #
    # def test_12_unbalanced_without_second_open(self):
    #     self.assertFalse(is_nested('[[]')) # Requires 4 brackets