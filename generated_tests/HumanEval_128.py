import unittest

class TestProdSigns(unittest.TestCase):

    def test_example_one(self):
        # Example from problem description: Mixed numbers, odd negative count
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)

    def test_example_two(self):
        # Example from problem description: Contains zero
        self.assertEqual(prod_signs([0, 1]), 0)

    def test_empty_array(self):
        # Example from problem description: Empty array
        self.assertIsNone(prod_signs([]))

    def test_all_positives(self):
        # All positive numbers
        self.assertEqual(prod_signs([1, 5, 10]), 16)

    def test_all_negatives_odd_count(self):
        # All negative numbers, odd count of negatives
        self.assertEqual(prod_signs([-1, -2, -3]), -6)

    def test_all_negatives_even_count(self):
        # All negative numbers, even count of negatives
        self.assertEqual(prod_signs([-1, -2, -3, -4]), 10)

    def test_mixed_even_negatives(self):
        # Mixed positive/negative, even count of negatives
        self.assertEqual(prod_signs([1, -2, 3, -4]), 10)

    def test_mixed_odd_negatives(self):
        # Mixed positive/negative, odd count of negatives
        self.assertEqual(prod_signs([1, -2, 3, -4, -5]), -15)

    def test_array_with_only_zero(self):
        # Array with a single zero
        self.assertEqual(prod_signs([0]), 0)

    def test_single_negative_number(self):
        # Single negative number
        self.assertEqual(prod_signs([-7]), -7)

# Assuming prod_signs function is defined elsewhere for testing purposes.
# For example:
# def prod_signs(arr):
#     if not arr:
#         return None
#
#     sum_magnitudes = 0
#     product_signs = 1
#
#     for x in arr:
#         sum_magnitudes += abs(x)
#         if x > 0:
#             product_signs *= 1
#         elif x < 0:
#             product_signs *= -1
#         else: # x == 0
#             product_signs *= 0 # If any number is 0, product of signs becomes 0
#
#     return sum_magnitudes * product_signs

if __name__ == '__main__':
    unittest.main()