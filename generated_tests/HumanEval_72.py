import unittest

class TestWillItFly(unittest.TestCase):

    # Assume will_it_fly function is defined elsewhere:
    # def will_it_fly(q, w):
    #     is_balanced = q == q[::-1]
    #     sum_elements = sum(q)
    #     return is_balanced and sum_elements <= w

    def test_example_balanced_and_flies(self):
        # Example 1: Balanced and sum within weight
        self.assertTrue(will_it_fly([3, 2, 3], 9))

    def test_example_balanced_but_too_heavy(self):
        # Example 2: Balanced but sum exceeds weight
        self.assertFalse(will_it_fly([3, 2, 3], 1))

    def test_example_unbalanced_but_light_enough(self):
        # Example 3: Unbalanced but sum within weight
        self.assertFalse(will_it_fly([1, 2], 5))

    def test_example_single_element_flies(self):
        # Example 4: Single element, balanced, and light enough
        self.assertTrue(will_it_fly([3], 5))

    def test_empty_list_flies_with_zero_weight(self):
        # Empty list is palindromic, sum is 0. Should fly if w >= 0.
        self.assertTrue(will_it_fly([], 0))

    def test_empty_list_does_not_fly_with_negative_weight(self):
        # Empty list is palindromic, sum is 0. Should not fly if w < 0.
        self.assertFalse(will_it_fly([], -1))

    def test_even_length_balanced_and_flies(self):
        # Even length palindromic, sum exactly equals weight.
        self.assertTrue(will_it_fly([1, 2, 2, 1], 6))

    def test_even_length_balanced_but_too_heavy(self):
        # Even length palindromic, sum exceeds weight.
        self.assertFalse(will_it_fly([1, 2, 2, 1], 5))

    def test_unbalanced_and_too_heavy(self):
        # Neither condition met: Unbalanced and sum exceeds weight.
        self.assertFalse(will_it_fly([1, 2, 3, 4], 5))

    def test_long_balanced_and_flies(self):
        # Longer balanced list, flies.
        self.assertTrue(will_it_fly([5, 1, 9, 1, 5], 25))
    def test_empty_list_cases(self):
            # Test with an empty list q, which is palindromic and has a sum of 0.
            # Case 1: Empty list, w allows sum 0 -> True
            self.assertTrue(will_it_fly([], 0))
            self.assertTrue(will_it_fly([], 5))
            # Case 2: Empty list, w does not allow sum 0 (w is negative) -> False
            self.assertFalse(will_it_fly([], -1))
            self.assertFalse(will_it_fly([], -10))

    def test_negative_numbers_in_list(self):
            # Test with lists containing negative numbers.
            # Case 1: Balanced, sum <= w -> True
            self.assertTrue(will_it_fly([-1, -2, -1], -3)) # sum = -4, -4 <= -3
            self.assertTrue(will_it_fly([-5, 0, -5], -1)) # sum = -10, -10 <= -1
            # Case 2: Balanced, sum > w -> False
            self.assertFalse(will_it_fly([-1, -2, -1], -5)) # sum = -4, -4 > -5 (False)
            # Case 3: Unbalanced, sum <= w -> False
            self.assertFalse(will_it_fly([-1, -2, 1], 0)) # sum = -2, -2 <= 0, but unbalanced
            # Case 4: Unbalanced, sum > w -> False (F and F branch)
            self.assertFalse(will_it_fly([-1, -2, 1], -3)) # sum = -2, -2 > -3, and unbalanced

    def test_list_with_floats(self):
            # Test with lists containing floating-point numbers.
            # Case 1: Balanced, sum <= w -> True
            self.assertTrue(will_it_fly([1.5, 2.0, 1.5], 5)) # sum = 5.0, 5.0 <= 5
            self.assertTrue(will_it_fly([0.0, 0.0], 0)) # sum = 0.0, 0.0 <= 0
            # Case 2: Balanced, sum > w -> False
            self.assertFalse(will_it_fly([1.5, 2.0, 1.5], 4)) # sum = 5.0, 5.0 > 4
            # Case 3: Unbalanced, sum <= w -> False
            self.assertFalse(will_it_fly([1.1, 2.2], 5)) # sum = 3.3, 3.3 <= 5, but unbalanced

    def test_weight_boundary_conditions(self):
            # Test specific boundary conditions for w.
            # Case 1: Sum equals w, balanced -> True
            self.assertTrue(will_it_fly([1, 2, 1], 4)) # sum = 4, 4 <= 4
            self.assertTrue(will_it_fly([0], 0)) # sum = 0, 0 <= 0
            # Case 2: Sum equals w, unbalanced -> False
            self.assertFalse(will_it_fly([1, 2, 3], 6)) # sum = 6, 6 <= 6, but unbalanced
            # Case 3: w is negative, sum is positive (unbalanced or balanced) -> False
            self.assertFalse(will_it_fly([1, 2, 1], -1)) # sum = 4, 4 <= -1 (False)
            self.assertFalse(will_it_fly([1, 2], -5)) # sum = 3, 3 <= -5 (False), and unbalanced

    def test_both_conditions_false_explicitly(self):
            # Test a case where both is_balanced and is_light_enough are False.
            # This covers the F and F branch of the final 'and' condition.
            self.assertFalse(will_it_fly([1, 2, 3], 0)) # Unbalanced, sum=6 > 0 -> False and False
