import unittest

class TestIsBored(unittest.TestCase):

    def test_01_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_02_no_boredom_simple(self):
        self.assertEqual(is_bored("Hello world. How are you?"), 0)

    def test_03_one_boredom_at_end(self):
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather."), 1)

    def test_04_one_boredom_at_beginning(self):
        self.assertEqual(is_bored("I am happy. What about you?"), 1)

    def test_05_multiple_boredoms(self):
        self.assertEqual(is_bored("I am tired. You are not. I want to sleep now! I feel great."), 3)

    def test_06_i_not_at_sentence_start(self):
        # "I" appearing in the middle of a sentence should not count.
        self.assertEqual(is_bored("He said, I am going. Hi, I am fine. Indeed!"), 0)

    def test_07_different_delimiters_and_multiple_boredoms(self):
        self.assertEqual(is_bored("I think it's great! Are you enjoying it? I certainly am."), 2)

    def test_08_word_starts_with_i_but_is_not_i(self):
        # Test cases like "Indeed", "I'm", "Ice" should not be counted as "I".
        self.assertEqual(is_bored("Indeed, it is! I'm not sure. I am happy."), 1)

    def test_09_spaces_around_delimiters_and_sentences(self):
        # Leading/trailing spaces for sentences and around delimiters.
        self.assertEqual(is_bored("  Hello there.   I am good!  Are you?   I'm okay.  "), 1)

    def test_10_only_one_delimiter_at_end_with_boredom(self):
        self.assertEqual(is_bored("What a day! I am thrilled."), 1)