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
    def test_equal_total_chars_non_empty(self):
            # Test case for when total characters are equal with non-empty lists
            # This specifically covers the 'else' branch for non-trivial inputs.
            lst1 = ['abc', 'def']  # Total chars: 3 + 3 = 6
            lst2 = ['ghi', 'jkl']  # Total chars: 3 + 3 = 6
            self.assertEqual(self.solution.total_match(lst1, lst2), lst1)

            lst3 = ['hello']       # Total chars: 5
            lst4 = ['world']       # Total chars: 5
            self.assertEqual(self.solution.total_match(lst3, lst4), lst3)

    def test_one_list_empty_other_non_empty(self):
            # Test case where one list is empty and the other is not.
            # Covers both `lst1` empty and `lst2` empty scenarios.
            lst1 = []
            lst2 = ['single']      # Total chars: 6
            self.assertEqual(self.solution.total_match(lst1, lst2), lst1) # 0 < 6, returns lst1

            lst3 = ['another']     # Total chars: 7
            lst4 = []
            self.assertEqual(self.solution.total_match(lst3, lst4), lst4) # 7 > 0, returns lst4 (which is lst4 itself)

    def test_lists_with_empty_strings_inside(self):
            # Test cases involving lists that contain empty strings.
            # This ensures len('') is handled correctly and affects total character count.
            lst1 = ['a', '', 'b']  # Total chars: 1 + 0 + 1 = 2
            lst2 = ['cd']          # Total chars: 2
            self.assertEqual(self.solution.total_match(lst1, lst2), lst1) # Equal, returns lst1

            lst3 = ['']            # Total chars: 0
            lst4 = ['e']           # Total chars: 1
            self.assertEqual(self.solution.total_match(lst3, lst4), lst3) # 0 < 1, returns lst3

    def test_diverse_string_content_and_lengths(self):
            # Test with strings containing various characters (numbers, spaces, symbols)
            # to ensure len() is correctly applied across different string types.
            lst1 = ['123', 'abc def'] # Total chars: 3 + 7 = 10
            lst2 = ['test!@#$']      # Total chars: 8
            self.assertEqual(self.solution.total_match(lst1, lst2), lst2) # 10 > 8, returns lst2

            lst3 = ['short']         # Total chars: 5
            lst4 = ['much longer string'] # Total chars: 18
            self.assertEqual(self.solution.total_match(lst3, lst4), lst3) # 5 < 18, returns lst3
