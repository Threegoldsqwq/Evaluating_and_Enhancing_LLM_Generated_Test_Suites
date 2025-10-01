import unittest

class TestIsHappy(unittest.TestCase):

    def test_empty_string(self):
        # Length is less than 3
        self.assertFalse(is_happy(""))

    def test_single_character_string(self):
        # Length is less than 3
        self.assertFalse(is_happy("a"))

    def test_two_character_string(self):
        # Length is less than 3
        self.assertFalse(is_happy("ab"))

    def test_three_distinct_characters(self):
        # Length is 3, all distinct
        self.assertTrue(is_happy("abc"))

    def test_three_repeated_first_last_characters(self):
        # Length is 3, 'a' and 'a' are not distinct
        self.assertFalse(is_happy("aba"))

    def test_three_repeated_last_two_characters(self):
        # Length is 3, 'b' and 'b' are not distinct
        self.assertFalse(is_happy("abb"))

    def test_longer_happy_string(self):
        # Length > 3, all consecutive 3 letters are distinct
        self.assertTrue(is_happy("abcd"))

    def test_longer_unhappy_string_at_beginning(self):
        # Length > 3, first three characters 'aab' are not distinct
        self.assertFalse(is_happy("aabb"))

    def test_longer_unhappy_string_at_middle(self):
        # Length > 3, middle characters 'bca' are fine, but 'ccd' are not distinct
        self.assertFalse(is_happy("abccde"))

    def test_longer_happy_string_complex(self):
        # Length > 3, all consecutive 3 letters are distinct, more complex pattern
        self.assertTrue(is_happy("xzyxw"))