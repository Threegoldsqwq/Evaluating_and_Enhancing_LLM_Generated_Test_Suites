import unittest

class TestSortNumbers(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')

    def test_already_sorted(self):
        self.assertEqual(sort_numbers('one two three'), 'one two three')

    def test_reverse_sorted(self):
        self.assertEqual(sort_numbers('nine seven five two'), 'two five seven nine')

    def test_single_number(self):
        self.assertEqual(sort_numbers('four'), 'four')

    def test_empty_string(self):
        self.assertEqual(sort_numbers(''), '')

    def test_with_duplicates(self):
        self.assertEqual(sort_numbers('two five two one'), 'one two two five')

    def test_all_same_number(self):
        self.assertEqual(sort_numbers('eight eight eight'), 'eight eight eight')

    def test_including_zero_and_nine(self):
        self.assertEqual(sort_numbers('nine zero five three'), 'zero three five nine')

    def test_all_numbers_zero_to_nine_shuffled(self):
        input_str = 'five two nine zero one eight four seven three six'
        expected_str = 'zero one two three four five six seven eight nine'
        self.assertEqual(sort_numbers(input_str), expected_str)

    def test_two_numbers(self):
        self.assertEqual(sort_numbers('seven one'), 'one seven')
    def test_already_sorted_numbers(self):
            # Test case for an input string that is already sorted
            self.assertEqual(self.solution.sort_numbers('one two three'), 'one two three')

    def test_reverse_sorted_numbers(self):
            # Test case for an input string that is reverse sorted
            self.assertEqual(self.solution.sort_numbers('three two one'), 'one two three')

    def test_numbers_with_duplicates(self):
            # Test case for an input string containing duplicate number words
            self.assertEqual(self.solution.sort_numbers('one three one two'), 'one one two three')

    def test_all_identical_numbers(self):
            # Test case for an input string where all number words are identical
            self.assertEqual(self.solution.sort_numbers('five five five'), 'five five five')

    def test_two_words_reverse_order(self):
            # Test case for a minimal two-word input in reverse order
            self.assertEqual(self.solution.sort_numbers('two one'), 'one two')

    def test_extreme_values_only(self):
            # Test case specifically using 'zero' and 'nine'
            self.assertEqual(self.solution.sort_numbers('nine zero'), 'zero nine')

    def test_mixed_duplicates_and_order(self):
            # Test case with a more complex mix of order and duplicates
            self.assertEqual(self.solution.sort_numbers('seven two zero seven four'), 'zero two four seven seven')
