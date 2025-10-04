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

    def test_empty_list(self):
            """Test with an empty input list."""
            self.assertEqual(list_sort([]), [])

    def test_all_odd_length_strings(self):
            """Test with a list containing only odd-length strings."""
            self.assertEqual(list_sort(["a", "bbb", "hello", "world"]), [])

    def test_all_even_length_strings_no_duplicates(self):
            """Test with a list containing only even-length strings, no duplicates, sorted by length then alphabetically."""
            input_list = ["code", "list", "python", "four"]
            # "code" (4), "four" (4), "list" (4), "python" (6)
            expected_output = ["code", "four", "list", "python"]
            self.assertEqual(list_sort(input_list), expected_output)

    def test_mixed_odd_even_length_strings_complex(self):
            """Test with a complex mix of odd and even-length strings, ensuring correct filtering and sorting."""
            input_list = ["apple", "banana", "kiwi", "grape", "orange", "test", "car", "door"]
            # Even length strings:
            # "kiwi" (4)
            # "test" (4)
            # "door" (4)
            # "banana" (6)
            # "orange" (6)
            # Sorted first by length, then alphabetically for same length:
            # ["door", "kiwi", "test", "banana", "orange"]
            expected_output = ["door", "kiwi", "test", "banana", "orange"]
            self.assertEqual(list_sort(input_list), expected_output)

    def test_strings_of_same_even_length_alphabetical_sort(self):
            """Test secondary alphabetical sorting for strings of the same even length."""
            input_list = ["kite", "code", "list", "bear", "lion", "duck"]
            # All have length 4 (even).
            # Sorted alphabetically:
            # ["bear", "code", "duck", "kite", "lion", "list"]
            self.assertEqual(list_sort(input_list), ["bear", "code", "duck", "kite", "lion", "list"])

    def test_duplicate_even_length_strings(self):
            """Test with duplicate even-length strings, verifying they are retained and sorted correctly."""
            input_list = ["test", "duplicate", "a", "test", "bb", "cc", "bb"]
            # Filtered even-length strings:
            # "test" (4), "test" (4), "bb" (2), "cc" (2), "bb" (2)
            # Sorted:
            # ["bb", "bb", "cc", "test", "test"]
            self.assertEqual(list_sort(input_list), ["bb", "bb", "cc", "test", "test"])

    def test_single_even_length_string(self):
            """Test with a single even-length string."""
            self.assertEqual(list_sort(["python"]), ["python"])

    def test_single_odd_length_string(self):
            """Test with a single odd-length string."""
            self.assertEqual(list_sort(["cat"]), [])

    def test_list_with_empty_string(self):
            """Test with an empty string (length 0, which is even) and other strings."""
            input_list = ["", "a", "bb", "ccc", "dddd", "eeeee", "ffffff"]
            # Filtered even-length strings:
            # "" (0), "bb" (2), "dddd" (4), "ffffff" (6)
            # Sorted:
            # ["", "bb", "dddd", "ffffff"]
            self.assertEqual(list_sort(input_list), ["", "bb", "dddd", "ffffff"])

    def test_case_sensitivity_in_sorting(self):
            """Test that alphabetical sorting is case-sensitive, affecting order of same-length strings."""
            input_list = ["AA", "bb", "BB", "aa", "Cc", "cc"]
            # All len 2, even. Python's string comparison is case-sensitive: 'A' < 'B', 'a' < 'b', 'A' < 'a'.
            # Expected order: "AA", "BB", "Cc", "aa", "bb", "cc"
            self.assertEqual(list_sort(input_list), ["AA", "BB", "Cc", "aa", "bb", "cc"])

    def test_very_long_strings_mixed_lengths(self):
            """Test with very long strings and a mix of lengths to ensure scalability and correctness."""
            input_list = [
                "thisisalongstringwitheighteenscharacters", # 40 - even
                "anotherlongstringwithtwentyfourchars", # 36 - even
                "short",      # 5 - odd
                "medium",     # 6 - even
                "a" * 10,     # 10 - even
                "b" * 9,      # 9 - odd
                "c" * 10      # 10 - even
            ]
            # Filtered even-length strings:
            # "medium" (6)
            # "a" * 10 (10)
            # "c" * 10 (10)
            # "anotherlongstringwithtwentyfourchars" (36)
            # "thisisalongstringwitheighteenscharacters" (40)
            # Sorted:
            expected_output = [
                "medium",
                "a" * 10,
                "c" * 10,
                "anotherlongstringwithtwentyfourchars",
                "thisisalongstringwitheighteenscharacters"
            ]
            self.assertEqual(list_sort(input_list), expected_output)

    def test_unicode_strings(self):
            """Test with unicode strings to ensure proper handling in filtering and sorting."""
            input_list = ["café", "résumé", "déjà", "python", "你好"]
            # Lengths: "café" (4), "résumé" (6), "déjà" (4), "python" (6), "你好" (2)
            # Even: "你好" (2), "café" (4), "déjà" (4), "résumé" (6), "python" (6)
            # Sorted: "你好", "café", "déjà", "python", "résumé"
            self.assertEqual(list_sort(input_list), ["你好", "café", "déjà", "python", "résumé"])
if __name__ == '__main__':
    # This placeholder function must be defined or imported for the tests to run.
    # In a real scenario, you would have your actual 'list_sort' function here or imported.
    # def list_sort(string_list):
    #     filtered_list = [s for s in string_list if len(s) % 2 == 0]
    #     # Sort primarily by length, secondarily by alphabetical order
    #     filtered_list.sort(key=lambda x: (len(x), x))
    #     return filtered_list

    unittest.main(argv=['first-arg-is-ignored'], exit=False)