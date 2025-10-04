import unittest

class TestCountUpTo(unittest.TestCase):

    def test_zero_limit(self):
        """Test with n = 0, no primes are less than 0."""
        self.assertEqual(count_up_to(0), [])

    def test_one_limit(self):
        """Test with n = 1, no primes are less than 1."""
        self.assertEqual(count_up_to(1), [])

    def test_two_limit(self):
        """Test with n = 2, no primes are less than 2."""
        self.assertEqual(count_up_to(2), [])

    def test_three_limit(self):
        """Test with n = 3, only 2 is less than 3."""
        self.assertEqual(count_up_to(3), [2])

    def test_four_limit(self):
        """Test with n = 4, primes less than 4 are 2, 3."""
        self.assertEqual(count_up_to(4), [2, 3])

    def test_five_limit(self):
        """Test with n = 5, primes less than 5 are 2, 3 (example case)."""
        self.assertEqual(count_up_to(5), [2, 3])

    def test_eleven_limit(self):
        """Test with n = 11, primes less than 11 are 2, 3, 5, 7 (example case)."""
        self.assertEqual(count_up_to(11), [2, 3, 5, 7])

    def test_eighteen_limit(self):
        """Test with n = 18, primes less than 18 are 2, 3, 5, 7, 11, 13, 17 (example case)."""
        self.assertEqual(count_up_to(18), [2, 3, 5, 7, 11, 13, 17])

    def test_twenty_limit(self):
        """Test with n = 20, primes less than 20 are 2, 3, 5, 7, 11, 13, 17, 19 (example case)."""
        self.assertEqual(count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_large_limit(self):
        """Test with a larger limit, n = 30."""
        # Primes less than 30: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
        self.assertEqual(count_up_to(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_is_prime_additional_coverage(self):
            # Test cases to ensure the loop (line 14) in is_prime is entered and branches are covered.
            # Covered: num < 2, num == 2, num % 2 == 0.
            # Focus on: loop entry, divisor found, no divisor found.

            # num is an odd composite, factor found immediately (first 'i' in loop)
            self.assertFalse(is_prime(9), "9 is not prime (3*3)")
            self.assertFalse(is_prime(15), "15 is not prime (3*5)")

            # num is an odd composite, factor found after some iterations
            self.assertFalse(is_prime(25), "25 is not prime (5*5)")
            self.assertFalse(is_prime(49), "49 is not prime (7*7)")
            self.assertFalse(is_prime(121), "121 is not prime (11*11)")
            self.assertFalse(is_prime(91), "91 is not prime (7*13)") # First factor is not 3

            # num is prime, loop is entered but no factors are found (loop completes)
            self.assertTrue(is_prime(11), "11 is prime (loop entered, no factor)")
            self.assertTrue(is_prime(13), "13 is prime (loop entered, no factor)")
            self.assertTrue(is_prime(17), "17 is prime (loop entered, no factor)")
            self.assertTrue(is_prime(19), "19 is prime (loop entered, no factor)")
            self.assertTrue(is_prime(23), "23 is prime (loop entered, no factor)")
            self.assertTrue(is_prime(29), "29 is prime (loop entered, no factor)")
            self.assertTrue(is_prime(97), "97 is prime (larger prime, multiple iterations)")

            # Additional even numbers greater than 2 to confirm initial even check
            self.assertFalse(is_prime(4), "4 is not prime")
            self.assertFalse(is_prime(6), "6 is not prime")
            self.assertFalse(is_prime(8), "8 is not prime")

    def test_count_up_to_additional_coverage(self):
            # Test cases for count_up_to to ensure diverse inputs for 'n'.
            # Covered: n <= 2, various larger n (prime and composite).
            # Focus on: n being a small composite, n being a larger number for comprehensive is_prime calls.

            # n is a small composite number
            self.assertEqual(count_up_to(4), [2, 3], "Primes less than 4 should be [2, 3]")
            self.assertEqual(count_up_to(6), [2, 3, 5], "Primes less than 6 should be [2, 3, 5]")
            self.assertEqual(count_up_to(8), [2, 3, 5, 7], "Primes less than 8 should be [2, 3, 5, 7]")
            self.assertEqual(count_up_to(10), [2, 3, 5, 7], "Primes less than 10 should be [2, 3, 5, 7]")

            # n is a larger prime number, ensuring is_prime is called for many numbers up to n-1
            self.assertEqual(count_up_to(7), [2, 3, 5], "Primes less than 7 should be [2, 3, 5]")
            self.assertEqual(count_up_to(13), [2, 3, 5, 7, 11], "Primes less than 13 should be [2, 3, 5, 7, 11]")

            # Re-test small edge cases for clarity, even if indirectly covered by example usage
            self.assertEqual(count_up_to(0), [], "Primes less than 0 should be empty list")
            self.assertEqual(count_up_to(1), [], "Primes less than 1 should be empty list")
            self.assertEqual(count_up_to(2), [], "Primes less than 2 should be empty list")
            self.assertEqual(count_up_to(3), [2], "Primes less than 3 should be [2]")
# To run these tests, you would typically have the count_up_to function defined
# and then use:
# if __name__ == '__main__':
#     unittest.main()