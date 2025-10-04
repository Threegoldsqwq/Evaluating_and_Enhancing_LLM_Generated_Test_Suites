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

    def test_factorize_edge_cases(self):
            # Covers the 'if n <= 1:' branch comprehensively
            self.assertEqual(factorize(1), [], "Should return an empty list for n=1")
            self.assertEqual(factorize(0), [], "Should return an empty list for n=0")
            self.assertEqual(factorize(-1), [], "Should return an empty list for negative n")
            self.assertEqual(factorize(-100), [], "Should return an empty list for another negative n")

    def test_factorize_even_numbers(self):
            # Specifically targets line 21 ('n //= 2') and the 'while n % 2 == 0:' loop
            self.assertEqual(factorize(2), [2], "Should factorize the smallest even prime number")
            self.assertEqual(factorize(4), [2, 2], "Should handle powers of 2, hitting 'n //= 2' multiple times")
            self.assertEqual(factorize(6), [2, 3], "Should factorize even numbers with an odd prime factor")
            self.assertEqual(factorize(12), [2, 2, 3], "Should handle even numbers with multiple 2s and an odd factor")

    def test_factorize_odd_composite_numbers(self):
            # Ensures coverage of the 'while i * i <= n:' loop for various odd composites
            self.assertEqual(factorize(9), [3, 3], "Should factorize odd composite numbers with repeated factors")
            self.assertEqual(factorize(15), [3, 5], "Should factorize odd composite numbers with distinct factors")
            self.assertEqual(factorize(75), [3, 5, 5], "Should handle odd composite numbers with multiple distinct and repeated factors")
            self.assertEqual(factorize(121), [11, 11], "Should factorize a perfect square of a prime number")

    def test_factorize_prime_numbers(self):
            # Covers the 'if n > 1:' block when 'n' itself is a prime
            self.assertEqual(factorize(7), [7], "Should return the number itself for a prime input")
            self.assertEqual(factorize(13), [13], "Should return the number itself for another prime input")
            self.assertEqual(factorize(97), [97], "Should return the number itself for a larger prime input")

    def test_factorize_mixed_factors(self):
            # Covers scenarios with mixed factors, including large prime factors
            self.assertEqual(factorize(14), [2, 7], "Should handle even numbers where the largest prime factor is greater than sqrt(original_n)")
            self.assertEqual(factorize(39), [3, 13], "Should handle odd numbers where the largest prime factor is greater than sqrt(original_n)")
            self.assertEqual(factorize(111), [3, 37], "Should handle larger numbers with distinct prime factors")
            self.assertEqual(factorize(2 * 101), [2, 101], "Should handle combinations of small and large prime factors")

    def test_factorize_large_numbers(self):
            # Tests with larger inputs to ensure robustness
            self.assertEqual(factorize(2**10), [2]*10, "Should handle large powers of 2 efficiently")
            self.assertEqual(factorize(2 * 3 * 5 * 7 * 11 * 13), [2, 3, 5, 7, 11, 13], "Should factorize product of many small primes")
            self.assertEqual(factorize(999999937), [999999937], "Should correctly identify a very large prime number") # 999999937 is a prime
            self.assertEqual(factorize(999999999), [3, 3, 3, 7, 11, 13, 37], "Should factorize a very large composite number")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)