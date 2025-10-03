import unittest

class TestGetOddCollatz(unittest.TestCase):

    def test_n_is_1(self):
        # Collatz sequence for 1 is [1], odd numbers: [1]
        self.assertEqual(get_odd_collatz(1), [1])

    def test_n_is_5(self):
        # Collatz sequence for 5 is [5, 16, 8, 4, 2, 1], odd numbers: [5, 1]
        self.assertEqual(get_odd_collatz(5), [1, 5])

    def test_n_is_6(self):
        # Collatz sequence for 6 is [6, 3, 10, 5, 16, 8, 4, 2, 1], odd numbers: [3, 5, 1]
        self.assertEqual(get_odd_collatz(6), [1, 3, 5])

    def test_n_is_2(self):
        # Collatz sequence for 2 is [2, 1], odd numbers: [1]
        self.assertEqual(get_odd_collatz(2), [1])

    def test_n_is_7(self):
        # Collatz sequence for 7 is [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        # Odd numbers: [7, 11, 17, 13, 5, 1]
        self.assertEqual(get_odd_collatz(7), [1, 5, 7, 11, 13, 17])

    def test_n_is_3(self):
        # Collatz sequence for 3 is [3, 10, 5, 16, 8, 4, 2, 1]
        # Odd numbers: [3, 5, 1]
        self.assertEqual(get_odd_collatz(3), [1, 3, 5])

    def test_n_is_9(self):
        # Collatz sequence for 9 is [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        # Odd numbers: [9, 7, 11, 17, 13, 5, 1]
        self.assertEqual(get_odd_collatz(9), [1, 5, 7, 9, 11, 13, 17])

    def test_n_is_10(self):
        # Collatz sequence for 10 is [10, 5, 16, 8, 4, 2, 1]
        # Odd numbers: [5, 1]
        self.assertEqual(get_odd_collatz(10), [1, 5])

    def test_n_is_13(self):
        # Collatz sequence for 13 is [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        # Odd numbers: [13, 5, 1]
        self.assertEqual(get_odd_collatz(13), [1, 5, 13])

    def test_n_is_small_even_number(self):
        # Test an even number that quickly becomes odd.
        # Collatz sequence for 4 is [4, 2, 1], odd numbers: [1]
        self.assertEqual(get_odd_collatz(4), [1])