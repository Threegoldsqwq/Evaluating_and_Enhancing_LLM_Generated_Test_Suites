import unittest

# Assume the words_string function is defined elsewhere, e.g.:
# def words_string(s):
#     import re
#     # Split by one or more spaces or commas, and filter out empty strings
#     return [word for word in re.split(r'[ ,]+', s) if word]

class TestWordsString(unittest.TestCase):

    def test_basic_spaces(self):
        """Test with words separated by spaces only."""
        self.assertEqual(words_string("Hi my name is John"), ["Hi", "my", "name", "is", "John"])

    def test_basic_commas(self):
        """Test with words separated by commas only."""
        self.assertEqual(words_string("One,two,three"), ["One", "two", "three"])

    def test_mixed_delimiters(self):
        """Test with words separated by both spaces and commas."""
        self.assertEqual(words_string("Hello, world! How are you?"), ["Hello", "world!", "How", "are", "you?"])

    def test_leading_trailing_delimiters(self):
        """Test with leading, trailing, and multiple delimiters."""
        self.assertEqual(words_string(" , word1, word2 , "), ["word1", "word2"])

    def test_multiple_delimiters_between_words(self):
        """Test with multiple spaces and commas between words."""
        self.assertEqual(words_string("apple   banana,,orange"), ["apple", "banana", "orange"])

    def test_empty_string(self):
        """Test with an empty input string."""
        self.assertEqual(words_string(""), [])

    def test_single_word_no_delimiters(self):
        """Test with a single word and no delimiters."""
        self.assertEqual(words_string("Python"), ["Python"])

    def test_string_with_only_delimiters(self):
        """Test with a string containing only delimiters."""
        self.assertEqual(words_string(",  ,,"), [])

    def test_complex_sentence_varied_delimiters(self):
        """Test a more complex sentence with varied delimiter usage."""
        self.assertEqual(words_string("This,is a test, with, mixed   delimiters."),
                         ["This", "is", "a", "test", "with", "mixed", "delimiters."])

    def test_example_from_problem_description(self):
        """Test the exact example provided in the problem description."""
        self.assertEqual(words_string("One, two, three, four, five, six"),
                         ["One", "two", "three", "four", "five", "six"])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)