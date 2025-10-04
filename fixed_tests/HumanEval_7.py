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

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)