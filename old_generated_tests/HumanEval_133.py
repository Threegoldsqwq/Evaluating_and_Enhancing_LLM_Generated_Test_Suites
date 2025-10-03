import unittest
import math

# Assume the function to be tested is named 'sum_of_squared_ceilings'.
# For the purpose of running these tests, a dummy implementation is provided here.
# In a real scenario, this would be imported from the module containing the actual function.
# def sum_of_squared_ceilings(lst):
#     """
#     Calculates the sum of squared numbers in the given list,
#     after rounding each element to the upper integer (Ceiling).
#     """
#     if not lst:
#         return 0

#     ceiled_numbers = [math.ceil(x) for x in lst]
#     squared_numbers = [int(x)**2 for x in ceiled_numbers] # Ensure integer before squaring
#     return sum(squared_numbers)


class TestSumOfSquaredCeilings(unittest.TestCase):

    def test_example_1(self):
        # Test case from the problem description: all positive integers
        self.assertEqual(sum_of_squared_ceilings([1, 2, 3]), 14) # ceil([1,2,3]) -> [1,2,3], sq -> [1,4,9], sum -> 14

    def test_example_2(self):
        # Test case from the problem description: all positive integers
        self.assertEqual(sum_of_squared_ceilings([1, 4, 9]), 98) # ceil([1,4,9]) -> [1,4,9], sq -> [1,16,81], sum -> 98

    def test_example_3(self):
        # Test case from the problem description: all positive integers
        self.assertEqual(sum_of_squared_ceilings([1, 3, 5, 7]), 84) # ceil([1,3,5,7]) -> [1,3,5,7], sq -> [1,9,25,49], sum -> 84

    def test_example_4(self):
        # Test case from the problem description: positive floats and zero, requiring ceiling
        # 1.4 -> 2, 4.2 -> 5, 0 -> 0
        # 2^2 + 5^2 + 0^2 = 4 + 25 + 0 = 29
        self.assertEqual(sum_of_squared_ceilings([1.4, 4.2, 0]), 29)

    def test_example_5(self):
        # Test case from the problem description: mixed negative float, positive integers
        # -2.4 -> -2, 1 -> 1, 1 -> 1
        # (-2)^2 + 1^2 + 1^2 = 4 + 1 + 1 = 6
        self.assertEqual(sum_of_squared_ceilings([-2.4, 1, 1]), 6)

    def test_empty_list(self):
        # Test case for an empty list, sum should be 0
        self.assertEqual(sum_of_squared_ceilings([]), 0)

    def test_all_negative_floats_rounding_up_to_zero(self):
        # Test case with negative floats, some rounding up to 0
        # -3.7 -> -3, -1.1 -> -1, -0.5 -> 0, -0.99 -> 0
        # (-3)^2 + (-1)^2 + 0^2 + 0^2 = 9 + 1 + 0 + 0 = 10
        self.assertEqual(sum_of_squared_ceilings([-3.7, -1.1, -0.5, -0.99]), 10)

    def test_mixed_pos_neg_floats_and_integers(self):
        # Test case with a mix of positive/negative floats and exact integers
        # 2.0 -> 2, -1.5 -> -1, 3.4 -> 4, -5 -> -5
        # 2^2 + (-1)^2 + 4^2 + (-5)^2 = 4 + 1 + 16 + 25 = 46
        self.assertEqual(sum_of_squared_ceilings([2.0, -1.5, 3.4, -5]), 46)

    def test_single_element_list(self):
        # Test case with a single element, a positive float
        # 7.0001 -> 8
        # 8^2 = 64
        self.assertEqual(sum_of_squared_ceilings([7.0001]), 64)

    def test_all_zeros_and_near_zeros(self):
        # Test case with various representations of zero and very small positive float
        # 0 -> 0, 0.0 -> 0, -0.0 -> 0, 0.001 -> 1
        # 0^2 + 0^2 + 0^2 + 1^2 = 0 + 0 + 0 + 1 = 1
        self.assertEqual(sum_of_squared_ceilings([0, 0.0, -0.0, 0.001]), 1)

# To run these tests, you would typically use:
# if __name__ == '__main__':
#     unittest.main()