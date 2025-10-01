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