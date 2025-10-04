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

    def test_empty_lists(self):
            """Test with empty scores and guesses lists."""
            scores = []
            guesses = []
            expected = []
            self.assertEqual(self.solution.compare(scores, guesses), expected)

    def test_all_correct_guesses(self):
            """Test a scenario where all guesses are correct."""
            scores = [10, 20, 30, 40]
            guesses = [10, 20, 30, 40]
            expected = [0, 0, 0, 0]
            self.assertEqual(self.solution.compare(scores, guesses), expected)

    def test_all_incorrect_guesses(self):
            """Test a scenario where all guesses are incorrect."""
            scores = [10, 20, 30]
            guesses = [15, 25, 35]
            expected = [5, 5, 5]
            self.assertEqual(self.solution.compare(scores, guesses), expected)

    def test_mixed_guesses(self):
            """Test a scenario with a mix of correct and incorrect guesses."""
            scores = [5, 10, 15, 20, 25]
            guesses = [5, 12, 15, 18, 30]
            expected = [0, 2, 0, 2, 5]
            self.assertEqual(self.solution.compare(scores, guesses), expected)

    def test_guesses_higher_than_scores(self):
            """Test when some guesses are higher than actual scores."""
            scores = [10, 5, 8]
            guesses = [12, 8, 10]
            expected = [2, 3, 2]
            self.assertEqual(self.solution.compare(scores, guesses), expected)

    def test_scores_higher_than_guesses(self):
            """Test when some scores are higher than actual guesses."""
            scores = [12, 8, 10]
            guesses = [10, 5, 8]
            expected = [2, 3, 2]
            self.assertEqual(self.solution.compare(scores, guesses), expected)

    def test_single_element_lists_match(self):
            """Test with single-element lists where guess matches score."""
            scores = [100]
            guesses = [100]
            expected = [0]
            self.assertEqual(self.solution.compare(scores, guesses), expected)

    def test_single_element_lists_mismatch(self):
            """Test with single-element lists where guess mismatches score."""
            scores = [100]
            guesses = [90]
            expected = [10]
            self.assertEqual(self.solution.compare(scores, guesses), expected)

    def test_with_negative_numbers(self):
            """Test with negative scores and guesses, ensuring absolute difference is correct."""
            scores = [-5, -10, 0, 5]
            guesses = [-5, -8, 2, 0]
            expected = [0, 2, 2, 5] # abs(-10 - -8) = abs(-2) = 2, abs(0 - 2) = abs(-2) = 2, abs(5 - 0) = 5
            self.assertEqual(self.solution.compare(scores, guesses), expected)

    def test_large_numbers(self):
            """Test with large integer values."""
            scores = [10**9, 2 * (10**9)]
            guesses = [10**9 + 1, 2 * (10**9)]
            expected = [1, 0]
            self.assertEqual(self.solution.compare(scores, guesses), expected)
# Assume the 'compare' function is defined elsewhere for these tests to run.
# For example:
# def compare(scores, guesses):
#     result = []
#     for i in range(len(scores)):
#         result.append(abs(scores[i] - guesses[i]))
#     return result