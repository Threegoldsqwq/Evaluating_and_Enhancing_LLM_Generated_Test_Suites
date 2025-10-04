import unittest

# Assume largest_divisor function is defined elsewhere, e.g.:
# def largest_divisor(n):
#     for i in range(n // 2, 0, -1):
#         if n % i == 0:
#             return i
#     return 1 # Should not be reached if n > 1 as 1 is always a divisor

class TestLargestDivisor(unittest.TestCase):

    def test_example_case(self):
        # Example from the problem description
        self.assertEqual(largest_divisor(15), 5)

    def test_prime_number(self):
        # For a prime number, the largest divisor smaller than n is always 1.
        self.assertEqual(largest_divisor(7), 1)

    def test_small_prime_number(self):
        # Test with the smallest prime number.
        self.assertEqual(largest_divisor(2), 1)

    def test_even_composite_number(self):
        # A composite even number.
        self.assertEqual(largest_divisor(12), 6)

    def test_perfect_square(self):
        # Test with a perfect square.
        self.assertEqual(largest_divisor(9), 3)

    def test_power_of_two(self):
        # Test with a power of two.
        self.assertEqual(largest_divisor(16), 8)

    def test_large_composite_number(self):
        # A larger composite number.
        self.assertEqual(largest_divisor(100), 50)

    def test_another_odd_composite(self):
        # Another odd composite number.
        self.assertEqual(largest_divisor(21), 7)

    def test_number_with_many_divisors(self):
        # A number with many divisors.
        self.assertEqual(largest_divisor(30), 15)

    def test_smallest_composite_not_power_of_prime(self):
        # Smallest composite number that is not a prime power (and not an example).
        self.assertEqual(largest_divisor(6), 3)
    def test_value_error_for_n_less_than_or_equal_to_1(self):
            # Test n = 1, which should raise a ValueError
            with self.assertRaisesRegex(ValueError, "Input n must be greater than 1."):
                largest_divisor(1)

            # Test n = 0, which should also raise a ValueError
            with self.assertRaisesRegex(ValueError, "Input n must be greater than 1."):
                largest_divisor(0)

            # Test with a negative number, e.g., n = -5, to ensure the condition holds
            with self.assertRaisesRegex(ValueError, "Input n must be greater than 1."):
                largest_divisor(-5)

        # Note on line 40: The final 'return 1' in the solution code is unreachable
        # for any n > 1 because the loop "for i in range(n - 1, 0, -1)" will always
        # reach i=1, and 'n % 1 == 0' is always true, causing an earlier return.
        # If n <= 1, a ValueError is raised. Thus, this specific line is dead code
        # and cannot be covered by a test case without altering the function's logic.
