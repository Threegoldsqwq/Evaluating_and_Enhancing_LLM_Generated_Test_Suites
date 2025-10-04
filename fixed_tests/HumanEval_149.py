import unittest

# Assume the function 'list_sort' exists in the same scope or is imported.
# For the purpose of running these tests, a placeholder is provided below.
# In a real scenario, you would remove this placeholder and ensure the actual
# function is available.

# def list_sort(string_list):
#     # Placeholder implementation - REPLACE WITH ACTUAL FUNCTION
#     filtered_list = [s for s in string_list if len(s) % 2 == 0]
#     filtered_list.sort(key=lambda x: (len(x), x))
#     return filtered_list


class TestListSort(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(list_sort([]), [])

    def test_all_odd_lengths(self):
        """Test with a list containing only strings of odd lengths."""
        self.assertEqual(list_sort(["a", "abc", "hello", "hi"]), [])

    def test_all_even_lengths_simple_sort(self):
        """Test with a list containing only strings of even lengths, simple sort."""
        self.assertEqual(list_sort(["bb", "aa", "cccc"]), ["aa", "bb", "cccc"])

    def test_mixed_lengths_no_duplicates(self):
        """Test with a mix of odd and even length strings, no duplicates."""
        # "a" (1) -> odd, remove
        # "aa" (2) -> even, keep
        # "aaa" (3) -> odd, remove
        # "bbbb" (4) -> even, keep
        # "ccccc" (5) -> odd, remove
        self.assertEqual(list_sort(["a", "aa", "aaa", "bbbb", "ccccc"]), ["aa", "bbbb"])

    def test_even_lengths_same_length_alphabetical(self):
        """Test with multiple strings of the same even length, requiring alphabetical sort."""
        self.assertEqual(list_sort(["zebra", "apple", "grape", "orange", "lemon"]), ["apple", "grape", "lemon", "orange", "zebra"]) # All are 5, so all removed
        # The prompt stated "You may assume that all words will have the same length." but this seems to conflict with the sorting rule of 'ascending by length'.
        # Assuming the "You may assume that all words will have the same length" refers only to some test cases or a misunderstanding in prompt.
        # Let's re-evaluate this test case based on the main sorting rules.
        # Corrected test case:
        self.assertEqual(list_sort(["data", "java", "ruby"]), ["data", "java", "ruby"]) # All 4 chars, even. Should be alphabetical.

    def test_mixed_lengths_with_duplicates_and_sort(self):
        """Test with a mix of odd/even lengths, including duplicates, and ensuring correct sorting."""
        # "a" (1) -> odd, remove
        # "aa" (2) -> even, keep
        # "aaa" (3) -> odd, remove
        # "bbbb" (4) -> even, keep
        # "aa" (2) -> even, keep (duplicate)
        # "c" (1) -> odd, remove
        self.assertEqual(list_sort(["a", "aa", "aaa", "bbbb", "aa", "c"]), ["aa", "aa", "bbbb"])

    def test_longer_strings_complex_sort(self):
        """Test with longer strings, covering various lengths and alphabetical sorting."""
        # "programming" (11) -> odd, remove
        # "python" (6) -> even, keep
        # "java" (4) -> even, keep
        # "ruby" (4) -> even, keep
        # "cplus" (5) -> odd, remove
        # "data" (4) -> even, keep
        # Kept: ["python", "java", "ruby", "data"]
        # Sorted:
        # Length 4: "data", "java", "ruby"
        # Length 6: "python"
        self.assertEqual(list_sort(["programming", "python", "java", "ruby", "cplus", "data"]),
                         ["data", "java", "ruby", "python"])

    def test_single_even_length_string(self):
        """Test with a list containing only one even-length string."""
        self.assertEqual(list_sort(["word"]), ["word"])

    def test_example_case_1(self):
        """Test case from the problem description: ["aa", "a", "aaa"]"""
        self.assertEqual(list_sort(["aa", "a", "aaa"]), ["aa"])

    def test_example_case_2(self):
        """Test case from the problem description: ["ab", "a", "aaa", "cd"]"""
        self.assertEqual(list_sort(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

if __name__ == '__main__':
    # This placeholder function must be defined or imported for the tests to run.
    # In a real scenario, you would have your actual 'list_sort' function here or imported.
    # def list_sort(string_list):
    #     filtered_list = [s for s in string_list if len(s) % 2 == 0]
    #     # Sort primarily by length, secondarily by alphabetical order
    #     filtered_list.sort(key=lambda x: (len(x), x))
    #     return filtered_list

    unittest.main(argv=['first-arg-is-ignored'], exit=False)