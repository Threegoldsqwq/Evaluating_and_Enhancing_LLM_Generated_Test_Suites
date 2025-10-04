import unittest

class TestSmallestChange(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(smallest_change([]), 0)

    def test_single_element_array(self):
        self.assertEqual(smallest_change([5]), 0)

    def test_already_palindromic_even_length(self):
        self.assertEqual(smallest_change([1, 2, 2, 1]), 0)

    def test_already_palindromic_odd_length(self):
        # Example from problem description
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

    def test_one_change_even_length(self):
        # Only the first and last elements differ
        self.assertEqual(smallest_change([1, 2, 3, 3, 2, 5]), 1)

    def test_one_change_odd_length_example(self):
        # Example from problem description
        # [1, 2, 3, 4, 3, 2, 2] -> change last 2 to 1 (or first 1 to 2)
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)

    def test_multiple_changes_even_length_example(self):
        # Example from problem description
        # (1 vs 6), (2 vs 9), (3 vs 7), (5 vs 4) all differ -> 4 changes
        self.assertEqual(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]), 4)

    def test_multiple_changes_odd_length(self):
        # (1 vs 7), (2 vs 6), (3 vs 5) all differ -> 3 changes. Middle element (4) does not need change.
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7]), 3)

    def test_all_different_elements_even_length(self):
        # Every pair of symmetric elements differs
        # (10 vs 60), (20 vs 50), (30 vs 40) all differ -> 3 changes
        self.assertEqual(smallest_change([10, 20, 30, 40, 50, 60]), 3)

    def test_long_array_many_changes(self):
        # Length 15. Pairs are (1,15), (2,14), (3,13), (4,12), (5,11), (6,10), (7,9).
        # All 7 pairs need a change. Middle element (8) is fine.
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 7)
    def test_empty_array(self):
            # Covers the case where n=0. The loop range(0) is empty, changes remains 0.
            self.assertEqual(smallest_change([]), 0)

    def test_single_element_array(self):
            # Covers the case where n=1. The loop range(0) is empty, changes remains 0.
            self.assertEqual(smallest_change([5]), 0)

    def test_two_elements_no_change(self):
            # Covers n=2, where the elements are already a palindrome.
            # Exercises the 'if' condition being False.
            self.assertEqual(smallest_change([1, 1]), 0)

    def test_two_elements_one_change(self):
            # Covers n=2, where one change is needed.
            # Exercises the 'if' condition being True.
            self.assertEqual(smallest_change([1, 2]), 1)

    def test_odd_length_already_palindrome(self):
            # Covers an odd-length array that is already a palindrome.
            # Ensures the 'if' condition is False for all relevant pairs.
            self.assertEqual(smallest_change([1, 2, 1]), 0)
            self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

    def test_even_length_already_palindrome(self):
            # Covers an even-length array that is already a palindrome.
            # Ensures the 'if' condition is False for all relevant pairs.
            self.assertEqual(smallest_change([1, 2, 2, 1]), 0)
            self.assertEqual(smallest_change([5, 4, 3, 3, 4, 5]), 0)

    def test_odd_length_multiple_changes(self):
            # Covers an odd-length array needing multiple changes.
            # Exercises the 'if' condition being True multiple times.
            self.assertEqual(smallest_change([1, 2, 3, 4, 5]), 2) # arr[0]!=arr[4], arr[1]!=arr[3]
            self.assertEqual(smallest_change([10, 20, 30, 40, 50, 60, 70]), 3) # 10!=70, 20!=60, 30!=50

    def test_even_length_multiple_changes(self):
            # Covers an even-length array needing multiple changes.
            # Exercises the 'if' condition being True multiple times.
            self.assertEqual(smallest_change([1, 2, 3, 4]), 2) # arr[0]!=arr[3], arr[1]!=arr[2]
            self.assertEqual(smallest_change([10, 20, 30, 40, 50, 60]), 3) # 10!=60, 20!=50, 30!=40

    def test_mixed_changes_even_length(self):
            # Covers an even-length array with a mix of matching and differing pairs.
            # Ensures both true and false branches of the 'if' condition are taken.
            self.assertEqual(smallest_change([1, 2, 3, 2, 5, 1]), 1) # arr[0]==arr[5], arr[1]==arr[3], arr[2]!=arr[4] (3!=5)
            self.assertEqual(smallest_change([1, 2, 3, 4, 2, 1]), 1) # arr[0]==arr[5], arr[1]==arr[4], arr[2]!=arr[3] (3!=4)

    def test_mixed_changes_odd_length(self):
            # Covers an odd-length array with a mix of matching and differing pairs.
            # Ensures both true and false branches of the 'if' condition are taken.
            self.assertEqual(smallest_change([1, 5, 3, 2, 1]), 1) # arr[0]==arr[4], arr[1]!=arr[3] (5!=2)
            self.assertEqual(smallest_change([7, 8, 9, 8, 10]), 1) # arr[0]!=arr[4] (7!=10), arr[1]==arr[3]

    def test_array_with_negative_numbers_and_zeros(self):
            # Ensures the function handles negative numbers and zeros correctly.
            self.assertEqual(smallest_change([0, -1, 0]), 0)
            self.assertEqual(smallest_change([-1, -2, -3, -2, -1]), 1) # -1==-1, -2==-2, -3 is middle
            self.assertEqual(smallest_change([-1, 0, 1, 0, -1]), 0)
            self.assertEqual(smallest_change([-5, -4, -3, -2]), 2)
