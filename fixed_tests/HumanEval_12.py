import unittest

# Assume the 'longest' function is defined elsewhere, e.g.:
# def longest(strings):
#     if not strings:
#         return None
#     
#     max_length = -1
#     longest_string = None
# 
#     for s in strings:
#         if len(s) > max_length:
#             max_length = len(s)
#             longest_string = s
#     return longest_string

class TestLongest(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list, should return None."""
        self.assertIsNone(longest([]))

    def test_single_string(self):
        """Test with a list containing a single string."""
        self.assertEqual(longest(['hello']), 'hello')

    def test_longest_at_end(self):
        """Test with the longest string being the last element."""
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_longest_at_beginning(self):
        """Test with the longest string being the first element."""
        self.assertEqual(longest(['longest_string', 'short', 'medium']), 'longest_string')

    def test_longest_in_middle(self):
        """Test with the longest string being in the middle."""
        self.assertEqual(longest(['one', 'longest_in_middle', 'two']), 'longest_in_middle')

    def test_all_same_length_first_wins(self):
        """Test where all strings have the same length, first one should be returned."""
        self.assertEqual(longest(['apple', 'grape', 'peach']), 'apple')

    def test_ties_amongst_longest_first_wins(self):
        """Test with multiple strings having the maximum length, the first one encountered should win."""
        self.assertEqual(longest(['a', 'bb', 'ccc', 'ddd', 'ee']), 'ccc')

    def test_with_empty_string_not_longest(self):
        """Test with an empty string present, but a non-empty string is the longest."""
        self.assertEqual(longest(['', 'a', 'longest_str']), 'longest_str')

    def test_only_empty_string(self):
        """Test with a list containing only an empty string."""
        self.assertEqual(longest(['']), '')

    def test_mixed_lengths_and_ties_at_end(self):
        """Test with a mix of lengths and a tie for the longest near the end."""
        self.assertEqual(longest(['x', 'yy', 'zzz', 'aaaa', 'bbbb', 'ccc']), 'aaaa')