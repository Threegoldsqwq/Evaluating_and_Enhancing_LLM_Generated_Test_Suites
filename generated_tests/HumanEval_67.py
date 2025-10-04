import unittest

class TestFruitDistribution(unittest.TestCase):

    def test_example_1(self):
        # Example from problem description
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)

    def test_example_2(self):
        # Example from problem description
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)

    def test_example_3(self):
        # Example from problem description
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)

    def test_example_4(self):
        # Example from problem description
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

    def test_zero_oranges(self):
        # Case with zero oranges
        self.assertEqual(fruit_distribution("7 apples and 0 oranges", 15), 8)

    def test_zero_apples_and_oranges(self):
        # Case with zero apples and zero oranges (all fruits are mangoes)
        self.assertEqual(fruit_distribution("0 apples and 0 oranges", 50), 50)

    def test_no_mangoes(self):
        # Case where there are no mangoes (total fruits = apples + oranges)
        self.assertEqual(fruit_distribution("10 apples and 15 oranges", 25), 0)

    def test_large_numbers(self):
        # Case with larger numbers for fruits
        self.assertEqual(fruit_distribution("150 apples and 200 oranges", 500), 150)

    def test_single_fruit_of_each_type(self):
        # Case with one apple and one orange
        self.assertEqual(fruit_distribution("1 apples and 1 oranges", 10), 8)
        
    def test_almost_all_non_mangoes(self):
        # Case where there's only one mango left
        self.assertEqual(fruit_distribution("1 apples and 98 oranges", 100), 1)
    def test_negative_mangoes_result(self):
            # Test case where total_fruits is less than the sum of apples and oranges,
            # resulting in a negative number of mangoes.
            self.assertEqual(self.solution.fruit_distribution("5 apples and 6 oranges", 10), -1)
            self.assertEqual(self.solution.fruit_distribution("10 apples and 1 oranges", 5), -6)

    def test_zero_apples_and_zero_oranges(self):
            # Test case where there are no apples and no oranges,
            # meaning all total fruits are mangoes.
            self.assertEqual(self.solution.fruit_distribution("0 apples and 0 oranges", 10), 10)
            self.assertEqual(self.solution.fruit_distribution("0 apples and 0 oranges", 0), 0)

    def test_all_fruits_are_known_types(self):
            # Test case where total_fruits equals the sum of apples and oranges,
            # resulting in zero mangoes.
            self.assertEqual(self.solution.fruit_distribution("5 apples and 5 oranges", 10), 0)
            self.assertEqual(self.solution.fruit_distribution("100 apples and 50 oranges", 150), 0)

    def test_zero_total_fruits_with_existing_fruits(self):
            # Test case where total_fruits is zero, but apples and oranges are positive,
            # leading to a negative mango count.
            self.assertEqual(self.solution.fruit_distribution("1 apples and 2 oranges", 0), -3)
            self.assertEqual(self.solution.fruit_distribution("0 apples and 1 oranges", 0), -1)

    def test_large_number_of_fruits(self):
            # Test with very large numbers to ensure correctness with integer handling.
            self.assertEqual(self.solution.fruit_distribution("1000000 apples and 2000000 oranges", 5000000), 2000000)
            self.assertEqual(self.solution.fruit_distribution("999999999 apples and 1 oranges", 1000000000), 0)
