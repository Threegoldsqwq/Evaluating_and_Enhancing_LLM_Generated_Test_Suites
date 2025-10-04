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
    def test_substring_longer_than_original(self):
            # Covers the case where len(substring) > len(original_string).
            # This causes the loop's range to be empty, thus the count remains 0.
            self.assertEqual(how_many_times("short", "much_longer_substring"), 0)
            self.assertEqual(how_many_times("a", "aa"), 0)
            self.assertEqual(how_many_times("abc", "abcdef"), 0)

    def test_single_character_strings(self):
            # Covers cases with very short strings (single character)
            # to ensure loop and slice logic handles minimal lengths correctly.
            self.assertEqual(how_many_times("a", "a"), 1)
            self.assertEqual(how_many_times("a", "b"), 0)
            self.assertEqual(how_many_times("b", "a"), 0)

    def test_substring_is_entire_original_string(self):
            # Specific case where the substring is exactly the original string.
            self.assertEqual(how_many_times("hello", "hello"), 1)
            self.assertEqual(how_many_times("world", "world"), 1)

    def test_multiple_non_overlapping_occurrences(self):
            # Ensures correct counting when substrings do not overlap but appear multiple times.
            self.assertEqual(how_many_times("ababab", "ab"), 3)
            self.assertEqual(how_many_times("testtesttest", "test"), 3)
            self.assertEqual(how_many_times("abcabcabc", "abc"), 3)

    def test_case_sensitivity(self):
            # Verifies that the substring search is case-sensitive.
            self.assertEqual(how_many_times("Hello World", "hello"), 0)
            self.assertEqual(how_many_times("Python", "python"), 0)
            self.assertEqual(how_many_times("PYTHON", "python"), 0)
            self.assertEqual(how_many_times("PYTHON", "PYT"), 1)

    def test_strings_with_special_characters_and_numbers(self):
            # Checks functionality with non-alphabetic characters and numbers.
            self.assertEqual(how_many_times("123123123", "123"), 3)
            self.assertEqual(how_many_times("!@#$%!@#$!", "!@#$"), 2)
            self.assertEqual(how_many_times("alpha-beta-gamma", "-"), 2)
            self.assertEqual(how_many_times("alpha-beta-gamma", "alpha-"), 1)

    def test_substring_not_present_with_similar_length(self):
            # Tests scenarios where a substring of comparable length exists,
            # but does not exactly match.
            self.assertEqual(how_many_times("apple", "aplle"), 0)
            self.assertEqual(how_many_times("banana", "banaa"), 0)
