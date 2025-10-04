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
    def test_empty_list_coverage(self):
            # Exercises the path where the input list is empty.
            # The loop range (len(arr) - 1, 0, -1) becomes range(-1, 0, -1), which is empty.
            # This ensures the final 'return -1' is reached without loop execution.
            self.assertEqual(can_arrange([]), -1)

    def test_single_element_list_coverage(self):
            # Exercises the path where the input list has a single element.
            # The loop range (len(arr) - 1, 0, -1) becomes range(0, 0, -1), which is empty.
            # This ensures the final 'return -1' is reached without loop execution.
            self.assertEqual(can_arrange([5]), -1)

    def test_strictly_increasing_list_coverage(self):
            # Exercises the path where the loop iterates through the entire list, but
            # the condition arr[i] < arr[i-1] is never met.
            # This covers the final 'return -1' after a full loop execution.
            self.assertEqual(can_arrange([1, 2, 3, 4, 5]), -1)
            self.assertEqual(can_arrange([-10, -5, 0, 5]), -1) # With negative numbers

    def test_decreasing_pair_at_end_coverage(self):
            # Exercises the main execution path where a decreasing pair is found.
            # This specific test ensures that when the largest such index is at the end
            # of the array (and thus found first by the reverse iteration), it's returned.
            self.assertEqual(can_arrange([1, 2, 4, 3]), 3)
            self.assertEqual(can_arrange([10, 20, 5]), 2) # Shorter list, decreasing at index 2

    def test_decreasing_pair_at_beginning_coverage(self):
            # Exercises the path where the largest index of a decreasing pair is 1.
            # This ensures the loop correctly identifies and returns the first valid index it finds
            # while iterating backwards, even if it's the smallest index position (1).
            self.assertEqual(can_arrange([5, 4, 10, 20]), 1)
            self.assertEqual(can_arrange([0, -1, 5, 10]), 1) # With negative numbers

    def test_multiple_decreasing_pairs_coverage(self):
            # Tests a scenario with multiple decreasing pairs to ensure the function
            # correctly returns the *largest* index, which is achieved by iterating backwards.
            # For [1, 3, 2, 5, 4]:
            # - i=4: arr[4]=4, arr[3]=5 (4 < 5) -> return 4
            # - i=2: arr[2]=2, arr[1]=3 (2 < 3)
            self.assertEqual(can_arrange([1, 3, 2, 5, 4]), 4)

            # Another case: [10, 5, 4, 8, 3, 2, 7, 6]
            # Violations: (10,5) at i=1, (5,4) at i=2, (8,3) at i=4, (3,2) at i=5, (7,6) at i=7.
            # Largest index is 7.
            self.assertEqual(can_arrange([10, 5, 4, 8, 3, 2, 7, 6]), 7)
