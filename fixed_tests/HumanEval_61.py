import unittest

class TestCorrectBracketing(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(correct_bracketing(""))

    def test_simple_valid(self):
        self.assertTrue(correct_bracketing("()"))

    def test_nested_valid(self):
        self.assertTrue(correct_bracketing("(())"))

    def test_sequential_valid(self):
        self.assertTrue(correct_bracketing("()()"))

    def test_complex_valid(self):
        self.assertTrue(correct_bracketing("(()(()))"))

    def test_single_open_invalid(self):
        self.assertFalse(correct_bracketing("("))

    def test_single_close_invalid(self):
        self.assertFalse(correct_bracketing(")"))

    def test_unmatched_open_invalid(self):
        self.assertFalse(correct_bracketing("(()("))

    def test_unmatched_close_invalid(self):
        self.assertFalse(correct_bracketing(")("))

    def test_interspersed_invalid(self):
        self.assertFalse(correct_bracketing("())("))