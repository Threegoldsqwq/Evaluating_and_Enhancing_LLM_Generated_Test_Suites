import unittest

class TestSolution(unittest.TestCase):

    def test_example_1(self):
        # Example provided: sum of odd elements at even indices (0, 2, ...)
        # Indices: 0  1  2  3
        # Elements:5  8  7  1
        # Element at index 0 (5) is odd.
        # Element at index 2 (7) is odd.
        # Sum: 5 + 7 = 12
        self.assertEqual(solution([5, 8, 7, 1]), 12)

    def test_example_2_all_odd_even_indices(self):
        # Example provided: all elements are odd, all even indices (0, 2, 4) contain odd numbers
        # Indices: 0  1  2  3  4
        # Elements:3  3  3  3  3
        # Element at index 0 (3) is odd.
        # Element at index 2 (3) is odd.
        # Element at index 4 (3) is odd.
        # Sum: 3 + 3 + 3 = 9
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)

    def test_example_3_no_matches(self):
        # Example provided: no odd elements at even indices
        # Indices: 0   1   2   3
        # Elements:30  13  24  321
        # Element at index 0 (30) is even.
        # Element at index 2 (24) is even.
        # Sum: 0
        self.assertEqual(solution([30, 13, 24, 321]), 0)

    def test_single_odd_element(self):
        # A list with a single odd element at index 0 (which is an even position)
        self.assertEqual(solution([7]), 7)

    def test_single_even_element(self):
        # A list with a single even element at index 0
        self.assertEqual(solution([6]), 0)

    def test_mixed_positives_and_negatives(self):
        # Test with negative numbers, ensuring their odd/even parity is handled correctly
        # Indices:   0  1   2   3   4
        # Elements: -5  2  -7  10  -9
        # Index 0 (-5) is odd.
        # Index 2 (-7) is odd.
        # Index 4 (-9) is odd.
        # Sum: -5 + (-7) + (-9) = -21
        self.assertEqual(solution([-5, 2, -7, 10, -9]), -21)

    def test_large_numbers(self):
        # Test with large numbers
        # Indices:    0            1  2            3  4
        # Elements: 1000000001  2  1000000003  4  1000000005
        # Index 0 (1000000001) is odd.
        # Index 2 (1000000003) is odd.
        # Index 4 (1000000005) is odd.
        # Sum: 1000000001 + 1000000003 + 1000000005 = 3000000009
        self.assertEqual(solution([1000000001, 2, 1000000003, 4, 1000000005]), 3000000009)

    def test_all_even_numbers(self):
        # All elements are even, so no sum
        self.assertEqual(solution([2, 4, 6, 8, 10]), 0)

    def test_only_one_match(self):
        # Only one element satisfies both conditions
        # Indices:  0   1  2   3   4   5
        # Elements:10  5  20  30  41  50
        # Index 4 (41) is odd.
        # Sum: 41
        self.assertEqual(solution([10, 5, 20, 30, 41, 50]), 41)

    def test_with_zeros(self):
        # Zero is an even number.
        # Indices:  0  1  2  3  4
        # Elements: 0  1  3  0  5
        # Index 0 (0) is even.
        # Index 2 (3) is odd.
        # Index 4 (5) is odd.
        # Sum: 3 + 5 = 8
        self.assertEqual(solution([0, 1, 3, 0, 5]), 8)

if __name__ == '__main__':
    unittest.main()