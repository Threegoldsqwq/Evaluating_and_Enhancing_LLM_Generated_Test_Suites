import unittest

class TestCanArrange(unittest.TestCase):

    def test_example_one(self):
        # Example from problem description: one dip, returns its index
        self.assertEqual(can_arrange([1,2,4,3,5]), 3)

    def test_example_two(self):
        # Example from problem description: strictly increasing, returns -1
        self.assertEqual(can_arrange([1,2,3]), -1)

    def test_empty_array(self):
        # Edge case: empty array
        self.assertEqual(can_arrange([]), -1)

    def test_single_element_array(self):
        # Edge case: array with a single element
        self.assertEqual(can_arrange([42]), -1)

    def test_strictly_increasing_longer(self):
        # Test with a longer strictly increasing array
        self.assertEqual(can_arrange([10, 20, 30, 40, 50]), -1)

    def test_one_dip_at_start(self):
        # Test with a single dip occurring at the beginning of the array
        self.assertEqual(can_arrange([10, 5, 15, 20]), 1)

    def test_one_dip_in_middle(self):
        # Test with a single dip occurring in the middle of the array
        self.assertEqual(can_arrange([1, 5, 3, 7, 9]), 2)

    def test_one_dip_at_end(self):
        # Test with a single dip occurring at the very end of the array
        self.assertEqual(can_arrange([1, 2, 3, 8, 6]), 4)

    def test_multiple_dips_largest_at_end(self):
        # Test with multiple dips, where the largest index is the last dip
        self.assertEqual(can_arrange([1, 0, 5, 4, 10, 9]), 5)

    def test_completely_decreasing_array(self):
        # Test with an array that is completely decreasing
        self.assertEqual(can_arrange([5, 4, 3, 2, 1]), 4)