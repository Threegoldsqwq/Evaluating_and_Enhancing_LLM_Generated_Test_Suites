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

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)