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