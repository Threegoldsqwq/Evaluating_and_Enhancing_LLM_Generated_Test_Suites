import unittest

class TestCorrectBracketing(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(correct_bracketing(""))

    def test_simple_valid_pair(self):
        self.assertTrue(correct_bracketing("<>"))

    def test_unclosed_opening_bracket(self):
        self.assertFalse(correct_bracketing("<"))

    def test_unopened_closing_bracket(self):
        self.assertFalse(correct_bracketing(">"))

    def test_closing_before_opening(self):
        self.assertFalse(correct_bracketing("><"))

    def test_nested_valid_brackets(self):
        self.assertTrue(correct_bracketing("<<>>"))

    def test_complex_nested_valid_brackets(self):
        self.assertTrue(correct_bracketing("<<><>>"))

    def test_not_enough_closing_brackets(self):
        self.assertFalse(correct_bracketing("<<>"))

    def test_too_many_closing_brackets(self):
        self.assertFalse(correct_bracketing("<>>>"))


    def test_long_valid_sequence(self):
        self.assertTrue(correct_bracketing("<<<<>>>>"))

    # An additional test for long invalid sequence
    def test_long_invalid_sequence(self):
        self.assertFalse(correct_bracketing("<<<<>>>>>"))
    def test_empty_string(self):
            # Covers the case where the input string is empty,
            # ensuring the loop is skipped and the final balance == 0 returns True.
            self.assertTrue(correct_bracketing(""))

    def test_balance_goes_negative_mid_string(self):
            # Covers the branch where `balance` becomes negative after some valid operations,
            # triggering the early `return False` within the loop (lines 11-12).
            # Existing tests cover `balance < 0` immediately (`><<>`), but not after processing other brackets.
            # Balance sequence: 0 -> 1 ('<') -> 2 ('<') -> 1 ('>') -> 0 ('>') -> -1 ('>')
            self.assertFalse(correct_bracketing("<<>>><"))
