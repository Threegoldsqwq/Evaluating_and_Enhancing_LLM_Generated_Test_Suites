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