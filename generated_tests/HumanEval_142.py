import unittest

# Assume the function 'process_list_and_sum' exists and is imported or defined elsewhere.
# For example:
# def process_list_and_sum(lst):
#     modified_list = list(lst) # Create a mutable copy
#     for i in range(len(modified_list)):
#         if i % 3 == 0:
#             modified_list[i] = modified_list[i] ** 2
#         elif i % 4 == 0: # This implies i % 3 != 0 due to 'elif'
#             modified_list[i] = modified_list[i] ** 3
#     return sum(modified_list)


class TestProcessListAndSum(unittest.TestCase):

    def test_empty_list(self):
        """
        Test case 1: Verify the function handles an empty list correctly.
        Expected: Sum of an empty list is 0.
        """
        lst = []
        expected_output = 0
        self.assertEqual(process_list_and_sum(lst), expected_output)

    def test_small_list_example_one(self):
        """
        Test case 2: Verify a small list where only index 0 is a multiple of 3.
        (From problem description: For lst = [1,2,3] the output should be 6)
        """
        lst = [1, 2, 3]
        # Index 0 (1): 1^2 = 1
        # Index 1 (2): no change = 2
        # Index 2 (3): no change = 3
        # Sum: 1 + 2 + 3 = 6
        expected_output = 6
        self.assertEqual(process_list_and_sum(lst), expected_output)

    def test_small_list_example_two_negatives(self):
        """
        Test case 3: Verify a list with negative numbers, covering all modification rules.
        (From problem description: For lst = [-1,-5,2,-1,-5] the output should be -126)
        """
        lst = [-1, -5, 2, -1, -5]
        # Index 0 (-1): (-1)^2 = 1
        # Index 1 (-5): no change = -5
        # Index 2 (2): no change = 2
        # Index 3 (-1): (-1)^2 = 1
        # Index 4 (-5): (-5)^3 = -125 (4 is multiple of 4, not 3)
        # Sum: 1 + (-5) + 2 + 1 + (-125) = -126
        expected_output = -126
        self.assertEqual(process_list_and_sum(lst), expected_output)

    def test_list_with_zeros_and_mixed_signs(self):
        """
        Test case 4: Verify behavior with zeros and a mix of positive and negative numbers.
        Covers index 0, 3, and 4 rules.
        """
        lst = [0, 1, -1, 3, -2, 5]
        # Index 0 (0): 0^2 = 0
        # Index 1 (1): no change = 1
        # Index 2 (-1): no change = -1
        # Index 3 (3): 3^2 = 9
        # Index 4 (-2): (-2)^3 = -8
        # Index 5 (5): no change = 5
        # Sum: 0 + 1 + (-1) + 9 + (-8) + 5 = 6
        expected_output = 6
        self.assertEqual(process_list_and_sum(lst), expected_output)

    def test_longer_list_all_ones(self):
        """
        Test case 5: Verify with a longer list where all elements are 1.
        This checks that 1^2 and 1^3 still result in 1, and covers a range of indices up to 12.
        """
        lst = [1] * 13  # List of 13 ones, indices 0 to 12
        # All operations (square, cube, no change) on 1 result in 1.
        # Sum: 13 * 1 = 13
        expected_output = 13
        self.assertEqual(process_list_and_sum(lst), expected_output)

    def test_longer_list_varied_numbers_up_to_index_12(self):
        """
        Test case 6: Verify with a longer list of varied numbers, specifically checking index 12.
        Index 12 is a multiple of both 3 and 4, ensuring the precedence rule (multiple of 3) is applied.
        """
        lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # Length 13
        # Index 0 (2): 2^2 = 4
        # Index 1 (3): 3
        # Index 2 (4): 4
        # Index 3 (5): 5^2 = 25
        # Index 4 (6): 6^3 = 216
        # Index 5 (7): 7
        # Index 6 (8): 8^2 = 64
        # Index 7 (9): 9
        # Index 8 (10): 10^3 = 1000
        # Index 9 (11): 11^2 = 121
        # Index 10 (12): 12
        # Index 11 (13): 13
        # Index 12 (14): 14^2 = 196 (12 % 3 == 0, so squared)
        # Sum: 4 + 3 + 4 + 25 + 216 + 7 + 64 + 9 + 1000 + 121 + 12 + 13 + 196 = 1674
        expected_output = 1674
        self.assertEqual(process_list_and_sum(lst), expected_output)

    def test_list_emphasizing_multiple_of_three_and_four_indices(self):
        """
        Test case 7: Verify a list specifically crafted to test multiples of 3,
        multiples of 4 (not 3), and untouched indices.
        """
        lst = [10, 20, 30, 40, 50, 60, 70]  # Length 7
        # Index 0 (10): 10^2 = 100
        # Index 1 (20): no change = 20
        # Index 2 (30): no change = 30
        # Index 3 (40): 40^2 = 160
        # Index 4 (50): 50^3 = 125000 (4 is multiple of 4, not 3)
        # Index 5 (60): no change = 60
        # Index 6 (70): 70^2 = 4900
        # Sum: 100 + 20 + 30 + 160 + 125000 + 60 + 4900 = 130270
        expected_output = 130270
        self.assertEqual(process_list_and_sum(lst), expected_output)

    def test_list_emphasizing_multiple_of_four_not_three_indices(self):
        """
        Test case 8: Verify a list where elements at indices which are multiples of 4 (but not 3)
        are prominent, along with other index types.
        """
        lst = [1, 1, 1, 1, 2, 1, 1, 1, 2]  # Length 9
        # Index 0 (1): 1^2 = 1
        # Index 1 (1): no change = 1
        # Index 2 (1): no change = 1
        # Index 3 (1): 1^2 = 1
        # Index 4 (2): 2^3 = 8 (4 is multiple of 4, not 3)
        # Index 5 (1): no change = 1
        # Index 6 (1): 1^2 = 1
        # Index 7 (1): no change = 1
        # Index 8 (2): 2^3 = 8 (8 is multiple of 4, not 3)
        # Sum: 1 + 1 + 1 + 1 + 8 + 1 + 1 + 1 + 8 = 23
        expected_output = 23
        self.assertEqual(process_list_and_sum(lst), expected_output)

    def test_list_with_large_numbers(self):
        """
        Test case 9: Verify handling of large integer values to ensure no overflow issues (Python handles large ints).
        """
        lst = [100, 200, 300, 400, 500]
        # Index 0 (100): 100^2 = 10000
        # Index 1 (200): no change = 200
        # Index 2 (300): no change = 300
        # Index 3 (400): 400^2 = 160000
        # Index 4 (500): 500^3 = 125000000
        # Sum: 10000 + 200 + 300 + 160000 + 125000000 = 125170500
        expected_output = 125170500
        self.assertEqual(process_list_and_sum(lst), expected_output)

    def test_mixed_signs_and_zero_values_specific_sum(self):
        """
        Test case 10: A comprehensive test with a mix of positive, negative, and zero values,
        designed to result in a specific sum, exercising all conditions.
        """
        lst = [2, -1, 0, -2, -1, 5, -3, 2, -2]  # Length 9
        # Index 0 (2): 2^2 = 4
        # Index 1 (-1): no change = -1
        # Index 2 (0): no change = 0
        # Index 3 (-2): (-2)^2 = 4
        # Index 4 (-1): (-1)^3 = -1 (4 is multiple of 4, not 3)
        # Index 5 (5): no change = 5
        # Index 6 (-3): (-3)^2 = 9
        # Index 7 (2): no change = 2
        # Index 8 (-2): (-2)^3 = -8 (8 is multiple of 4, not 3)
        # Sum: 4 + (-1) + 0 + 4 + (-1) + 5 + 9 + 2 + (-8) = 14
        expected_output = 14
        self.assertEqual(process_list_and_sum(lst), expected_output)