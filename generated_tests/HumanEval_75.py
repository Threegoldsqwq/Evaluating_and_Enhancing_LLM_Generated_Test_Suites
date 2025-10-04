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
    def test_invalid_input_types(self):
            # Covers: line 29 (not isinstance(a, int) branch)
            # Ensures the function handles non-integer inputs gracefully by returning False.
            self.assertFalse(is_multiply_prime(30.5))
            self.assertFalse(is_multiply_prime("test"))
            self.assertFalse(is_multiply_prime(None))
            self.assertFalse(is_multiply_prime([]))

    def test_invalid_input_range_below_min(self):
            # Covers: line 29 (a <= 0 branch)
            # Tests inputs that are integers but out of the positive range.
            self.assertFalse(is_multiply_prime(0))
            self.assertFalse(is_multiply_prime(-1))
            self.assertFalse(is_multiply_prime(-100))

    def test_invalid_input_range_above_max(self):
            # Covers: line 29 (a >= 100 branch)
            # Tests inputs that are integers but exceed the maximum limit (100).
            self.assertFalse(is_multiply_prime(100))
            self.assertFalse(is_multiply_prime(101))
            self.assertFalse(is_multiply_prime(200))

    def test_numbers_less_than_30(self):
            # Covers: line 36 (if a < 30: return False)
            # Tests positive integers less than 30, which cannot be a product of 3 distinct primes.
            self.assertFalse(is_multiply_prime(1)) # Smallest positive integer
            self.assertFalse(is_multiply_prime(2)) # Prime
            self.assertFalse(is_multiply_prime(29)) # Largest prime less than 30
            self.assertFalse(is_multiply_prime(6)) # 2*3 (2 factors)
            self.assertFalse(is_multiply_prime(12)) # 2*2*3 (3 factors, but not distinct, also <30)
            self.assertFalse(is_multiply_prime(25)) # 5*5 (2 factors, not distinct)

    def test_trigger_p_squared_greater_than_temp_a_break(self):
            # Covers: line 45 (if p * p > temp_a: break)
            # This condition is met when temp_a (the remaining number to factor) is a prime
            # or a product of primes, all of which are larger than the current prime 'p' being checked.
            # This also indirectly covers line 58 (if temp_a > 1) which appends the remaining prime.

            # Case 1: 'a' is a prime number itself (e.g., 97).
            # The loop will iterate through small primes (2, 3, 5, 7).
            # For p=11, p*p=121 which is > temp_a=97. The loop breaks.
            # temp_a (97) is then added as a factor. Result: [97], len=1, False.
            self.assertFalse(is_multiply_prime(97)) 

            # Case 2: 'a' is a product of two distinct primes (e.g., 7*11=77).
            # Factorization: p=7, temp_a becomes 11. factors=[7].
            # Next prime is 11. p=11, p*p=121 which is > temp_a=11. The loop breaks.
            # temp_a (11) is then added as a factor. Result: [7, 11], len=2, False.
            self.assertFalse(is_multiply_prime(77))

            # Case 3: Another product of two distinct primes (e.g., 5*17=85).
            # Factorization: p=5, temp_a becomes 17. factors=[5].
            # Next prime is 7. p=7, p*p=49 which is > temp_a=17. The loop breaks.
            # temp_a (17) is then added as a factor. Result: [5, 17], len=2, False.
            self.assertFalse(is_multiply_prime(85))

    def test_three_factors_not_distinct(self):
            # Covers: line 63, specifically when len(factors) == 3 is True, but len(set(factors)) == 3 is False.
            # These are numbers that are products of three prime numbers, but not all of them are distinct.
            self.assertFalse(is_multiply_prime(44)) # 2 * 2 * 11. Factors: [2, 2, 11]. len=3, len(set)=2.
            self.assertFalse(is_multiply_prime(52)) # 2 * 2 * 13. Factors: [2, 2, 13]. len=3, len(set)=2.
            self.assertFalse(is_multiply_prime(45)) # 3 * 3 * 5. Factors: [3, 3, 5]. len=3, len(set)=2.
            self.assertFalse(is_multiply_prime(63)) # 3 * 3 * 7. Factors: [3, 3, 7]. len=3, len(set)=2.
            self.assertFalse(is_multiply_prime(50)) # 2 * 5 * 5. Factors: [2, 5, 5]. len=3, len(set)=2.
            self.assertFalse(is_multiply_prime(98)) # 2 * 7 * 7. Factors: [2, 7, 7]. len=3, len(set)=2.
            self.assertFalse(is_multiply_prime(99)) # 3 * 3 * 11. Factors: [3, 3, 11]. len=3, len(set)=2.

    def test_more_than_three_factors(self):
            # Covers: line 63, specifically when len(factors) == 3 is False.
            # These are numbers with more than three prime factors (counting multiplicity).
            self.assertFalse(is_multiply_prime(60)) # 2 * 2 * 3 * 5. Factors: [2, 2, 3, 5]. len=4.
            self.assertFalse(is_multiply_prime(40)) # 2 * 2 * 2 * 5. Factors: [2, 2, 2, 5]. len=4.
            self.assertFalse(is_multiply_prime(90)) # 2 * 3 * 3 * 5. Factors: [2, 3, 3, 5]. len=4.

    def test_valid_multiply_primes_boundary_cases(self):
            # Ensure that valid cases, especially those close to the 99 limit, are correctly identified.
            # Smallest multiply prime: 2*3*5 = 30.
            self.assertTrue(is_multiply_prime(30)) 
            # Other valid multiply primes within the range.
            self.assertTrue(is_multiply_prime(2 * 3 * 7))  # 42
            self.assertTrue(is_multiply_prime(2 * 3 * 11)) # 66
            self.assertTrue(is_multiply_prime(2 * 5 * 7))  # 70
            self.assertTrue(is_multiply_prime(2 * 3 * 13)) # 78
            # Largest possible multiply prime under 100 is 2*3*13 = 78.
            # 2*3*17 = 102 (too large, covered by a >= 100 check)
            # 2*5*11 = 110 (too large)
