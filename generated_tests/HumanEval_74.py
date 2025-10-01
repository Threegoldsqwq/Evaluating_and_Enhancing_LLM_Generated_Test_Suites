import unittest

# Assume the function 'total_match' is defined elsewhere and available.
# Example:
# def total_match(list1, list2):
#     sum1 = sum(len(s) for s in list1)
#     sum2 = sum(len(s) for s in list2)
#
#     if sum1 <= sum2:
#         return list1
#     else:
#         return list2


class TestTotalMatch(unittest.TestCase):

    def test_empty_lists(self):
        # Test case 1: Both lists are empty
        self.assertEqual(total_match([], []), [])

    def test_example_one(self):
        # Test case 2: Example from problem description
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])

    def test_example_two(self):
        # Test case 3: Example from problem description
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_example_three(self):
        # Test case 4: Example from problem description
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])

    def test_example_four(self):
        # Test case 5: Example from problem description
        self.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

    def test_equal_total_chars_return_first(self):
        # Test case 6: Both lists have the same total number of characters, should return the first list
        self.assertEqual(total_match(['a', 'b', 'c'], ['d', 'e', 'f']), ['a', 'b', 'c'])

    def test_first_list_empty(self):
        # Test case 7: First list is empty, second is not
        self.assertEqual(total_match([], ['apple', 'banana']), [])

    def test_second_list_empty(self):
        # Test case 8: Second list is empty, first is not
        self.assertEqual(total_match(['apple', 'banana'], []), [])

    def test_longer_list_less_chars(self):
        # Test case 9: One list is longer (more elements) but has fewer total characters
        self.assertEqual(total_match(['a', 'b', 'c', 'd', 'e'], ['longstring']), ['a', 'b', 'c', 'd', 'e'])

    def test_different_lengths_and_char_counts(self):
        # Test case 10: Lists with different numbers of strings and total characters
        self.assertEqual(total_match(['hello', 'world'], ['a', 'b', 'c', 'd', 'e', 'f', 'g']), ['a', 'b', 'c', 'd', 'e', 'f', 'g'])