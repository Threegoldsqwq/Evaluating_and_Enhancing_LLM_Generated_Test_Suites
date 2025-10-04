import unittest

class TestIsPrime(unittest.TestCase):

    def test_one_is_not_prime(self):
        self.assertFalse(is_prime(1))

    def test_two_is_prime(self):
        self.assertTrue(is_prime(2))

    def test_three_is_prime(self):
        self.assertTrue(is_prime(3))

    def test_four_is_not_prime(self):
        self.assertFalse(is_prime(4))

    def test_six_is_not_prime(self):
        self.assertFalse(is_prime(6))

    def test_nine_is_not_prime(self):
        self.assertFalse(is_prime(9)) # Smallest odd composite (perfect square)

    def test_eleven_is_prime(self):
        self.assertTrue(is_prime(11))

    def test_sixty_one_is_prime(self):
        self.assertTrue(is_prime(61))

    def test_one_hundred_one_is_prime(self):
        self.assertTrue(is_prime(101))

    def test_thirteen_thousand_four_hundred_forty_one_is_prime(self):
        self.assertTrue(is_prime(13441))

    def test_prime_two(self):
            # Covers the 'if n == 2:' branch (line 3) when n is 2.
            self.assertTrue(is_prime(2))

    def test_non_prime_zero(self):
            # Covers the 'if n <= 1:' branch (line 1) when n is 0.
            self.assertFalse(is_prime(0))

    def test_non_prime_negative(self):
            # Covers the 'if n <= 1:' branch (line 1) for negative numbers.
            self.assertFalse(is_prime(-1))
            self.assertFalse(is_prime(-100))

    def test_non_prime_odd_composite(self):
            # Covers the 'for i in range(3, limit + 1, 2):' loop and
            # the 'if n % i == 0:' return False for an odd composite number.
            # The existing doctests for non-primes (6, 4, 1) either hit n <= 1 or n % 2 == 0.
            # This test ensures the odd divisor check within the loop is exercised.
            self.assertFalse(is_prime(9))  # 3*3
            self.assertFalse(is_prime(15)) # 3*5
            self.assertFalse(is_prime(25)) # 5*5
            self.assertFalse(is_prime(49)) # 7*7
# Assume the function 'is_prime' exists in the scope where these tests are run.
# For example:
# def is_prime(n):
#     if n < 2:
#         return False
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#     return True

if __name__ == '__main__':
    # This dummy is_prime function is here just to make the tests runnable.
    # In a real scenario, this would be imported or defined elsewhere.
    # def is_prime(n):
    #     if n < 2:
    #         return False
    #     if n == 2 or n == 3:
    #         return True
    #     if n % 2 == 0 or n % 3 == 0:
    #         return False
    #     i = 5
    #     while i * i <= n:
    #         if n % i == 0 or n % (i + 2) == 0:
    #             return False
    #         i += 6
    #     return True

    unittest.main(argv=['first-arg-is-ignored'], exit=False)