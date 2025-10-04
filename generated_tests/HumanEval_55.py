import unittest

class TestFibonacci(unittest.TestCase):

    def test_fib_1(self):
        self.assertEqual(fib(1), 1)

    def test_fib_2(self):
        self.assertEqual(fib(2), 1)

    def test_fib_3(self):
        self.assertEqual(fib(3), 2)

    def test_fib_4(self):
        self.assertEqual(fib(4), 3)

    def test_fib_5(self):
        self.assertEqual(fib(5), 5)

    def test_fib_8(self):
        self.assertEqual(fib(8), 21)

    def test_fib_10(self):
        self.assertEqual(fib(10), 55)

    def test_fib_13(self):
        self.assertEqual(fib(13), 233)

    def test_fib_15(self):
        self.assertEqual(fib(15), 610)

    def test_fib_20(self):
        self.assertEqual(fib(20), 6765)
    def test_fib_one(self):
            # Ensures coverage for the 'n == 1' part of the elif condition (line 8).
            # This addresses potential partial coverage if only n=2 was tested, or vice-versa.
            self.assertEqual(self.fib_solution(1), 1)

    def test_fib_two(self):
            # Ensures coverage for the 'n == 2' part of the elif condition (line 8).
            # This addresses potential partial coverage, completing the 'or' branch.
            self.assertEqual(self.fib_solution(2), 1)

    def test_fib_three(self):
            # Covers the smallest 'n' that enters the iterative loop (n > 2).
            # This ensures the loop is entered at least once and the 'return b' statement (line 24) is hit.
            # It also ensures the function definition itself (line 1) is called.
            self.assertEqual(self.fib_solution(3), 2)

    def test_fib_small_positive_loop(self):
            # Covers another small positive 'n' to ensure loop logic works for more than one iteration.
            # Further ensures coverage for the loop and 'return b' (line 24).
            self.assertEqual(self.fib_solution(5), 5)

    def test_fib_zero(self):
            # Explicitly tests the n <= 0 condition for n = 0.
            # If this path wasn't fully covered, this ensures it is.
            self.assertEqual(self.fib_solution(0), 0)

    def test_fib_negative_number(self):
            # Explicitly tests the n <= 0 condition for a negative integer.
            # If this path wasn't fully covered, this ensures it is.
            self.assertEqual(self.fib_solution(-7), 0)
