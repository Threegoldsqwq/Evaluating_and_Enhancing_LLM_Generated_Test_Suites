import unittest

# Assume split_words function is defined elsewhere as per the problem description.
# For demonstration purposes, a dummy function might look like this,
# but it's not part of the requested output.
#
# def split_words(text: str):
#     if any(c.isspace() for c in text):
#         return text.split()
#     elif ',' in text:
#         return text.split(',')
#     else:
#         count = 0
#         for char in text:
#             if 'a' <= char <= 'z':
#                 order = ord(char) - ord('a')
#                 if order % 2 != 0: # Check if order is odd (1, 3, 5, ...)
#                     count += 1
#         return count

class TestSplitWords(unittest.TestCase):

    def test_1_split_on_whitespace_basic(self):
        """Test case from example: basic split on a single space."""
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_2_split_on_whitespace_multiple_types_and_trimming(self):
        """Test with various whitespace characters (space, tab, newline) and leading/trailing whitespace."""
        self.assertEqual(split_words("  Python\tis\nfun  "), ["Python", "is", "fun"])

    def test_3_split_on_comma_basic(self):
        """Test case from example: basic split on a single comma (no whitespace)."""
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_4_split_on_comma_multiple_and_empty_strings(self):
        """Test with multiple commas, including leading/trailing, which should produce empty strings."""
        self.assertEqual(split_words(",apple,banana,orange,"), ["", "apple", "banana", "orange", ""])

    def test_5_whitespace_precedence_over_comma(self):
        """Test a string with both whitespace and commas. Whitespace split should take precedence."""
        self.assertEqual(split_words("first,item second,item"), ["first,item", "second,item"])

    def test_6_count_odd_ordered_letters_all_odd(self):
        """Test counting odd-ordered lowercase letters with only odd-ordered ones."""
        # b=1, d=3, f=5, h=7, j=9, l=11 -> 6
        self.assertEqual(split_words("bdfhjl"), 6)

    def test_7_count_odd_ordered_letters_all_even(self):
        """Test counting odd-ordered lowercase letters with only even-ordered ones."""
        # a=0, c=2, e=4, g=6, i=8, k=10 -> 0
        self.assertEqual(split_words("acegik"), 0)

    def test_8_count_odd_ordered_letters_mixed_case_and_numbers(self):
            """Test counting odd-ordered letters with mixed case, numbers, and symbols."""
            # Only 'b', 'd', 'f', 'h' are lowercase and odd-ordered.
            # b=1, d=3, f=5, h=7 -> 4
            # The original input "aB1cD2eF3gH4" contained only even-ordered lowercase letters ('a', 'c', 'e', 'g')
            # and uppercase versions of 'B', 'D', 'F', 'H', which are ignored.
            # To test for a count of 4, the input must contain 'b', 'd', 'f', 'h' as lowercase.
            self.assertEqual(split_words("ab1cd2ef3gh4"), 4)
    def test_9_count_odd_ordered_letters_empty_string(self):
        """Test an empty string (should result in 0 as no conditions are met)."""
        self.assertEqual(split_words(""), 0)

    def test_10_count_odd_ordered_letters_only_symbols_numbers(self):
        """Test a string with only non-alphabetic characters (no whitespace, no commas)."""
        self.assertEqual(split_words("!@#$%^&*()12345"), 0)
    def test_split_words_whitespace_only_empty_list(self):
            # Covers Rule 1: Text with only whitespace, leading/trailing/multiple, should result in an empty list.
            self.assertEqual(self.solution.split_words("   "), [])
            self.assertEqual(self.solution.split_words("\t\n "), [])

    def test_split_words_whitespace_mixed_types(self):
            # Covers Rule 1: Text with various types of whitespace (tab, newline, space).
            self.assertEqual(self.solution.split_words("hello\tworld"), ['hello', 'world'])
            self.assertEqual(self.solution.split_words("first\nline\rsecond"), ['first', 'line', 'second'])
            self.assertEqual(self.solution.split_words("  leading  middle\t trailing "), ['leading', 'middle', 'trailing'])

    def test_split_words_comma_edge_cases(self):
            # Covers Rule 2: Comma splitting with leading/trailing/consecutive commas.
            self.assertEqual(self.solution.split_words(",a,b,"), ['', 'a', 'b', ''])
            self.assertEqual(self.solution.split_words("a,,b"), ['a', '', 'b'])
            self.assertEqual(self.solution.split_words(",,,"), ['', '', '', ''])

    def test_split_words_comma_with_internal_non_split_whitespace(self):
            # Covers Rule 2: Ensures Rule 1 is correctly skipped, and internal whitespace in segments is preserved
            # when splitting by commas.
            self.assertEqual(self.solution.split_words("apple, banana cake, cherry"), ['apple', ' banana cake', ' cherry'])

    def test_split_words_empty_string_odd_order_count(self):
            # Covers Rule 3: Empty string, a critical edge case for loop-based logic.
            self.assertEqual(self.solution.split_words(""), 0)

    def test_split_words_odd_order_count_only_even_letters(self):
            # Covers Rule 3: String with only even-ordered lowercase letters ('a' through 'z').
            self.assertEqual(self.solution.split_words("acegikmoqsuwy"), 0) # a=0, c=2, e=4, etc. are all even

    def test_split_words_odd_order_count_only_odd_letters(self):
            # Covers Rule 3: String with only odd-ordered lowercase letters ('a' through 'z').
            self.assertEqual(self.solution.split_words("bdfhjlnprtvxz"), 12) # b=1, d=3, f=5, etc. are all odd

    def test_split_words_odd_order_count_mixed_chars(self):
            # Covers Rule 3: Mix of lowercase, uppercase, numbers, and symbols (no spaces or commas).
            # Should only count lowercase letters with odd order.
            self.assertEqual(self.solution.split_words("aBcD1eF!g@H"), 3) # 'b'(1), 'd'(3), 'f'(5) are odd
            self.assertEqual(self.solution.split_words("PYTHONisGREAT123"), 4) # 'p'(15), 't'(19), 'h'(7), 'n'(13) are odd

    def test_split_words_odd_order_count_no_letters(self):
            # Covers Rule 3: String with no alphabetic characters.
            self.assertEqual(self.solution.split_words("123!@#$%^&*()[]{}"), 0)

    def test_split_words_odd_order_count_single_char_cases(self):
            # Covers Rule 3: Single character tests for odd/even order, uppercase, numbers, and symbols.
            self.assertEqual(self.solution.split_words("a"), 0) # 'a'=0 (even)
            self.assertEqual(self.solution.split_words("b"), 1) # 'b'=1 (odd)
            self.assertEqual(self.solution.split_words("z"), 1) # 'z'=25 (odd)
            self.assertEqual(self.solution.split_words("y"), 0) # 'y'=24 (even)
            self.assertEqual(self.solution.split_words("A"), 0) # Uppercase is skipped
            self.assertEqual(self.solution.split_words("1"), 0) # Number is skipped
            self.assertEqual(self.solution.split_words("!"), 0) # Symbol is skipped
