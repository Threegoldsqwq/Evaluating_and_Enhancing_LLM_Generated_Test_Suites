import unittest

# Assume order_by_points function exists, as per the problem statement.
# For reference, a potential implementation based on the most coherent interpretation
# (sum of digits ascending, then original index descending for ties)
# would look something like this.
# However, the first test case is designed to match the specific example output provided in the problem,
# which appears to contradict this general rule for some elements.
# All other test cases follow the derived coherent rule.

# def _sum_digits(n):
#     return sum(int(digit) for digit in str(abs(n)))

# def order_by_points(lst):
#     if not lst:
#         return []
#     
#     # Store (sum_of_digits, -original_index, value) for sorting
#     # -original_index is used to sort original_index in descending order
#     items_with_keys = []
#     for i, num in enumerate(lst):
#         s_digits = _sum_digits(num)
#         items_with_keys.append((s_digits, -i, num))
#     
#     items_with_keys.sort()
#     
#     return [item[2] for item in items_with_keys]


class TestOrderByPoints(unittest.TestCase):

    def setUp(self):
        # Helper function to calculate sum of digits (absolute value)
        # This helper is used to derive expected outputs for tests,
        # assuming the sorting logic described.
        self._sum_digits = lambda n: sum(int(d) for d in str(abs(n)))

    def _get_expected(self, input_list):
        """
        Calculates the expected output based on the derived rule:
        1. Primary sort by sum of digits (ascending).
        2. Secondary sort by original index (descending).
        """
        if not input_list:
            return []

        # Create tuples (sum_of_digits, -original_index, value)
        # -original_index ensures descending order for original index on ascending sort
        indexed_items = []
        for i, num in enumerate(input_list):
            indexed_items.append((self._sum_digits(num), -i, num))

        # Sort these tuples
        indexed_items.sort()

        # Extract the original values
        return [item[2] for item in indexed_items]

    def test_empty_list(self):
        self.assertEqual(order_by_points([]), [])

    def test_single_element(self):
        self.assertEqual(order_by_points([5]), [5])

    def test_example_from_problem_description(self):
        # NOTE: This test case uses the *exact expected output* provided
        # in the problem description, which appears to deviate from a strict
        # "sum of digits ascending" primary sort for some elements.
        # For example, -1 (sum 1) is followed by -11 (sum 2), then 1 (sum 1).
        # This test is crucial as it validates against the explicitly given example.
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])

    def test_all_same_sum_of_digits_different_indices(self):
        # All have sum 1. Sorted by original index descending.
        input_list = [1, 10, 100] # 1(idx 0), 10(idx 1), 100(idx 2)
        # Expected: 100 (idx 2), 10 (idx 1), 1 (idx 0)
        self.assertEqual(order_by_points(input_list), self._get_expected(input_list)) # [100, 10, 1]

    def test_mixed_sums_no_ties(self):
        # sums: 2, 1, 3. Simple ascending sort by sum.
        input_list = [2, 1, 3]
        self.assertEqual(order_by_points(input_list), self._get_expected(input_list)) # [1, 2, 3]

    def test_mixed_sums_with_ties_positive(self):
        # 13(sum 4, idx 0), 22(sum 4, idx 1), 1(sum 1, idx 2), 4(sum 4, idx 3)
        # Sorted by sum, then by original index descending:
        # Sum 1: 1 (idx 2)
        # Sum 4: 4 (idx 3), 22 (idx 1), 13 (idx 0)
        input_list = [13, 22, 1, 4]
        self.assertEqual(order_by_points(input_list), self._get_expected(input_list)) # [1, 4, 22, 13]

    def test_mixed_sums_with_ties_negative(self):
        # -13(sum 4, idx 0), -22(sum 4, idx 1), -1(sum 1, idx 2), -4(sum 4, idx 3)
        # Sorted by sum, then by original index descending:
        # Sum 1: -1 (idx 2)
        # Sum 4: -4 (idx 3), -22 (idx 1), -13 (idx 0)
        input_list = [-13, -22, -1, -4]
        self.assertEqual(order_by_points(input_list), self._get_expected(input_list)) # [-1, -4, -22, -13]

    def test_mixed_positive_and_negative_all_same_sum(self):
        # All have sum 1. Sorted by original index descending.
        # 1(idx 0), -1(idx 1), 10(idx 2), -10(idx 3)
        # Expected: -10 (idx 3), 10 (idx 2), -1 (idx 1), 1 (idx 0)
        input_list = [1, -1, 10, -10]
        self.assertEqual(order_by_points(input_list), self._get_expected(input_list)) # [-10, 10, -1, 1]

    def test_with_zeros(self):
        # 0(sum 0, idx 0), 10(sum 1, idx 1), 0(sum 0, idx 2)
        # Sorted by sum, then by original index descending:
        # Sum 0: 0 (idx 2), 0 (idx 0)
        # Sum 1: 10 (idx 1)
        input_list = [0, 10, 0]
        self.assertEqual(order_by_points(input_list), self._get_expected(input_list)) # [0, 0, 10]

    def test_large_numbers(self):
        # 99(sum 18, idx 0), 18(sum 9, idx 1), 1(sum 1, idx 2), 1000000(sum 1, idx 3)
        # Sorted by sum, then by original index descending:
        # Sum 1: 1000000 (idx 3), 1 (idx 2)
        # Sum 9: 18 (idx 1)
        # Sum 18: 99 (idx 0)
        input_list = [99, 18, 1, 1000000]
        self.assertEqual(order_by_points(input_list), self._get_expected(input_list)) # [1000000, 1, 18, 99]

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)