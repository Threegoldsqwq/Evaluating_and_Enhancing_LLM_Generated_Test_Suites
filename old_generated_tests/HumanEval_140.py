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