import unittest

# Assume the function largest_prime_factor exists in the current scope or is imported.
# For example:
# from your_module import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):

    def test_smallest_composite(self):
        # n = 2 * 2
        self.assertEqual(largest_prime_factor(4), 2)

    def test_product_of_two_small_primes(self):
        # n = 2 * 3
        self.assertEqual(largest_prime_factor(6), 3)

    def test_power_of_two(self):
        # n = 2^3
        self.assertEqual(largest_prime_factor(8), 2)

    def test_power_of_odd_prime(self):
        # n = 3^2
        self.assertEqual(largest_prime_factor(9), 3)

    def test_from_problem_description_1(self):
        # n = 5 * 7 * 13 * 29
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_from_problem_description_2(self):
        # n = 2^11
        self.assertEqual(largest_prime_factor(2048), 2)

    def test_multiple_distinct_odd_primes(self):
        # n = 7 * 11
        self.assertEqual(largest_prime_factor(77), 11)

    def test_mixed_small_prime_factors(self):
        # n = 2^2 * 5^2
        self.assertEqual(largest_prime_factor(100), 5)

    def test_larger_number_with_various_factors(self):
        # n = 2 * 3 * 5 * 7 * 11 = 2310
        self.assertEqual(largest_prime_factor(2310), 11)

    def test_large_number_with_a_larger_prime_factor(self):
        # n = 3^3 * 7 * 11 * 13 * 37 = 999999
        self.assertEqual(largest_prime_factor(999999), 37)

# To run the tests, you would typically add:
# if __name__ == '__main__':
#     unittest.main()