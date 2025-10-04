import unittest

# Assume the 'tribonacci' function exists and is imported or defined elsewhere.
# It should take a non-negative integer `n` and return a list of the first
# `n + 1` numbers of the Tribonacci sequence, i.e., [tri(0), tri(1), ..., tri(n)].

# Based on the problem description and example:
# tri(0) = 1 (implicit from example tri(3) = [1, 3, 2, 8])
# tri(1) = 3 (given)
# tri(n) = 1 + n // 2, if n is even (assuming integer division based on examples)
# tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
#
# For odd n, the recurrence tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1) can be simplified:
# If n is odd, then n-1 and n+1 are even.
# tri(n-1) = 1 + (n-1)//2
# tri(n+1) = 1 + (n+1)//2
# Substituting these:
# tri(n) = (1 + (n-1)//2) + tri(n-2) + (1 + (n+1)//2)
# tri(n) = 2 + (n-1)//2 + (n+1)//2 + tri(n-2)
# tri(n) = 2 + ( (n-1) + (n+1) ) // 2 + tri(n-2)
# tri(n) = 2 + (2n) // 2 + tri(n-2)
# tri(n) = 2 + n + tri(n-2) (for odd n)

# Let's calculate the first few terms:
# tri(0) = 1
# tri(1) = 3
# tri(2) = 1 + 2 // 2 = 1 + 1 = 2
# tri(3) = 3 + 2 + tri(1) = 5 + 3 = 8
# tri(4) = 1 + 4 // 2 = 1 + 2 = 3
# tri(5) = 5 + 2 + tri(3) = 7 + 8 = 15
# tri(6) = 1 + 6 // 2 = 1 + 3 = 4
# tri(7) = 7 + 2 + tri(5) = 9 + 15 = 24
# tri(8) = 1 + 8 // 2 = 1 + 4 = 5
# tri(9) = 9 + 2 + tri(7) = 11 + 24 = 35

class TestTribonacci(unittest.TestCase):

    def test_n_is_zero(self):
        # Smallest non-negative input
        self.assertEqual(tribonacci(0), [1])

    def test_n_is_one(self):
        # Includes the first explicit base case tri(1)
        self.assertEqual(tribonacci(1), [1, 3])

    def test_n_is_two(self):
        # First even number, uses tri(n) = 1 + n // 2
        self.assertEqual(tribonacci(2), [1, 3, 2])

    def test_n_is_three_example(self):
        # Example from the problem description
        # tri(3) = 3 + 2 + tri(1) = 5 + 3 = 8
        self.assertEqual(tribonacci(3), [1, 3, 2, 8])

    def test_n_is_four(self):
        # Another even number
        # tri(4) = 1 + 4 // 2 = 3
        self.assertEqual(tribonacci(4), [1, 3, 2, 8, 3])

    def test_n_is_five(self):
        # Another odd number, depends on tri(3)
        # tri(5) = 5 + 2 + tri(3) = 7 + 8 = 15
        self.assertEqual(tribonacci(5), [1, 3, 2, 8, 3, 15])

    def test_n_is_six(self):
        # Another even number
        # tri(6) = 1 + 6 // 2 = 4
        self.assertEqual(tribonacci(6), [1, 3, 2, 8, 3, 15, 4])

    def test_n_is_seven(self):
        # Another odd number, depends on tri(5)
        # tri(7) = 7 + 2 + tri(5) = 9 + 15 = 24
        self.assertEqual(tribonacci(7), [1, 3, 2, 8, 3, 15, 4, 24])

    def test_n_is_eight(self):
        # Another even number
        # tri(8) = 1 + 8 // 2 = 5
        self.assertEqual(tribonacci(8), [1, 3, 2, 8, 3, 15, 4, 24, 5])

    def test_n_is_nine(self):
        # Another odd number, depends on tri(7)
        # tri(9) = 9 + 2 + tri(7) = 11 + 24 = 35
        self.assertEqual(tribonacci(9), [1, 3, 2, 8, 3, 15, 4, 24, 5, 35])

# To run these tests, you would typically include:
# if __name__ == '__main__':
#     unittest.main()