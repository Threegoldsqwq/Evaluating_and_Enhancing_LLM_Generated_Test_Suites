import unittest

# Assume the function 'filter_prime_length_words' exists and is imported or defined elsewhere.
# For example:
# def filter_prime_length_words(sentence: str) -> str:
#     # Helper to check if a number is prime
#     def is_prime(n):
#         if n < 2:
#             return False
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     words = sentence.split()
#     result_words = []
#     for word in words:
#         if is_prime(len(word)):
#             result_words.append(word)
#
#     return " ".join(result_words)


class TestFilterPrimeLengthWords(unittest.TestCase):

    def test_example_1(self):
        # Input sentence: "This is a test"
        # Word lengths: "This" (4), "is" (2), "a" (1), "test" (4)
        # Prime lengths: 2 ("is")
        sentence = "This is a test"
        expected_output = "is"
        self.assertEqual(filter_prime_length_words(sentence), expected_output)

    def test_example_2(self):
        # Input sentence: "lets go for swimming"
        # Word lengths: "lets" (4), "go" (2), "for" (3), "swimming" (8)
        # Prime lengths: 2 ("go"), 3 ("for")
        sentence = "lets go for swimming"
        expected_output = "go for"
        self.assertEqual(filter_prime_length_words(sentence), expected_output)

    def test_all_prime_length_words(self):
        # All words have prime lengths: "is" (2), "and" (3), "for" (3), "three" (5), "seven" (5)
        sentence = "is and for three seven"
        expected_output = "is and for three seven"
        self.assertEqual(filter_prime_length_words(sentence), expected_output)

    def test_no_prime_length_words(self):
        # No words have prime lengths: "that" (4), "four" (4), "word" (4), "nine" (4), "twelve" (6), "twenty" (6), "four" (4)
        sentence = "that four word nine twelve twenty four"
        expected_output = ""
        self.assertEqual(filter_prime_length_words(sentence), expected_output)

    def test_single_word_prime_length(self):
        # Single word, length 5 (prime)
        sentence = "three"
        expected_output = "three"
        self.assertEqual(filter_prime_length_words(sentence), expected_output)

    def test_single_word_non_prime_length(self):
        # Single word, length 4 (not prime)
        sentence = "four"
        expected_output = ""
        self.assertEqual(filter_prime_length_words(sentence), expected_output)

    def test_mixed_starting_with_prime(self):
        # Mixed lengths, starting with prime: "hello" (5), "this" (4), "is" (2), "a" (1), "long" (4), "sentence" (8), "of" (2), "words" (5)
        # Primes: "hello", "is", "of", "words"
        sentence = "hello this is a long sentence of words"
        expected_output = "hello is of words"
        self.assertEqual(filter_prime_length_words(sentence), expected_output)

    def test_mixed_ending_with_non_prime(self):
        # Mixed lengths, ending with non-prime: "is" (2), "a" (1), "test" (4), "of" (2), "long" (4), "words" (5), "like" (4), "this" (4)
        # Primes: "is", "of", "words"
        sentence = "is a test of long words like this"
        expected_output = "is of words"
        self.assertEqual(filter_prime_length_words(sentence), expected_output)

    def test_all_words_length_one(self):
        # All words are "a", length 1 (not prime)
        sentence = "a a a a a"
        expected_output = ""
        self.assertEqual(filter_prime_length_words(sentence), expected_output)

    def test_longer_prime_lengths_and_mixed(self):
        # Includes longer prime lengths like 7:
        # "its" (3), "a" (1), "really" (6), "long" (4), "string" (6), "with" (4),
        # "words" (5), "that" (4), "have" (4), "many" (4), "letters" (7)
        # Primes: "its", "words", "letters"
        sentence = "its a really long string with words that have many letters"
        expected_output = "its words letters"
        self.assertEqual(filter_prime_length_words(sentence), expected_output)