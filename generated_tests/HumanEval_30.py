import unittest

class TestGetPositive(unittest.TestCase):

    def test_mixed_numbers_example_1(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])

    def test_mixed_numbers_example_2(self):
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

    def test_all_positive_numbers(self):
        self.assertEqual(get_positive([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_negative_numbers(self):
        self.assertEqual(get_positive([-1, -2, -3, -4, -5]), [])

    def test_empty_list(self):
        self.assertEqual(get_positive([]), [])

    def test_with_zeros_present(self):
        # Zero is not a positive number
        self.assertEqual(get_positive([-1, 0, 2, 0, -3, 4]), [2, 4])

    def test_single_positive_number(self):
        self.assertEqual(get_positive([7]), [7])

    def test_single_negative_number(self):
        self.assertEqual(get_positive([-8]), [])

    def test_large_numbers_and_mixed_zeros(self):
        self.assertEqual(get_positive([1000000, -500000, 0, 2000000, -1]), [1000000, 2000000])

    def test_numbers_with_duplicates_and_zeros(self):
        self.assertEqual(get_positive([1, -1, 2, -2, 1, 0, 3, 3, -3, 0]), [1, 2, 1, 3, 3])
    def test_empty_list(self):
            self.assertEqual(self.solution.get_positive([]), [])

    def test_all_negative_numbers(self):
            self.assertEqual(self.solution.get_positive([-1, -2, -3, -100]), [])

    def test_all_zero_numbers(self):
            self.assertEqual(self.solution.get_positive([0, 0, 0, 0]), [])

    def test_all_positive_numbers(self):
            self.assertEqual(self.solution.get_positive([1, 2, 3, 100]), [1, 2, 3, 100])

    def test_single_positive_number(self):
            self.assertEqual(self.solution.get_positive([7]), [7])

    def test_single_negative_number(self):
            self.assertEqual(self.solution.get_positive([-7]), [])

    def test_single_zero_number(self):
            self.assertEqual(self.solution.get_positive([0]), [])

    def test_mixed_numbers_with_floats(self):
            self.assertEqual(self.solution.get_positive([-1.5, 2.3, -4.0, 5.7, 0.0, 6.1]), [2.3, 5.7, 6.1])
