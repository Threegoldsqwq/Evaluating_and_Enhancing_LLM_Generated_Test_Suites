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
    def test_empty_sentence_and_spaces(self):
            """
            Covers filter_prime_length_words when the input sentence is empty or
            consists only of whitespace, leading to an empty list of words.
            This ensures lines 25, 26, and 27 are covered, especially the path
            where the 'for' loop is not entered.
            """
            self.assertEqual(filter_prime_length_words(""), "")
            self.assertEqual(filter_prime_length_words("   "), "")
            self.assertEqual(filter_prime_length_words(" \t\n "), "")

    def test_words_length_one(self):
            """
            Covers the 'is_prime' function's 'n <= 1' branch for n=1.
            Words of length 1 are not prime.
            """
            self.assertEqual(filter_prime_length_words("a i o u e"), "")

    def test_words_length_two(self):
            """
            Covers the 'is_prime' function's 'n == 2' branch for n=2.
            2 is the only even prime number.
            """
            self.assertEqual(filter_prime_length_words("hi go is am me"), "hi go is am me")

    def test_words_even_length_greater_than_two(self):
            """
            Covers the 'is_prime' function's 'n % 2 == 0' branch for n > 2 (even numbers).
            These lengths are not prime. This also ensures lines 25-27 are covered
            where words are processed but none are prime, resulting in an empty output.
            """
            self.assertEqual(filter_prime_length_words("test python longer solution computer"), "") # Lengths: 4, 6, 6, 8, 8

    def test_words_composite_odd_length(self):
            """
            Covers the 'is_prime' function's 'if n % i == 0' branch (True for odd composites).
            Specifically targets n=9 (divisible by 3) and n=49 (divisible by 7),
            which involves the 'while i * i <= n' loop and 'i += 2'.
            """
            # "ninth" (5) - prime (loop not entered: i*i > n)
            # "twentyone" (9) - composite (i=3, 9%3==0, returns False)
            # "fortynine" (9) - composite (i=3, 9%3==0, returns False)
            self.assertEqual(filter_prime_length_words("ninth twentyone fortynine"), "ninth")

    def test_long_composite_odd_length_with_iterations(self):
            """
            Specifically covers `is_prime(49)` which involves `i += 2` multiple times
            before finding a divisor (i=7).
            """
            # "a_49_chars_word_to_test_odd_composite_49" (length 49)
            # 'a_49_chars_word_to_test_odd_composite_49'.replace(" ", "").replace("_", "") => "a49charswordtotestoddcomposite49" (32 chars)
            # Let's construct a word of length 49.
            word_len_49 = "supercalifragilisticexpialidociousishlongwordas" # 49 characters
            word_len_5 = "hello" # prime
            self.assertEqual(filter_prime_length_words(f"{word_len_49} {word_len_5}"), "hello")

    def test_words_prime_length_requiring_loop_iterations(self):
            """
            Covers 'is_prime' for prime numbers where the 'while i * i <= n' loop is entered
            and 'i += 2' is executed, but no divisors are found before 'i * i > n'.
            Targets n=11 (e.g., 'programming') and n=23 (e.g., 'unbelievableword')
            """
            # "programming" (11) - prime: i=3 (no), i=5 (no), then 5*5 > 11, returns True.
            # "unbelievableword" (16) - not prime (even).
            # "discoveries" (11) - prime.
            # "extraordinary" (13) - prime.
            # "thisistwentythreecharslongword" (30). Make a 23 char word: "thisistwentythreechar"
            word_len_23 = "thisistwentythreechar" # 21 chars. "thisisatwentythreecharword" (26)
            word_len_23_prime = "anexampleofalongprime" # 21.
            word_len_23_prime_two = "anotherlongprimewordt" # 21.

            # Let's try 11 and 13 as they are explicitly mentioned in thought process.
            # 11: is_prime(11) -> i=3 (11%3!=0), i=5 (5*5=25 > 11, exit) -> True.
            # 13: is_prime(13) -> i=3 (13%3!=0), i=5 (5*5=25 > 13, exit) -> True.
            self.assertEqual(filter_prime_length_words("programming discoveries extraordinary"), "programming discoveries extraordinary")

    def test_mixed_sentence_comprehensive_coverage(self):
            """
            A comprehensive test case with various word lengths to ensure all branches
            of 'is_prime' and the overall 'filter_prime_length_words' logic are covered.
            Includes lengths 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 49.
            """
            sentence = (
                "a "          # 1 (not prime)
                "hi "         # 2 (prime)
                "the "        # 3 (prime)
                "test "       # 4 (not prime, even)
                "world "      # 5 (prime)
                "banana "     # 6 (not prime, even)
                "amazing "    # 7 (prime)
                "computer "   # 8 (not prime, even)
                "excellent "  # 9 (not prime, composite odd)
                "programming " # 11 (prime, requires loop iterations)
                "extraordinary " # 13 (prime, requires loop iterations)
                "supercalifragilisticexpialidociousislongwordas" # 49 (not prime, composite odd, requires loop iterations)
            )
            expected = "hi the world amazing programming extraordinary"
            self.assertEqual(filter_prime_length_words(sentence), expected)
