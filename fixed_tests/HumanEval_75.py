import unittest

# Assume the function is_multiply_prime exists in the same scope or is imported.
# For the sake of completeness in generating tests, let's briefly sketch a dummy function
# that would be tested, but it won't be part of the final output.
#
# def is_multiply_prime(n: int) -> bool:
#     if n <= 1:
#         return False
#
#     prime_factors_count = 0
#     d = 2
#     temp_n = n
#
#     while d * d <= temp_n:
#         while temp_n % d == 0:
#             prime_factors_count += 1
#             temp_n //= d
#         d += 1
#
#     if temp_n > 1:  # Remaining factor is prime
#         prime_factors_count += 1
#
#     return prime_factors_count == 3


class TestIsMultiplyPrime(unittest.TestCase):

    def test_example_case(self):
        # Example from the problem description
        self.assertTrue(is_multiply_prime(30))  # 2 * 3 * 5

    def test_cube_of_prime_2(self):
            # 8 is 2*2*2. It is a product of 3 prime numbers, but they are not distinct.
            # The function's docstring specifies "3 distinct prime numbers".
            self.assertFalse(is_multiply_prime(8))
    def test_product_of_squared_prime_and_another_prime_smallest(self):
            # Smallest number of form p^2 * q (2*2*3)
            # This number (12) is not a product of three *distinct* primes,
            # so the function should correctly return False.
            self.assertFalse(is_multiply_prime(12))
    def test_cube_of_prime_3(self):
            # Cube of a prime (e.g., 3*3*3 = 27) does not consist of 3 *distinct* prime numbers.
            # The function's definition specifies "3 distinct prime numbers".
            # Therefore, 27 (3*3*3) should return False.
            self.assertFalse(is_multiply_prime(27))
    def test_product_of_squared_prime_and_another_prime_largest(self):
            # The function tests if a number is a product of 3 DISTINCT prime numbers.
            # The largest number of this form (p*q*r, with p, q, r distinct primes)
            # and less than 100 is 2 * 3 * 13 = 78.
            # Numbers like 99 (3*3*11) are products of primes, but not 3 *distinct* primes.
            self.assertTrue(is_multiply_prime(78))
    def test_one(self):
        # Edge case: 1 has no prime factors
        self.assertFalse(is_multiply_prime(1))

    def test_prime_number(self):
        # A prime number (has only 1 prime factor)
        self.assertFalse(is_multiply_prime(7))

    def test_product_of_two_primes(self):
        # A number with exactly two prime factors (2*5)
        self.assertFalse(is_multiply_prime(10))

    def test_product_of_four_primes(self):
        # A number with four prime factors (2*2*2*2)
        self.assertFalse(is_multiply_prime(16))

    def test_product_of_six_primes(self):
        # A number with six prime factors (2*2*2*2*2*2)
        self.assertFalse(is_multiply_prime(64))