import unittest

# Assume the function prime_length exists globally or is imported
# For the purpose of running these tests in isolation,
# a dummy implementation might be useful, but the request asks to
# assume the function exists and ONLY generate test cases.
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def prime_length(s: str) -> bool:
#     return is_prime(len(s))

class TestPrimeLength(unittest.TestCase):

    def test_example_hello(self):
        # Length 5, which is prime
        self.assertTrue(prime_length('Hello'))

    def test_example_abcdcba(self):
        # Length 7, which is prime
        self.assertTrue(prime_length('abcdcba'))

    def test_example_kittens(self):
        # Length 7, which is prime
        self.assertTrue(prime_length('kittens'))

    def test_example_orange(self):
        # Length 6, which is not prime (2*3)
        self.assertFalse(prime_length('orange'))

    def test_empty_string(self):
        # Length 0, which is not prime
        self.assertFalse(prime_length(''))

    def test_single_character(self):
        # Length 1, which is not prime
        self.assertFalse(prime_length('a'))

    def test_length_two(self):
        # Length 2, which is the smallest prime
        self.assertTrue(prime_length('hi'))

    def test_length_four(self):
        # Length 4, which is not prime (2*2)
        self.assertFalse(prime_length('test'))

    def test_length_eleven(self):
        # Length 11, which is prime
        self.assertTrue(prime_length('long_string')) # 11 characters

    def test_length_twelve(self):
        # Length 12, which is not prime (2*2*3)
        self.assertFalse(prime_length('twelve_chars')) # 12 characters

    def test_prime_length_with_zero_and_one(self):
            # Covers the 'if n <= 1:' branch within _is_prime (True case)
            self.assertFalse(self.prime_length(""), "Length 0 is not prime.")
            self.assertFalse(self.prime_length("a"), "Length 1 is not prime.")

    def test_prime_length_with_two(self):
            # Covers the 'if n == 2:' branch within _is_prime (True case)
            self.assertTrue(self.prime_length("ab"), "Length 2 is prime.")

    def test_prime_length_with_even_numbers_greater_than_two(self):
            # Covers the 'if n % 2 == 0:' branch within _is_prime (True case for n > 2)
            self.assertFalse(self.prime_length("abcd"), "Length 4 is not prime.")
            self.assertFalse(self.prime_length("abcdef"), "Length 6 is not prime.")
            self.assertFalse(self.prime_length("a"*10), "Length 10 is not prime.")

    def test_prime_length_with_small_odd_primes(self):
            # Covers the 'if n % 2 == 0:' branch (False case) and the while loop not running
            self.assertTrue(self.prime_length("abc"), "Length 3 is prime.")
            self.assertTrue(self.prime_length("abcde"), "Length 5 is prime.")
            self.assertTrue(self.prime_length("abcdefg"), "Length 7 is prime.")

    def test_prime_length_with_odd_composites(self):
            # Covers the 'while i * i <= n:' branch (True case) and 'if n % i == 0:' branch (True case)
            self.assertFalse(self.prime_length("a"*9), "Length 9 (3*3) is not prime.")
            self.assertFalse(self.prime_length("a"*15), "Length 15 (3*5) is not prime.")
            self.assertFalse(self.prime_length("a"*21), "Length 21 (3*7) is not prime.")
            self.assertFalse(self.prime_length("a"*25), "Length 25 (5*5) is not prime.")
            self.assertFalse(self.prime_length("a"*33), "Length 33 (3*11) is not prime.")
            self.assertFalse(self.prime_length("a"*49), "Length 49 (7*7) is not prime.")

    def test_prime_length_with_larger_primes(self):
            # Covers the 'while i * i <= n:' branch (True case) and 'if n % i == 0:' branch (False case, ultimately returning True)
            self.assertTrue(self.prime_length("a"*11), "Length 11 is prime.")
            self.assertTrue(self.prime_length("a"*13), "Length 13 is prime.")
            self.assertTrue(self.prime_length("a"*17), "Length 17 is prime.")
            self.assertTrue(self.prime_length("a"*19), "Length 19 is prime.")
            self.assertTrue(self.prime_length("a"*23), "Length 23 is prime.")
if __name__ == '__main__':
    unittest.main()