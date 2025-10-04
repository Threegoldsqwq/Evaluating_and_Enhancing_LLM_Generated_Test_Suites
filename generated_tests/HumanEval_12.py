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
    def test_longest_empty_list(self):
            # Covers the 'if not strings:' branch returning None
            self.assertIsNone(longest([]))

    def test_longest_single_element(self):
            # Test case for a list with a single string
            self.assertEqual(longest(['single']), 'single')

    def test_longest_first_is_longest(self):
            # Test case where the first string is the longest
            self.assertEqual(longest(['applepie', 'banana', 'grape']), 'applepie')

    def test_longest_middle_is_longest(self):
            # Test case where a middle string is the longest
            self.assertEqual(longest(['short', 'mediumlength', 'small']), 'mediumlength')

    def test_longest_last_is_longest(self):
            # Test case where the last string is the longest
            self.assertEqual(longest(['one', 'two', 'threefourfive']), 'threefourfive')

    def test_longest_all_same_length(self):
            # Test case where all strings have the same length, verifies first one is returned
            self.assertEqual(longest(['cat', 'dog', 'cow']), 'cat')
            self.assertEqual(longest(['abc', 'def', 'ghi']), 'abc')

    def test_longest_ties_first_is_returned(self):
            # Test case with multiple strings having the same maximum length, verifies first one is returned
            self.assertEqual(longest(['hello', 'world', 'a', 'testt']), 'hello')
            self.assertEqual(longest(['longest', 'anotherlongest', 'short']), 'longest')
            self.assertEqual(longest(['ab', 'cd', 'efg', 'hij']), 'efg')

    def test_longest_with_empty_strings(self):
            # Test case including empty strings in the list
            self.assertEqual(longest(['', 'a', 'bb', 'ccc']), 'ccc')
            self.assertEqual(longest(['', '', '']), '') # All empty strings
            self.assertEqual(longest(['hello', '']), 'hello')

    def test_longest_with_unicode_strings(self):
            # Test with unicode characters to ensure length function works correctly
            self.assertEqual(longest(['你好', '世界', 'Python']), 'Python')
            self.assertEqual(longest(['short', '長長的字串']), '長長的字串')

    def test_longest_with_mixed_lengths(self):
            # Comprehensive test with various lengths and positions
            self.assertEqual(longest(['a', 'bbb', 'cc', 'dddd', 'e']), 'dddd')
            self.assertEqual(longest(['a_long_string', 'short', 'another_very_long_string']), 'another_very_long_string')
