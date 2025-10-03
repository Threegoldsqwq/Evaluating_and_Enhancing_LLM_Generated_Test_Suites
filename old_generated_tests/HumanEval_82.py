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

if __name__ == '__main__':
    unittest.main()