import unittest
import math

# Assume the function mean_absolute_deviation exists and is imported or defined elsewhere.
# For demonstration purposes, a dummy function might look like this:
# def mean_absolute_deviation(numbers):
#     if not numbers:
#         raise ValueError("Input list cannot be empty.")
#
#     n = len(numbers)
#     mean = sum(numbers) / n
#
#     deviations = [abs(x - mean) for x in numbers]
#     mad = sum(deviations) / n
#     return mad

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_basic_positive_integers(self):
        # Test case from the problem description
        numbers = [1.0, 2.0, 3.0, 4.0]
        expected_mad = 1.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_single_element_list(self):
        # A list with one element should have a MAD of 0
        numbers = [5.0]
        expected_mad = 0.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_all_same_elements(self):
        # If all elements are identical, MAD should be 0
        numbers = [7.0, 7.0, 7.0, 7.0]
        expected_mad = 0.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_negative_numbers(self):
        # Test with entirely negative numbers
        numbers = [-1.0, -2.0, -3.0, -4.0]
        expected_mad = 1.0 # Mean is -2.5
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_mixed_positive_negative_and_zero(self):
        # Test with a mix of positive, negative, and zero
        numbers = [-2.0, 0.0, 2.0, 4.0]
        # Mean = (-2 + 0 + 2 + 4) / 4 = 4 / 4 = 1.0
        # | -2 - 1 | = 3
        # |  0 - 1 | = 1
        # |  2 - 1 | = 1
        # |  4 - 1 | = 3
        # Sum = 3 + 1 + 1 + 3 = 8
        # MAD = 8 / 4 = 2.0
        expected_mad = 2.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_floating_point_numbers(self):
        # Test with general floating point numbers
        numbers = [0.1, 0.2, 0.3, 0.4, 0.5]
        # Mean = (0.1 + 0.2 + 0.3 + 0.4 + 0.5) / 5 = 1.5 / 5 = 0.3
        # |0.1 - 0.3| = 0.2
        # |0.2 - 0.3| = 0.1
        # |0.3 - 0.3| = 0.0
        # |0.4 - 0.3| = 0.1
        # |0.5 - 0.3| = 0.2
        # Sum = 0.2 + 0.1 + 0.0 + 0.1 + 0.2 = 0.6
        # MAD = 0.6 / 5 = 0.12
        expected_mad = 0.12
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_empty_list(self):
        # An empty list should raise a ValueError as mean is undefined
        numbers = []
        with self.assertRaises(ValueError):
            mean_absolute_deviation(numbers)

    def test_larger_numbers(self):
        # Test with larger magnitude numbers
        numbers = [100.0, 110.0, 120.0, 130.0, 140.0]
        # Mean = (100+110+120+130+140) / 5 = 600 / 5 = 120.0
        # |100-120| = 20
        # |110-120| = 10
        # |120-120| = 0
        # |130-120| = 10
        # |140-120| = 20
        # Sum = 20 + 10 + 0 + 10 + 20 = 60
        # MAD = 60 / 5 = 12.0
        expected_mad = 12.0
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_numbers_with_many_decimal_places(self):
        # Test with numbers requiring higher precision
        numbers = [0.1234, 0.5678, 0.9012]
        # Mean = (0.1234 + 0.5678 + 0.9012) / 3 = 1.5924 / 3 = 0.5308
        # |0.1234 - 0.5308| = 0.4074
        # |0.5678 - 0.5308| = 0.0370
        # |0.9012 - 0.5308| = 0.3704
        # Sum = 0.4074 + 0.0370 + 0.3704 = 0.8148
        # MAD = 0.8148 / 3 = 0.2716
        expected_mad = 0.2716
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

    def test_repeated_numbers(self):
        # Test with numbers where some are repeated
        numbers = [1.0, 1.0, 2.0, 2.0, 3.0]
        # Mean = (1+1+2+2+3) / 5 = 9 / 5 = 1.8
        # |1 - 1.8| = 0.8
        # |1 - 1.8| = 0.8
        # |2 - 1.8| = 0.2
        # |2 - 1.8| = 0.2
        # |3 - 1.8| = 1.2
        # Sum = 0.8 + 0.8 + 0.2 + 0.2 + 1.2 = 3.2
        # MAD = 3.2 / 5 = 0.64
        expected_mad = 0.64
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad, places=7)

# To run these tests, you would typically have the mean_absolute_deviation function defined
# and then use:
# if __name__ == '__main__':
#     unittest.main()