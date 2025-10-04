import unittest

class TestFixSpaces(unittest.TestCase):

    def test_no_spaces(self):
        self.assertEqual(fix_spaces("Example"), "Example")

    def test_single_space(self):
        self.assertEqual(fix_spaces("Hello World"), "Hello_World")

    def test_multiple_single_spaces(self):
        self.assertEqual(fix_spaces("This is a test string"), "This_is_a_test_string")

    def test_two_consecutive_spaces_only(self):
        self.assertEqual(fix_spaces("  "), "__")

    def test_two_consecutive_spaces_mixed(self):
        self.assertEqual(fix_spaces("Start  Middle  End"), "Start__Middle__End")

    def test_three_consecutive_spaces_only(self):
        self.assertEqual(fix_spaces("   "), "-")

    def test_three_consecutive_spaces_mixed(self):
        self.assertEqual(fix_spaces("Alpha   Beta"), "Alpha-Beta")

    def test_more_than_three_consecutive_spaces(self):
        self.assertEqual(fix_spaces("Foo    Bar"), "Foo-Bar")
        self.assertEqual(fix_spaces("Foo     Bar"), "Foo-Bar") # 5 spaces

    def test_mixed_space_patterns(self):
        # Leading single, two consecutive, three consecutive, four consecutive, trailing single
        self.assertEqual(fix_spaces(" A  B   C    D "), "_A__B-C-D_")

    def test_empty_string(self):
        self.assertEqual(fix_spaces(""), "")
    def test_multiple_long_space_sequences(self):
            # Covers multiple occurrences of 3+ spaces being replaced by hyphens.
            # This targets the first re.sub's branch for multiple matches.
            self.assertEqual(fix_spaces("apple   banana    cherry"), "apple-banana-cherry")

    def test_leading_trailing_long_spaces(self):
            # Covers 3+ spaces at the beginning and end of the string.
            # This targets the first re.sub's branch for matches at string boundaries.
            # Also ensures remaining single/double spaces are handled by the second re.sub.
            self.assertEqual(fix_spaces("   start and end   "), "-start_and_end-")

    def test_only_long_spaces(self):
            # Covers cases where the entire string consists of 3 or more spaces.
            # This targets the first re.sub's branch for replacing the whole string.
            self.assertEqual(fix_spaces("     "), "-") # 5 spaces -> 1 hyphen
            self.assertEqual(fix_spaces("   "), "-")  # 3 spaces -> 1 hyphen

    def test_mixed_spaces_no_long_sequences(self):
            # Covers cases with only single and double spaces, ensuring the first re.sub
            # finds no matches (partial coverage for its 'no match' branch) and
            # the second re.sub correctly converts all remaining spaces.
            self.assertEqual(fix_spaces("one  two three"), "one__two_three")
            self.assertEqual(fix_spaces(" a  b   c"), "_a__b-c") # Mix with 3+
            self.assertEqual(fix_spaces("only single spaces here"), "only_single_spaces_here")

    def test_empty_string(self):
            # Edge case for an empty input string.
            # Ensures both re.sub calls handle an empty string gracefully without error
            # and result in an empty string.
            self.assertEqual(fix_spaces(""), "")

    def test_no_spaces(self):
            # Edge case for a string with no spaces at all.
            # Ensures both re.sub calls find no matches and the original string is returned.
            self.assertEqual(fix_spaces("nospaceshere"), "nospaceshere")
            self.assertEqual(fix_spaces("HelloWorld"), "HelloWorld")

    def test_only_single_and_double_spaces(self):
            # Ensures that only single and double spaces are present, so the first re.sub does nothing,
            # and the second re.sub correctly converts all single and double spaces into underscores.
            self.assertEqual(fix_spaces("  leading  and trailing   double spaces  "), "__leading__and_trailing-double_spaces__")
            self.assertEqual(fix_spaces("  one two   three  "), "__one_two-three__")
