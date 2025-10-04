import unittest

# Assume 'rescale_to_unit' function exists globally or is imported appropriately.
# For example:
# from your_module import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):

    def assertListAlmostEqual(self, list1, list2, places=7, msg=None):
        """Helper to compare two lists of floats with almost equality."""
        self.assertEqual(len(list1), len(list2), msg="Lists have different lengths")
        for i, (a, b) in enumerate(zip(list1, list2)):
            self.assertAlmostEqual(a, b, places=places, msg=f"Elements at index {i} differ significantly: {a} vs {b}")

    def test_basic_positive_integers(self):
        input_list = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
        actual_output = rescale_to_unit(input_list)
        self.assertListAlmostEqual(actual_output, expected_output)

    def test_negative_numbers(self):
        input_list = [-5.0, -3.0, -1.0]
        expected_output = [0.0, 0.5, 1.0]
        actual_output = rescale_to_unit(input_list)
        self.assertListAlmostEqual(actual_output, expected_output)

    def test_mixed_numbers_with_zero(self):
        input_list = [-2.0, 0.0, 4.0]
        expected_output = [0.0, 1/3, 1.0]
        actual_output = rescale_to_unit(input_list)
        self.assertListAlmostEqual(actual_output, expected_output)

    def test_floating_point_numbers(self):
        input_list = [0.1, 0.3, 0.5, 0.7, 0.9]
        expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
        actual_output = rescale_to_unit(input_list)
        self.assertListAlmostEqual(actual_output, expected_output)

    def test_two_elements(self):
        input_list = [10.0, 20.0]
        expected_output = [0.0, 1.0]
        actual_output = rescale_to_unit(input_list)
        self.assertListAlmostEqual(actual_output, expected_output)

    def test_all_same_numbers(self):
        # When all numbers are the same, min == max.
        # The common behavior for normalization in this case is to map all to 0.0.
        input_list = [5.0, 5.0, 5.0, 5.0]
        expected_output = [0.0, 0.0, 0.0, 0.0]
        actual_output = rescale_to_unit(input_list)
        self.assertListAlmostEqual(actual_output, expected_output)

    def test_descending_order(self):
        input_list = [100.0, 50.0, 0.0, -50.0]
        expected_output = [1.0, 2/3, 1/3, 0.0]
        actual_output = rescale_to_unit(input_list)
        self.assertListAlmostEqual(actual_output, expected_output)

    def test_unsorted_list(self):
        input_list = [3.0, 1.0, 5.0, 2.0, 4.0]
        expected_output = [0.5, 0.0, 1.0, 0.25, 0.75]
        actual_output = rescale_to_unit(input_list)
        self.assertListAlmostEqual(actual_output, expected_output)

    def test_large_range(self):
        input_list = [1.0, 500000.0, 1000000.0]
        expected_output = [0.0, 499999.0 / 999999.0, 1.0]
        actual_output = rescale_to_unit(input_list)
        self.assertListAlmostEqual(actual_output, expected_output)

    def test_small_positive_range_floats(self):
        input_list = [0.001, 0.002, 0.003]
        expected_output = [0.0, 0.5, 1.0]
        actual_output = rescale_to_unit(input_list)
        self.assertListAlmostEqual(actual_output, expected_output)
    def test_empty_list(self):
            """Test with an empty list to cover the defensive programming branch."""
            self.assertEqual(rescale_to_unit([]), [])

    def test_two_distinct_elements(self):
            """Test with exactly two distinct elements, covering the minimal case for scaling."""
            self.assertEqual(rescale_to_unit([0.0, 1.0]), [0.0, 1.0])
            self.assertEqual(rescale_to_unit([10, 5]), [1.0, 0.0]) # reversed order
            self.assertEqual(rescale_to_unit([-5.0, 5.0]), [0.0, 1.0])

    def test_two_identical_elements(self):
            """Test with exactly two identical elements, covering the data_range == 0 branch for minimal length."""
            self.assertEqual(rescale_to_unit([7.0, 7.0]), [0.0, 0.0])
            self.assertEqual(rescale_to_unit([-1.0, -1.0]), [0.0, 0.0])

    def test_float_precision_mixed_values(self):
            """Test with various floating point numbers including negatives and non-integers, ensuring precision."""
            input_list = [-2.5, 0.0, 1.25, 5.0]
            # min_val = -2.5, max_val = 5.0, data_range = 7.5
            # Expected: 0.0, (2.5/7.5), (3.75/7.5), 1.0 -> 0.0, 1/3, 0.5, 1.0
            expected_list = [0.0, 1/3, 0.5, 1.0]
            result = rescale_to_unit(input_list)
            # Use assertAlmostEqual for floating point comparisons
            self.assertAlmostEqual(result[0], expected_list[0])
            self.assertAlmostEqual(result[1], expected_list[1])
            self.assertAlmostEqual(result[2], expected_list[2])
            self.assertAlmostEqual(result[3], expected_list[3])

    def test_large_range_values(self):
            """Test with numbers spanning a very large numerical range."""
            input_list = [1.0, 1e9, 2e9]
            # min_val = 1.0, max_val = 2e9, data_range = 2e9 - 1.0
            # 1.0 -> 0.0
            # 1e9 -> (1e9 - 1.0) / (2e9 - 1.0) approx 0.5
            # 2e9 -> 1.0
            expected_list = [0.0, (1e9 - 1.0) / (2e9 - 1.0), 1.0]
            result = rescale_to_unit(input_list)
            self.assertAlmostEqual(result[0], expected_list[0])
            self.assertAlmostEqual(result[1], expected_list[1])
            self.assertAlmostEqual(result[2], expected_list[2])
