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
    def test_basic_functionality_and_coverage(self):
            # This test ensures lines 1 (import re) and 3 (function definition) are executed
            # by calling the function with various fundamental cases.
            self.assertEqual(is_bored(""), 0)
            self.assertEqual(is_bored("Hello world."), 0)
            self.assertEqual(is_bored("I am bored."), 1)
            self.assertEqual(is_bored("I am bored. You are not. I am sad."), 2)
            self.assertEqual(is_bored("You are happy. I am glad."), 1)

    def test_empty_sentence_parts_branch(self):
            # Targets the `if not cleaned_sentence:` branch (line 25)
            # by creating scenarios where re.split produces empty strings or strings of only whitespace.
            self.assertEqual(is_bored("I am here!!! I am happy."), 2)  # Multiple '!' delimiters
            self.assertEqual(is_bored("Hello..World. I am fine."), 1)   # Multiple '.' delimiters
            self.assertEqual(is_bored("I. . I."), 2)                      # Spaces between delimiters
            self.assertEqual(is_bored("Hi.?!I am here."), 1)             # Mixed delimiters
            self.assertEqual(is_bored("!."), 0)                           # Text of only delimiters

    def test_whitespace_and_strip_functionality(self):
            # Verifies correct handling of leading/trailing whitespace around sentences.
            self.assertEqual(is_bored(" I am here."), 1)
            self.assertEqual(is_bored("I am here.  I am happy."), 2)
            self.assertEqual(is_bored("I am here . I am happy."), 2) # Space before delimiter
            self.assertEqual(is_bored("  I am bored."), 1)
            self.assertEqual(is_bored("I am great.   "), 1) # Trailing spaces after delimiter

    def test_case_sensitivity_and_word_position(self):
            # Ensures 'I' is case-sensitive and must be the very first word.
            self.assertEqual(is_bored("i am not bored."), 0)
            self.assertEqual(is_bored("Hello, I am here."), 0)
            self.assertEqual(is_bored("I am, you are."), 1) # 'I' followed by punctuation
            self.assertEqual(is_bored("I! Am! Bored!"), 1) # Only first 'I' counts due to case and position

    def test_no_sentence_delimiters(self):
            # Tests text inputs that do not contain any of the defined sentence delimiters.
            # In such cases, re.split treats the entire string as a single 'sentence part'.
            self.assertEqual(is_bored("I am here today"), 1)
            self.assertEqual(is_bored("Hello there I am here"), 0)
            self.assertEqual(is_bored("I am"), 1)
            self.assertEqual(is_bored("This is a test"), 0)

    def test_mixed_and_edge_delimiters(self):
            # Tests various combinations of delimiters and text ending with delimiters.
            self.assertEqual(is_bored("I like pizza! I like sushi? I like pasta."), 3)
            self.assertEqual(is_bored("Who am I? I am you! I am me."), 2)
            self.assertEqual(is_bored("I am here."), 1) # Ends with a delimiter
            self.assertEqual(is_bored("I!"), 1) # Shortest 'I' sentence ending with delimiter
            self.assertEqual(is_bored("."), 0) # Only a delimiter
            self.assertEqual(is_bored("?!"), 0) # Only multiple delimiters
