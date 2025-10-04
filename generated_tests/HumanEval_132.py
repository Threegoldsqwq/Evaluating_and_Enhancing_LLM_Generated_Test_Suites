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
    def test_empty_string(self):
            # Test case: Empty string should return False as no brackets are present.
            # This ensures the 'for' loop is correctly handled when the input is empty.
            self.assertFalse(is_nested(''))

    def test_single_open_bracket(self):
            # Test case: Single opening bracket. Should not be nested.
            self.assertFalse(is_nested('['))

    def test_single_close_bracket(self):
            # Test case: Single closing bracket. Should not be nested.
            # This specifically covers the path where char == ']' and state == 0 (initial state).
            self.assertFalse(is_nested(']'))

    def test_simple_non_nested_pair(self):
            # Test case: A simple non-nested pair "[]".
            # This specifically covers the path where char == ']' and state == 1 (after first '[').
            self.assertFalse(is_nested('[]'))

    def test_two_open_brackets_no_close(self):
            # Test case: Two opening brackets "[[". Should not be nested.
            # This covers the state transitions 0 -> 1 -> 2.
            self.assertFalse(is_nested('[['))

    def test_three_open_brackets_no_close(self):
            # Test case: Three opening brackets "[[[". Should not be nested.
            # This covers the implicit branch where char == '[' and state is already 2 (or 3).
            # Specifically, after processing "[[" (state becomes 2), another '[' keeps state at 2.
            self.assertFalse(is_nested('[[['))

    def test_open_open_close_open(self):
            # Test case: [[][ - tests a sequence that progresses through states, then hits an '['
            # when state is 3. This covers the implicit branch where char == '[' and state is 3.
            self.assertFalse(is_nested('[[]['))

    def test_two_non_nested_pairs(self):
            # Test case: [][], a sequence of two separate valid bracket pairs.
            # This progresses through states but never finds the final ']' in state 3.
            self.assertFalse(is_nested('[][]'))

    def test_nested_with_leading_and_trailing_noise(self):
            # Test case: `][[][]]` - A valid nested sequence `[[]]` exists within noise.
            # This ensures the state machine correctly identifies the nested pattern
            # even with preceding/succeeding non-relevant brackets.
            # This test exercises various state transitions including `char == ']'` when state is 0,
            # and `char == '['` when state is 1, and eventually `char == ']'` when state is 3 for success.
            self.assertTrue(is_nested('][[][]]'))

    def test_more_complex_nested_pattern(self):
            # Test case: `[[[[]]]]` - A more complex nested pattern that definitely contains `[[]]`.
            # This tests the ability to find the pattern amidst more brackets.
            self.assertTrue(is_nested('[[[[]]]]'))

    def test_interspersed_non_matching_brackets(self):
            # Test case: `[[]]][[` - contains a nested `[[]]` but also other brackets that don't contribute.
            # Ensures that once `True` is returned, the function exits immediately.
            self.assertTrue(is_nested('[[]]][['))
