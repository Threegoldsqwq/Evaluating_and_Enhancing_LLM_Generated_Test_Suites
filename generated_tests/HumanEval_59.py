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

    def test_smallest_even_composite(self):
            # n = 4 (2*2)
            # Should execute the 'while n % 2 == 0' loop multiple times, and then exit early for 'i' loop,
            # leading to n=1 and largest_factor=2.
            self.assertEqual(largest_prime_factor(4), 2)

    def test_smallest_odd_composite_square(self):
            # n = 9 (3*3)
            # Should execute the 'while n % i == 0' loop multiple times for i=3, leading to n=1
            # and largest_factor=3.
            self.assertEqual(largest_prime_factor(9), 3)

    def test_product_of_two_distinct_odd_primes(self):
            # n = 15 (3*5)
            # Should find 3, then n becomes 5, then 5 is picked up by 'if n > 1'.
            self.assertEqual(largest_prime_factor(15), 5)

    def test_product_of_multiple_distinct_odd_primes(self):
            # n = 3*5*7 = 105
            # Should find 3, then 5, then n becomes 7, then 7 is picked up by 'if n > 1'.
            self.assertEqual(largest_prime_factor(105), 7)

    def test_number_with_mixed_factors_starting_even(self):
            # n = 2*2*3 = 12
            # Should divide by 2 multiple times, then n becomes 3, which is picked up by 'if n > 1'.
            self.assertEqual(largest_prime_factor(12), 3)

    def test_number_with_mixed_factors_and_odd_loop(self):
            # n = 2*3*5*13 = 390
            # Divides by 2, then by 3, then by 5, then n becomes 13 which is picked up by 'if n > 1'.
            self.assertEqual(largest_prime_factor(390), 13)

    def test_power_of_odd_prime_ends_one(self):
            # n = 5*5*5 = 125
            # Should execute 'while n % i == 0' multiple times for i=5, and n ends up as 1.
            self.assertEqual(largest_prime_factor(125), 5)

    def test_composite_ends_with_prime_after_early_loop_termination(self):
            # n = 21 (3*7)
            # Finds 3, n becomes 7. The 'while i * i <= n' loop then terminates for i=5 (5*5 > 7),
            # and 'if n > 1' catches the remaining prime factor 7.
            self.assertEqual(largest_prime_factor(21), 7)

    def test_large_number_with_large_prime_factor(self):
            # A larger composite number (999999 = 3^3 * 7 * 11 * 13 * 37)
            # to stress the loops and ensure correct identification of the largest factor (37).
            self.assertEqual(largest_prime_factor(999999), 37)
# To run the tests, you would typically add:
# if __name__ == '__main__':
#     unittest.main()