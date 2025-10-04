import unittest

# Assume filter_by_substring function is defined elsewhere, e.g.:
# def filter_by_substring(strings, substring):
#     return [s for s in strings if substring in s]

class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_no_matches(self):
        self.assertEqual(filter_by_substring(['bcd', 'def', 'ghi'], 'a'), [])

    def test_all_matches(self):
        self.assertEqual(filter_by_substring(['apple', 'banana', 'apricot'], 'a'), ['apple', 'banana', 'apricot'])

    def test_some_matches(self):
        self.assertEqual(filter_by_substring(['cat', 'dog', 'elephant', 'mouse'], 'o'), ['dog', 'mouse'])

    def test_empty_substring(self):
        # An empty string is considered a substring of every string
        self.assertEqual(filter_by_substring(['one', 'two', 'three'], ''), ['one', 'two', 'three'])

    def test_case_sensitivity(self):
        # The function `filter_by_substring` performs a case-sensitive search.
        # 'a' (lowercase) is not present in 'Apple'.
        # 'a' (lowercase) is present in 'banana'.
        # 'a' (lowercase) is present in 'Orange'.
        # Therefore, the expected output should include 'banana' and 'Orange'.
        self.assertEqual(filter_by_substring(['Apple', 'banana', 'Orange'], 'a'), ['banana', 'Orange'])
    def test_substring_at_beginning(self):
        self.assertEqual(filter_by_substring(['apple', 'apricot', 'banana'], 'ap'), ['apple', 'apricot'])

    def test_substring_at_end(self):
        self.assertEqual(filter_by_substring(['running', 'jumping', 'walking'], 'ing'), ['running', 'jumping', 'walking'])

    def test_substring_in_middle(self):
        self.assertEqual(filter_by_substring(['keyboard', 'mousepad', 'monitor'], 'oar'), ['keyboard'])

    def test_list_with_duplicates(self):
        self.assertEqual(filter_by_substring(['test', 'another test', 'test', 'final'], 'test'), ['test', 'another test', 'test'])

    def test_case_sensitivity(self):
            # Test that the filtering is case-sensitive
            self.assertEqual(self.solution(['Apple', 'apple', 'banana'], 'apple'), ['apple'])
            self.assertEqual(self.solution(['Hello', 'World'], 'hello'), [])
            self.assertEqual(self.solution(['hello', 'world'], 'WORLD'), [])

    def test_substring_as_suffix(self):
            # Test when the substring appears at the end of a string
            self.assertEqual(self.solution(['testing', 'baking', 'running'], 'ing'), ['testing', 'baking', 'running'])
            self.assertEqual(self.solution(['cat', 'dog', 'rat'], 'at'), ['cat', 'rat'])

    def test_substring_appearing_multiple_times_in_string(self):
            # Test when the substring appears multiple times within a single string
            self.assertEqual(self.solution(['ababab', 'acac'], 'aba'), ['ababab'])
            self.assertEqual(self.solution(['mississippi', 'pipi'], 'iss'), ['mississippi'])
            self.assertEqual(self.solution(['aaaaa', 'bbbbb'], 'aa'), ['aaaaa'])

    def test_list_with_empty_strings_and_non_empty_substring(self):
            # Test cases where the input list contains empty strings and the substring is not empty
            self.assertEqual(self.solution(['', 'test', '', 'another'], 'test'), ['test'])
            self.assertEqual(self.solution(['', 'a', '', 'b'], 'a'), ['a'])
            self.assertEqual(self.solution(['', 'a', '', 'b'], 'x'), []) # No match

    def test_single_element_list(self):
            # Test with a list containing only one element, both matching and not matching
            self.assertEqual(self.solution(['unique'], 'uni'), ['unique'])
            self.assertEqual(self.solution(['unique'], 'xyz'), [])

    def test_strings_with_special_characters(self):
            # Test with strings and substrings containing special characters
            self.assertEqual(self.solution(['foo-bar', 'baz_qux'], '-'), ['foo-bar'])
            self.assertEqual(self.solution(['hello@world.com', 'test.com'], '.com'), ['hello@world.com', 'test.com'])
            self.assertEqual(self.solution(['123', '456'], '2'), ['123'])
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)