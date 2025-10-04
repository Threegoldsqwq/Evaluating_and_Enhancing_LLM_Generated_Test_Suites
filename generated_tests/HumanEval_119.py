import unittest

# Assume the match_parens function is defined elsewhere, for example:
# def match_parens(strings):
#     s1, s2 = strings[0], strings[1]

#     def _check_balance_components(s):
#         current_bal = 0
#         min_bal_so_far = 0
#         for char in s:
#             if char == '(':
#                 current_bal += 1
#             else:
#                 current_bal -= 1
#             min_bal_so_far = min(min_bal_so_far, current_bal)
#         return (current_bal, min_bal_so_far)

#     def _is_good_concat(first, second):
#         bal1, min_bal1 = _check_balance_components(first)
#         bal2, min_bal2 = _check_balance_components(second)

#         # Condition 1: Total balance must be zero
#         if bal1 + bal2 != 0:
#             return False
        
#         # Condition 2: The first string itself must not dip below zero balance
#         if min_bal1 < 0:
#             return False

#         # Condition 3: The combined balance (first_string_balance + second_string_min_balance_relative)
#         # must not dip below zero
#         if bal1 + min_bal2 < 0:
#             return False
            
#         return True

#     if _is_good_concat(s1, s2) or _is_good_concat(s2, s1):
#         return 'Yes'
#     return 'No'


class TestMatchParens(unittest.TestCase):

    # Test Case 1: Example from problem description - Yes case
    def test_example_yes(self):
        self.assertEqual(match_parens(['()(', ')']), 'Yes')

    # Test Case 2: Example from problem description - No case
    def test_example_no(self):
        self.assertEqual(match_parens([')', ')']), 'No')

    # Test Case 3: Both strings are individually good and concatenate to a good string - Yes
    def test_both_good_individually(self):
        self.assertEqual(match_parens(['()', '(())']), 'Yes')
        # s1+s2: '()(())' is good
        # s2+s1: '(())()' is good

    # Test Case 4: One concatenation order works, the other doesn't, with simple unmatched strings - Yes
    def test_simple_order_matters(self):
        self.assertEqual(match_parens(['((', '))']), 'Yes')
        # s1+s2: '(())' is good
        # s2+s1: '))((` is not good

    # Test Case 5: Simplest case where order matters (only one char each) - Yes
    def test_minimal_order_matters(self):
        self.assertEqual(match_parens(['(', ')']), 'Yes')
        # s1+s2: '()' is good
        # s2+s1: ')(' is not good

    # Test Case 6: Total balance is not zero for any combination - No
    def test_total_balance_not_zero(self):
        self.assertEqual(match_parens(['(((', '()']), 'No')
        # s1 has balance 3, s2 has balance 0. Total balance 3.

    # Test Case 7: Complex strings, one concatenation works due to balance accumulation - Yes
    def test_complex_balances_sum_to_zero(self):
        self.assertEqual(match_parens(['((()', '))']), 'Yes')
        # s1 = '((()' (balance 2, min_bal_so_far 0)
        # s2 = '))' (balance -2, min_bal_so_far -2)
        # s1+s2 = '((()))': bal1+bal2=0, min_bal1>=0, bal1+min_bal2 = 2+(-2)=0. All conditions met.

    # Test Case 8: Strings that individually go negative and cannot be rescued - No
    def test_both_fail_prefix_balance(self):
        self.assertEqual(match_parens([')(', ')(']), 'No')
        # s1 = ')(' (balance 0, min_bal_so_far -1)
        # s2 = ')(' (balance 0, min_bal_so_far -1)
        # Both s1 and s2 have min_bal_so_far < 0, so neither can be the 'first' string.

    # Test Case 9: Long, valid strings that combine to be valid - Yes
    def test_long_both_good_strings(self):
        s1 = '(((())))' # bal=0, min_bal=0
        s2 = '((()))()' # bal=0, min_bal=0
        self.assertEqual(match_parens([s1, s2]), 'Yes')
        # Both strings are good, so their concatenation will also be good.

    # Test Case 10: Perfectly complementary strings - Yes
    def test_perfectly_complementary(self):
        self.assertEqual(match_parens(['(((', ')))']), 'Yes')
        # s1 = '(((' (balance 3, min_bal_so_far 0)
        # s2 = ')))' (balance -3, min_bal_so_far -3)
        # s1+s2 = '((()))': bal1+bal2=0, min_bal1>=0, bal1+min_bal2 = 3+(-3)=0. All conditions met.
    def test_is_good_empty_string(self):
            # Covers the case where the loop is not entered, and final balance is 0.
            self.assertTrue(is_good(""))

    def test_is_good_simple_balanced(self):
            # Covers entering the loop, incrementing/decrementing, and final balance is 0.
            self.assertTrue(is_good("()"))
            self.assertTrue(is_good("(())"))
            self.assertTrue(is_good("()(())"))

    def test_is_good_unbalanced_early_exit(self):
            # Covers the 'if balance < 0' condition (line 15 in original code) returning False.
            self.assertFalse(is_good(")(("))
            self.assertFalse(is_good("())"))
            self.assertFalse(is_good("))))"))
            self.assertFalse(is_good("(()))(")) # Complex case with early exit

    def test_is_good_unbalanced_final_positive_balance(self):
            # Covers the 'return balance == 0' (line 20 in original code) being False due to balance > 0.
            self.assertFalse(is_good("("))
            self.assertFalse(is_good("(()"))
            self.assertFalse(is_good("((("))
            self.assertFalse(is_good("()("))

    def test_match_parens_first_combination_good(self):
            # Covers 'if is_good(combined1)' (line 33 in original code) returning 'Yes'.
            self.assertEqual(match_parens(["(", ")"]), "Yes")
            self.assertEqual(match_parens(["()", ""]), "Yes")
            self.assertEqual(match_parens(["((", "))"]), "Yes")
            self.assertEqual(match_parens(["", "()"]), "Yes")

    def test_match_parens_second_combination_good(self):
            # Covers 'if is_good(combined2)' (line 38 in original code) returning 'Yes'
            # after combined1 was not good.
            # Example: s1 = ")", s2 = "("
            # combined1 = ")(" -> is_good returns False
            # combined2 = "()" -> is_good returns True
            self.assertEqual(match_parens([")", "("]), "Yes")

    def test_match_parens_neither_combination_good(self):
            # Covers 'return 'No'' (line 42 in original code).
            self.assertEqual(match_parens(["(", "("]), "No")
            self.assertEqual(match_parens([")", ")"]), "No")
            self.assertEqual(match_parens(["()(", ")("]), "No") # s1+s2="()()(" (False), s2+s1=")()()" (False)
            self.assertEqual(match_parens(["(()", "))"]), "No") # s1+s2="(()))" (False), s2+s1="))(( " (False)
