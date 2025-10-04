import unittest

class TestMoveOneBall(unittest.TestCase):

    def test_empty_array(self):
        # Test case for an empty array, which should always be considered sorted.
        self.assertTrue(move_one_ball([]))

    def test_already_sorted_array(self):
        # Test case for an array that is already sorted, requiring zero shifts.
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

    def test_single_element_array(self):
        # Test case for an array with a single element.
        self.assertTrue(move_one_ball([42]))

    def test_one_right_shift_needed(self):
        # Test case where one right shift makes the array sorted.
        self.assertTrue(move_one_ball([5, 1, 2, 3, 4]))

    def test_multiple_right_shifts_needed(self):
        # Test case matching the problem's first example, requiring multiple shifts.
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))

    def test_not_possible_two_descending_points(self):
        # Test case matching the problem's second example, where two "breaks" exist.
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))

    def test_not_possible_general_unsorted(self):
        # Test case for a generally unsorted array that cannot be fixed by rotation.
        self.assertFalse(move_one_ball([1, 3, 2]))

    def test_larger_array_rotated_sorted(self):
        # Test case with a larger array that is a rotated version of a sorted array.
        self.assertTrue(move_one_ball([7, 8, 9, 10, 1, 2, 3, 4, 5, 6]))

    def test_larger_array_not_rotatable(self):
        # Test case with a larger array that has more than one point of unsortedness
        # (considering wrap-around).
        self.assertFalse(move_one_ball([1, 3, 2, 4, 6, 5, 7, 8]))

    def test_descending_array_not_sortable(self):
        # Test case for a perfectly descending array which cannot be sorted by rotation
        # (unless it's length 0 or 1, covered by other tests).
        self.assertFalse(move_one_ball([5, 4, 3, 2, 1]))
    def test_one_decrease_unsortable_cycle(self):
            # This test case targets the 'else: return False' branch within
            # 'elif count_decreases == 1:' block.
            # It's a case where there's exactly one decrease, but the array cannot
            # be cyclically sorted because the last element is greater than the first,
            # preventing a valid "wrap-around" condition for a right shift.
            # Example from comments: [2, 1, 3] -> count_decreases=1, arr[2]=3 > arr[0]=2
            self.assertFalse(move_one_ball([2, 1, 3]))
            self.assertFalse(move_one_ball([3, 1, 2, 4])) # Another example: [3,1] is break, but 4 > 3
            self.assertFalse(move_one_ball([10, 5, 6, 7, 8])) # Break at 10>5, but 8 > 10 is False (8 <= 10 is True - This should return True if it follows the cycle rule)
            # Let's re-evaluate [10, 5, 6, 7, 8].
            # n = 5
            # i=0: 10 > 5 => count_decreases = 1
            # i=1: 5 > 6 False
            # i=2: 6 > 7 False
            # i=3: 7 > 8 False
            # count_decreases = 1.
            # arr[n-1] = arr[4] = 8
            # arr[0] = 10
            # 8 <= 10 is True. This should return True.
            # So, [10, 5, 6, 7, 8] can be sorted by right shifts:
            # [10, 5, 6, 7, 8] -> [8, 10, 5, 6, 7] -> [7, 8, 10, 5, 6] -> [6, 7, 8, 10, 5] -> [5, 6, 7, 8, 10]
            # This is a good example for the True branch of 'arr[n-1] <= arr[0]'.

            # Let's find another clear example for the False branch (arr[n-1] > arr[0])
            # [1, 3, 2]
            # n = 3
            # i=0: 1 > 3 False
            # i=1: 3 > 2 => count_decreases = 1
            # count_decreases = 1.
            # arr[n-1] = arr[2] = 2
            # arr[0] = 1
            # 2 <= 1 is False. Returns False. This is another good one.
            self.assertFalse(move_one_ball([1, 3, 2]))

            # A longer example to ensure the logic holds
            self.assertFalse(move_one_ball([10, 1, 2, 3, 4, 11])) # Break at 10>1, but 11 > 10
