import unittest

class TestHowManyTimes(unittest.TestCase):

    def test_empty_original_string(self):
        """Test with an empty original string."""
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_empty_substring(self):
        """Test with an empty substring. (Commonly returns 0, as Python's str.count doesn't support it)."""
        self.assertEqual(how_many_times('abcde', ''), 0)

    def test_substring_not_found(self):
        """Test when the substring is not present in the original string."""
        self.assertEqual(how_many_times('hello world', 'xyz'), 0)

    def test_substring_found_once(self):
        """Test when the substring appears exactly once without overlap."""
        self.assertEqual(how_many_times('programming', 'gram'), 1)

    def test_problem_example_single_char_multiple_times(self):
        """Test with a single character substring, as per problem example 'aaa', 'a'."""
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_problem_example_overlapping(self):
        """Test with overlapping occurrences, as per problem example 'aaaa', 'aa'."""
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_highly_overlapping_same_char(self):
        """Test with a highly overlapping substring of repeated characters."""
        self.assertEqual(how_many_times('ooooo', 'ooo'), 3) # 'ooo..', '.ooo.', '..ooo'

    def test_substring_is_entire_string(self):
        """Test when the substring is identical to the original string."""
        self.assertEqual(how_many_times('python', 'python'), 1)

    def test_substring_longer_than_original(self):
        """Test when the substring is longer than the original string."""
        self.assertEqual(how_many_times('short', 'longer_substring'), 0)

    def test_complex_overlapping_with_mixed_chars(self):
        """Test with a more complex string and overlapping occurrences."""
        self.assertEqual(how_many_times('mississippi', 'iss'), 2) # 'm'iss'issippi', 'miss'iss'ippi'