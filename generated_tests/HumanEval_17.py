import unittest

# Assume the parse_music function is defined elsewhere, e.g.:
# def parse_music(music_string: str) -> list[int]:
#     # Implementation details as described in the problem
#     pass

class TestParseMusic(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(parse_music(''), [])

    def test_single_whole_note(self):
        self.assertEqual(parse_music('o'), [4])

    def test_single_half_note(self):
        self.assertEqual(parse_music('o|'), [2])

    def test_single_quarter_note(self):
        self.assertEqual(parse_music('.|'), [1])

    def test_multiple_whole_notes(self):
        self.assertEqual(parse_music('o o o'), [4, 4, 4])

    def test_multiple_quarter_notes(self):
        self.assertEqual(parse_music('.| .| .| .| .|'), [1, 1, 1, 1, 1])

    def test_mixed_notes_simple(self):
        self.assertEqual(parse_music('o .| o|'), [4, 1, 2])

    def test_mixed_notes_medium(self):
        self.assertEqual(parse_music('o| .| o .| o| o'), [2, 1, 4, 1, 2, 4])

    def test_example_from_doc(self):
        # This is the example given in the problem description
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_long_mixed_sequence(self):
        self.assertEqual(parse_music('.| o o| .| o o| .| o o|'), [1, 4, 2, 1, 4, 2, 1, 4, 2])
    def test_unrecognized_notes(self):
            # Test case to cover line 58 (the 'else' branch for unrecognized notes)
            # Input contains an unrecognized note 'x'
            self.assertEqual(self.solution.parse_music('o x .|'), [4, 1])
            # Input contains only unrecognized notes
            self.assertEqual(self.solution.parse_music('x y z'), [])
            # Input contains an unrecognized note amidst valid ones at different positions
            self.assertEqual(self.solution.parse_music('.| UNKNOWN o|'), [1, 2])
            self.assertEqual(self.solution.parse_music('o| invalid .| o'), [2, 1, 4])

    def test_edge_cases_with_spaces(self):
            # Test with leading/trailing spaces and multiple spaces between notes
            self.assertEqual(self.solution.parse_music('  o   o|  .|   '), [4, 2, 1])
            self.assertEqual(self.solution.parse_music(' o '), [4])
            self.assertEqual(self.solution.parse_music('     '), []) # String with only spaces

    def test_empty_string_explicitly(self):
            # Explicitly test the empty string case (if not already thoroughly covered)
            # This covers the 'if not music_string:' branch
            self.assertEqual(self.solution.parse_music(''), [])
