import unittest

class TestCompare(unittest.TestCase):

    def test_example_1(self):
        scores = [1, 2, 3, 4, 5, 1]
        guesses = [1, 2, 3, 4, 2, -2]
        expected = [0, 0, 0, 0, 3, 3]
        self.assertEqual(compare(scores, guesses), expected)

    def test_example_2(self):
        scores = [0, 5, 0, 0, 0, 4]
        guesses = [4, 1, 1, 0, 0, -2]
        expected = [4, 4, 1, 0, 0, 6]
        self.assertEqual(compare(scores, guesses), expected)

    def test_all_correct_guesses(self):
        scores = [10, 20, 30]
        guesses = [10, 20, 30]
        expected = [0, 0, 0]
        self.assertEqual(compare(scores, guesses), expected)

    def test_all_incorrect_positive_differences(self):
        scores = [5, 10, 15]
        guesses = [1, 2, 3]
        expected = [4, 8, 12]
        self.assertEqual(compare(scores, guesses), expected)

    def test_all_incorrect_with_negative_guesses(self):
        scores = [10, 20, 30]
        guesses = [-5, -10, -15]
        expected = [15, 30, 45]
        self.assertEqual(compare(scores, guesses), expected)

    def test_mixed_scores_and_guesses_with_negatives_and_zeros(self):
        scores = [0, -5, 10, -2, 7]
        guesses = [0, -10, 5, 3, 7]
        expected = [0, 5, 5, 5, 0]
        self.assertEqual(compare(scores, guesses), expected)

    def test_single_match_correct(self):
        scores = [100]
        guesses = [100]
        expected = [0]
        self.assertEqual(compare(scores, guesses), expected)

    def test_single_match_incorrect(self):
        scores = [50]
        guesses = [0]
        expected = [50]
        self.assertEqual(compare(scores, guesses), expected)

    def test_large_numbers_and_differences(self):
        scores = [1000, -500, 250, 0, -100]
        guesses = [900, -600, 300, 10, -50]
        expected = [100, 100, 50, 10, 50]
        self.assertEqual(compare(scores, guesses), expected)

    def test_zero_scores_and_mixed_guesses(self):
        scores = [0, 0, 0, 0, 0]
        guesses = [-1, 1, 0, 5, -5]
        expected = [1, 1, 0, 5, 5]
        self.assertEqual(compare(scores, guesses), expected)

# Assume the 'compare' function is defined elsewhere for these tests to run.
# For example:
# def compare(scores, guesses):
#     result = []
#     for i in range(len(scores)):
#         result.append(abs(scores[i] - guesses[i]))
#     return result