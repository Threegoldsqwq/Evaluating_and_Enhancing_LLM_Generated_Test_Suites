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

    def test_empty_list(self):
            """Test with an empty list, ensuring total_sum remains 0."""
            self.assertEqual(solution([]), 0)

    def test_no_qualifying_numbers_even_index_even_num(self):
            """
            Test case where numbers at even indices are even.
            This covers the branch where 'index % 2 == 0' is true,
            but 'num % 2 != 0' is false, preventing addition to total_sum.
            """
            self.assertEqual(solution([2, 10, 4, 12]), 0)
            self.assertEqual(solution([0, 1, 2, 3, 4]), 0)

    def test_no_qualifying_numbers_odd_index(self):
            """
            Test case where numbers that could be odd are exclusively at odd indices.
            This covers the branch where 'index % 2 == 0' is false,
            skipping the inner condition check.
            """
            self.assertEqual(solution([2, 3, 4, 5, 6, 7]), 0)
            self.assertEqual(solution([10, 11, 12, 13]), 0)

    def test_single_qualifying_number(self):
            """
            Test a list containing only one number that meets both criteria.
            Ensures 'total_sum += num' is executed for a single instance.
            """
            self.assertEqual(solution([1, 2]), 1)
            self.assertEqual(solution([0, 0, 5, 0]), 5)

    def test_mixed_qualifying_and_non_qualifying(self):
            """
            Test a comprehensive scenario with a mix of qualifying and non-qualifying numbers
            to ensure all branches and conditions are correctly handled throughout the loop.
            """
            # (index=0, num=1) -> add 1
            # (index=1, num=2) -> skip (odd index)
            # (index=2, num=3) -> add 3
            # (index=3, num=4) -> skip (odd index)
            # (index=4, num=5) -> add 5
            # (index=5, num=6) -> skip (odd index)
            # (index=6, num=7) -> add 7
            self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7]), 1 + 3 + 5 + 7) # Expected: 16
            self.assertEqual(solution([10, 11, 1, 13, 3, 15, 20, 21, 5]), 1 + 3 + 5)

    def test_negative_numbers(self):
            """
            Test with negative numbers, including cases where the sum should be negative.
            """
            # (index=0, num=-1) -> add -1
            # (index=1, num=-2) -> skip (odd index)
            # (index=2, num=-3) -> add -3
            # (index=3, num=-4) -> skip (odd index)
            # (index=4, num=-5) -> add -5
            self.assertEqual(solution([-1, -2, -3, -4, -5]), -1 + -3 + -5) # Expected: -9
            self.assertEqual(solution([-2, -1, -4, -3, -6]), 0) # No qualifying numbers

    def test_large_numbers(self):
            """Test with larger numbers to ensure correct summation."""
            self.assertEqual(solution([101, 200, 303, 400, 505]), 101 + 303 + 505) # Expected: 909
if __name__ == '__main__':
    unittest.main()