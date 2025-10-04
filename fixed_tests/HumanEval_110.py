import unittest

# Assume the function 'exchange' exists and is imported or defined elsewhere.
# For example, it might look something like this:
# def exchange(lst1, lst2):
#     odds_in_lst1 = sum(1 for x in lst1 if x % 2 != 0)
#     evens_in_lst2 = sum(1 for x in lst2 if x % 2 == 0)
#     if odds_in_lst1 <= evens_in_lst2:
#         return "YES"
#     else:
#         return "NO"

class TestExchange(unittest.TestCase):

    def test_example_1(self):
        """
        Test case from the problem description:
        lst1 needs 2 evens, lst2 provides 2 evens.
        """
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")

    def test_example_2(self):
        """
        Test case from the problem description:
        lst1 needs 2 evens, lst2 provides only 1 even.
        """
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

    def test_lst1_already_all_even(self):
        """
        lst1 is already all even, so no exchanges are needed.
        """
        self.assertEqual(exchange([2, 4, 6], [1, 3, 5]), "YES")

    def test_lst1_all_odd_lst2_enough_evens(self):
        """
        lst1 is entirely odd, but lst2 contains more than enough even numbers.
        """
        self.assertEqual(exchange([1, 3, 5], [2, 4, 6, 8, 10]), "YES")

    def test_lst1_all_odd_lst2_not_enough_evens(self):
        """
        lst1 is entirely odd, and lst2 does not have enough even numbers to replace them all.
        """
        self.assertEqual(exchange([1, 3, 5, 7], [2, 4]), "NO")

    def test_lst1_some_odd_lst2_just_enough_evens(self):
        """
        lst1 has a mix of odd/even, and lst2 provides exactly the right amount of evens for the odds in lst1.
        """
        self.assertEqual(exchange([1, 2, 3, 4], [8, 10]), "YES") # lst1 needs 2 evens (for 1,3), lst2 has 2 evens (8,10)

    def test_lst1_some_odd_lst2_not_enough_evens_mixed(self):
        """
        lst1 has a mix of odd/even, and lst2 has some evens but not enough.
        """
        self.assertEqual(exchange([1, 2, 3, 4, 5], [7, 9, 10]), "NO") # lst1 needs 3 evens (for 1,3,5), lst2 has 1 even (10)

    def test_lst1_all_odd_lst2_all_odd(self):
        """
        lst1 is all odd, and lst2 contains no even numbers to facilitate an exchange.
        """
        self.assertEqual(exchange([1, 3, 5], [7, 9, 11]), "NO") # lst1 needs 3 evens, lst2 has 0 evens

    def test_large_lists_yes(self):
        """
        Test with larger lists where it should be possible to make lst1 all even.
        lst1 has 50 odd numbers (1,3,...,99). lst2 has 100 even numbers (2,4,...,200).
        """
        lst1_large = list(range(1, 101)) # Contains 50 odd numbers
        lst2_large = list(range(2, 202, 2)) # Contains 100 even numbers
        self.assertEqual(exchange(lst1_large, lst2_large), "YES")

    def test_large_lists_no(self):
        """
        Test with larger lists where it should NOT be possible to make lst1 all even.
        lst1 has 50 odd numbers. lst2 has only 25 even numbers.
        """
        lst1_large = list(range(1, 101)) # Contains 50 odd numbers
        lst2_large = list(range(2, 52, 2)) # Contains 25 even numbers
        self.assertEqual(exchange(lst1_large, lst2_large), "NO")