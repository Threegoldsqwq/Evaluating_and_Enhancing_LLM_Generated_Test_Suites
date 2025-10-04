import unittest
from collections import Counter

# Assume the 'search' function is defined elsewhere, for example:
# def search(nums: list[int]) -> int:
#     counts = Counter(nums)
#     
#     max_valid_num = -1
#     
#     for num in sorted(counts.keys(), reverse=True): # Iterate from largest to smallest for efficiency
#         if num > 0 and counts[num] >= num:
#             # Since we are iterating in reverse, the first one we find will be the greatest
#             return num
#             
#     return -1

class TestSearchFunction(unittest.TestCase):

    def test_example_one(self):
        # Example 1: Basic case with multiple candidates, returns the greatest
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

    def test_example_two(self):
        # Example 2: Another basic case with multiple candidates, returns the greatest
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_example_three_no_solution(self):
        # Example 3: No number satisfies the condition, should return -1
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

    def test_single_number_satisfies(self):
        # Case: Only one type of number, and it satisfies the condition
        self.assertEqual(search([1, 1, 1, 1]), 1)

    def test_single_number_does_not_satisfy(self):
        # Case: Only one type of number, and it does not satisfy the condition
        self.assertEqual(search([5, 5, 5]), -1)

    def test_one_candidate_exists(self):
        # Case: Multiple numbers, but only one satisfies the condition
        self.assertEqual(search([7, 1, 1, 2, 3, 4, 5, 6]), 1)

    def test_largest_number_is_solution(self):
        # Case: The largest number in the list is the one that satisfies the condition and is the greatest valid
        self.assertEqual(search([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 2, 3]), 10)

    def test_all_numbers_satisfy(self):
        # Case: All numbers in the list satisfy the condition, return the greatest
        self.assertEqual(search([1, 1, 2, 2, 3, 3, 3]), 3)

    def test_unique_numbers_only_one_possible_solution(self):
        # Case: List contains unique numbers. Only 1 can satisfy the condition (frequency=1 >= value=1)
        self.assertEqual(search([1, 2, 3, 4, 5]), 1)

    def test_no_solution_all_unique_and_greater_than_one(self):
        # Case: List contains unique numbers all greater than 1, so no solution
        self.assertEqual(search([2, 3, 4, 5, 6]), -1)

    def test_no_qualifying_number_returns_minus_one(self):
            # Test cases where no number satisfies the frequency >= value condition.
            # This covers the path where max_qualifying_int remains -1.
            self.assertEqual(search([2, 1]), -1)  # {2:1} -> 1 < 2
            self.assertEqual(search([3, 3]), -1)  # {3:2} -> 2 < 3
            self.assertEqual(search([5, 5, 5]), -1)  # {5:3} -> 3 < 5
            self.assertEqual(search([10] * 9), -1) # {10:9} -> 9 < 10
            self.assertEqual(search([100] * 99), -1) # {100:99} -> 99 < 100

    def test_single_qualifying_number(self):
            # Test cases where only one type of number qualifies.
            self.assertEqual(search([1]), 1)  # {1:1} -> 1 >= 1
            self.assertEqual(search([1, 1, 1]), 1) # {1:3} -> 3 >= 1
            self.assertEqual(search([2, 2]), 2)  # {2:2} -> 2 >= 2
            self.assertEqual(search([5] * 5), 5) # {5:5} -> 5 >= 5

    def test_multiple_qualifying_numbers_selects_greatest(self):
            # Test cases with multiple numbers qualifying, ensuring the maximum is returned.
            self.assertEqual(search([1, 1, 2, 2]), 2)  # {1:2, 2:2}. Both qualify, 2 is greater.
            self.assertEqual(search([1, 1, 1, 3, 3, 3]), 3) # {1:3, 3:3}. Both qualify, 3 is greater.
            self.assertEqual(search([2, 2, 2, 1, 1, 1, 1]), 2) # {2:3, 1:4}. Both qualify, 2 is greater.
            self.assertEqual(search([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3]), 3)
            # {1:4 (qualifies), 2:2 (doesn't qualify), 3:6 (qualifies)}. Result: 3.

    def test_mixed_qualifying_and_non_qualifying_numbers(self):
            # Test cases with a mix of numbers, where some qualify and some do not.
            self.assertEqual(search([1, 1, 2]), 1) # {1:2 (qualifies), 2:1 (doesn't)}.
            self.assertEqual(search([1, 3, 3]), 1) # {1:1 (qualifies), 3:2 (doesn't)}.
            self.assertEqual(search([2, 2, 3, 3]), 2) # {2:2 (qualifies), 3:2 (doesn't)}.
            self.assertEqual(search([5, 5, 5, 5, 5, 10, 10, 10, 10]), 5)
            # {5:5 (qualifies), 10:4 (doesn't)}.

    def test_large_value_numbers(self):
            # Test with larger integer values.
            self.assertEqual(search([100] * 100), 100)
            self.assertEqual(search([99] * 100 + [100] * 99), 99) # 99 qualifies, 100 does not
            self.assertEqual(search([99] * 99 + [100] * 100), 100) # Both qualify, 100 is max
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)