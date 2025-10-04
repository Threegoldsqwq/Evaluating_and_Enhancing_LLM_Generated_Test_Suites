import unittest

class TestFactorize(unittest.TestCase):

    def test_prime_two(self):
        self.assertEqual(factorize(2), [2])

    def test_prime_seven(self):
        self.assertEqual(factorize(7), [7])

    def test_composite_with_two_repeated_factors(self):
        self.assertEqual(factorize(4), [2, 2])

    def test_composite_with_two_distinct_factors(self):
        self.assertEqual(factorize(6), [2, 3])

    def test_power_of_a_prime(self):
        self.assertEqual(factorize(27), [3, 3, 3])

    def test_composite_with_three_distinct_factors(self):
        self.assertEqual(factorize(30), [2, 3, 5])

    def test_product_of_mixed_factors(self):
        self.assertEqual(factorize(12), [2, 2, 3])

    def test_larger_composite_with_repeated_and_distinct(self):
        self.assertEqual(factorize(100), [2, 2, 5, 5])

    def test_another_large_composite(self):
        self.assertEqual(factorize(210), [2, 3, 5, 7])

    def test_large_prime(self):
        self.assertEqual(factorize(101), [101])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)