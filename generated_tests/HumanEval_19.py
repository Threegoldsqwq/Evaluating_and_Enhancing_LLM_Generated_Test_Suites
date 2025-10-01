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