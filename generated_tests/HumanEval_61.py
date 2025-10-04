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
    def test_empty_string(self):
            # Covers the case where the input is an empty string.
            # This path skips the loop and returns True.
            self.assertTrue(correct_bracketing(""))

    def test_simple_balanced(self):
            # Covers a basic correctly balanced string.
            # Exercises both increments and decrements, and ends with balance == 0.
            self.assertTrue(correct_bracketing("()"))

    def test_simple_unbalanced_open(self):
            # Covers an unbalanced string with an extra opening bracket at the end.
            # This path goes through the loop and ends with balance > 0, returning False.
            self.assertFalse(correct_bracketing("("))
            self.assertFalse(correct_bracketing("(()"))

    def test_simple_unbalanced_close_early_exit(self):
            # Covers an unbalanced string starting with a closing bracket, leading to an early exit.
            # Exercises the 'if balance < 0: return False' branch.
            self.assertFalse(correct_bracketing(")"))
            self.assertFalse(correct_bracketing(")("))

    def test_nested_balanced(self):
            # Covers more complex nested balanced brackets.
            # Ensures the balance counter correctly handles multiple levels.
            self.assertTrue(correct_bracketing("(()())"))
            self.assertTrue(correct_bracketing("((()))"))

    def test_nested_unbalanced_early_exit(self):
            # Covers a nested string that becomes unbalanced mid-way, leading to an early exit.
            # Specifically targets 'if balance < 0: return False' after some valid operations.
            self.assertFalse(correct_bracketing("())"))
            self.assertFalse(correct_bracketing("(()))"))

    def test_mixed_unbalanced_at_end(self):
            # Covers a string that appears balanced for a while but ends with an unmatched opening.
            # Ensures the final check 'return balance == 0' correctly catches this.
            self.assertFalse(correct_bracketing("()("))
            self.assertFalse(correct_bracketing("(()()("))
