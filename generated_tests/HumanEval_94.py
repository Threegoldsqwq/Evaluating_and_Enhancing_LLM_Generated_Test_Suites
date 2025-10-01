import unittest

# Assume the function `find_largest_prime_sum_digits` exists.
# The function should take a list of integers `lst` as input.

class TestLargestPrimeSumDigits(unittest.TestCase):

    def test_example_1(self):
        lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]
        # Primes: 3, 2, 5, 7, 181
        # Largest prime: 181
        # Sum of digits: 1 + 8 + 1 = 10
        self.assertEqual(find_largest_prime_sum_digits(lst), 10)

    def test_example_2(self):
        lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]
        # Primes: 2, 4597, 3, 5
        # Largest prime: 4597
        # Sum of digits: 4 + 5 + 9 + 7 = 25
        self.assertEqual(find_largest_prime_sum_digits(lst), 25)

    def test_example_3(self):
        lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]
        # Primes: 3, 5107, 109, 163, 23, 2323
        # Largest prime: 5107
        # Sum of digits: 5 + 1 + 0 + 7 = 13
        self.assertEqual(find_largest_prime_sum_digits(lst), 13)

    def test_example_4(self):
        lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6]
        # Primes: 71, 5, 83
        # Largest prime: 83
        # Sum of digits: 8 + 3 = 11
        self.assertEqual(find_largest_prime_sum_digits(lst), 11)

    def test_example_5(self):
        lst = [0,81,12,3,1,21]
        # Primes: 3
        # Largest prime: 3
        # Sum of digits: 3
        self.assertEqual(find_largest_prime_sum_digits(lst), 3)

    def test_example_6(self):
        lst = [0,8,1,2,1,7]
        # Primes: 2, 7
        # Largest prime: 7
        # Sum of digits: 7
        self.assertEqual(find_largest_prime_sum_digits(lst), 7)

    def test_no_primes_in_list(self):
        # List contains no prime numbers (0, 1 are not prime, others are composite)
        lst = [0, 1, 4, 6, 8, 9, 10, 12, 15]
        # If no prime is found, the function should likely return 0 (as sum of digits of 0).
        self.assertEqual(find_largest_prime_sum_digits(lst), 0)

    def test_list_with_only_one_prime(self):
        # List contains only one prime number
        lst = [10, 20, 2, 30, 40, 50]
        # Primes: 2
        # Largest prime: 2
        # Sum of digits: 2
        self.assertEqual(find_largest_prime_sum_digits(lst), 2)

    def test_list_with_large_primes_and_composites(self):
        # List with very large numbers, some prime, some composite
        lst = [1000000000, 999999999, 999999937, 1000000001, 1000000003] # 999999937 is prime, 1000000003 is prime
        # Primes: 999999937, 1000000003
        # Largest prime: 1000000003
        # Sum of digits: 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 3 = 4
        self.assertEqual(find_largest_prime_sum_digits(lst), 4)

    def test_list_with_small_primes_and_duplicates(self):
        # List containing small primes, including 2 and 3, with duplicates
        lst = [2, 3, 2, 5, 3, 1, 0, 4]
        # Primes: 2, 3, 5
        # Largest prime: 5
        # Sum of digits: 5
        self.assertEqual(find_largest_prime_sum_digits(lst), 5)

# To run the tests, you would typically have a main block like this:
if __name__ == '__main__':
    # You would define or import find_largest_prime_sum_digits here
    # For example:
    # def is_prime(n):
    #     if n < 2: return False
    #     for i in range(2, int(n**0.5) + 1):
    #         if n % i == 0: return False
    #     return True
    #
    # def sum_digits(n):
    #     return sum(int(digit) for digit in str(n))
    #
    # def find_largest_prime_sum_digits(lst):
    #     largest_prime = -1
    #     for num in lst:
    #         if is_prime(num):
    #             if num > largest_prime:
    #                 largest_prime = num
    #     return sum_digits(largest_prime) if largest_prime != -1 else 0

    unittest.main(argv=['first-arg-is-ignored'], exit=False)