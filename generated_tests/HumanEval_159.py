import unittest

class TestRabbitCarrots(unittest.TestCase):

    def test_example_basic_case(self):
        # Example 1: Basic scenario where needed carrots are available
        self.assertEqual(eat(5, 6, 10), [11, 4])

    def test_example_not_enough_remaining(self):
        # Example 2: Not enough remaining carrots, eats all available
        self.assertEqual(eat(2, 11, 5), [7, 0])

    def test_need_equals_remaining(self):
        # Scenario: The number of needed carrots exactly matches remaining
        self.assertEqual(eat(10, 50, 50), [60, 0])

    def test_need_less_than_remaining(self):
        # Scenario: Rabbit needs few carrots, many are remaining, starts with 0 eaten
        self.assertEqual(eat(0, 5, 20), [5, 15])

    def test_need_greater_than_remaining_large_numbers(self):
        # Scenario: Rabbit needs many carrots, but few are remaining, large numbers
        self.assertEqual(eat(100, 200, 50), [150, 0])

    def test_need_is_zero(self):
        # Scenario: Rabbit needs 0 carrots, but there are some remaining
        self.assertEqual(eat(50, 0, 100), [50, 100])

    def test_remaining_is_zero(self):
        # Scenario: No carrots remaining in stock
        self.assertEqual(eat(10, 20, 0), [10, 0])

    def test_all_zeros(self):
        # Scenario: All input values are zero
        self.assertEqual(eat(0, 0, 0), [0, 0])

    def test_max_values_need_less_than_remaining(self):
        # Scenario: High values, need is less than remaining
        self.assertEqual(eat(500, 200, 1000), [700, 800])

    def test_max_values_need_more_than_remaining(self):
        # Scenario: High values, need is more than remaining
        self.assertEqual(eat(1000, 1000, 500), [1500, 0])
    def test_rabbit_wants_more_than_available(self):
            # Test case where the rabbit needs more carrots than are available.
            # This covers the branch of min(need, remaining) where remaining < need.
            number = 10
            need = 20
            remaining = 5
            result = eat(number, need, remaining)
            self.assertEqual(result, [15, 0]) # 10 (eaten) + 5 (from remaining) = 15; 5 - 5 = 0 left

    def test_rabbit_needs_zero_carrots(self):
            # Test case where the rabbit needs 0 additional carrots.
            # This covers min(0, remaining).
            number = 5
            need = 0
            remaining = 10
            result = eat(number, need, remaining)
            self.assertEqual(result, [5, 10]) # 5 (eaten) + 0 (from remaining) = 5; 10 - 0 = 10 left

    def test_no_carrots_remaining(self):
            # Test case where there are 0 carrots remaining in stock.
            # This covers min(need, 0).
            number = 5
            need = 10
            remaining = 0
            result = eat(number, need, remaining)
            self.assertEqual(result, [5, 0]) # 5 (eaten) + 0 (from remaining) = 5; 0 - 0 = 0 left

    def test_rabbit_needs_exactly_available(self):
            # Test case where the rabbit needs exactly the number of carrots available.
            # This covers min(x, x).
            number = 5
            need = 5
            remaining = 5
            result = eat(number, need, remaining)
            self.assertEqual(result, [10, 0]) # 5 (eaten) + 5 (from remaining) = 10; 5 - 5 = 0 left
