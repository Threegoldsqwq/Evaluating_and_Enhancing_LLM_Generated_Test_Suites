import unittest

class TestPrimeFib(unittest.TestCase):
    def test_prime_fib_1(self):
        self.assertEqual(prime_fib(1), 2)

    def test_prime_fib_2(self):
        self.assertEqual(prime_fib(2), 3)

    def test_prime_fib_3(self):
        self.assertEqual(prime_fib(3), 5)

    def test_prime_fib_4(self):
        self.assertEqual(prime_fib(4), 13)

    def test_prime_fib_5(self):
        self.assertEqual(prime_fib(5), 89)

    def test_prime_fib_6(self):
        self.assertEqual(prime_fib(6), 233)

    def test_prime_fib_7(self):
        self.assertEqual(prime_fib(7), 1597)

    def test_prime_fib_8(self):
        self.assertEqual(prime_fib(8), 28657)

    def test_prime_fib_9(self):
        self.assertEqual(prime_fib(9), 514229)

    def test_prime_fib_10(self):
            self.assertEqual(prime_fib(10), 433494437)

    def test_is_prime_small_non_primes(self):
            # Covers num < 2 branch (line 4)
            self.assertFalse(is_prime(0), "0 is not prime")
            self.assertFalse(is_prime(1), "1 is not prime")
            self.assertFalse(is_prime(-5), "-5 is not prime")

    def test_is_prime_composite_numbers(self):
            # Covers num % i == 0 branch (line 7) and the loop (line 6, 9)
            self.assertFalse(is_prime(4), "4 is not prime")
            self.assertFalse(is_prime(6), "6 is not prime")
            self.assertFalse(is_prime(8), "8 is not prime") # Already covered by prime_fib but good for direct
            self.assertFalse(is_prime(9), "9 is not prime")
            self.assertFalse(is_prime(10), "10 is not prime")
            self.assertFalse(is_prime(12), "12 is not prime")
            self.assertFalse(is_prime(25), "25 is not prime")

    def test_is_prime_known_primes(self):
            # Covers the return True path after the loop (line 10) for various primes
            self.assertTrue(is_prime(2), "2 is prime")
            self.assertTrue(is_prime(3), "3 is prime")
            self.assertTrue(is_prime(5), "5 is prime")
            self.assertTrue(is_prime(7), "7 is prime")
            self.assertTrue(is_prime(11), "11 is prime")
            self.assertTrue(is_prime(13), "13 is prime") # Already covered by prime_fib but good for direct
            self.assertTrue(is_prime(17), "17 is prime")
            self.assertTrue(is_prime(19), "19 is prime")

        # Test cases for prime_fib function (to cover line 15, 41 and ValueError branches)

    def test_prime_fib_invalid_input_n_type(self):
            # Covers the 'not isinstance(n, int)' part of line 27
            with self.assertRaises(ValueError, msg="Should raise ValueError for non-integer n"):
                prime_fib(1.5)
            with self.assertRaises(ValueError, msg="Should raise ValueError for string n"):
                prime_fib("abc")
            with self.assertRaises(ValueError, msg="Should raise ValueError for list n"):
                prime_fib([1])

    def test_prime_fib_invalid_input_n_value(self):
            # Covers the 'n <= 0' part of line 27
            with self.assertRaises(ValueError, msg="Should raise ValueError for n = 0"):
                prime_fib(0)
            with self.assertRaises(ValueError, msg="Should raise ValueError for negative n"):
                prime_fib(-1)
            with self.assertRaises(ValueError, msg="Should raise ValueError for negative n"):
                prime_fib(-10)

    def test_prime_fib_larger_n_values(self):
            # Covers line 41 (Fibonacci generation) more extensively
            # and tests finding higher prime Fibonacci numbers.
            # F(13)=233 (prime), which is the 6th prime fib number
            self.assertEqual(prime_fib(6), 233, "The 6th prime Fibonacci number should be 233")
            # F(17)=1597 (prime), which is the 7th prime fib number
            self.assertEqual(prime_fib(7), 1597, "The 7th prime Fibonacci number should be 1597")
            # F(25)=75025 (not prime)
            # F(29)=514229 (prime), which is the 8th prime fib number (this will make the loop run even more)
            self.assertEqual(prime_fib(8), 514229, "The 8th prime Fibonacci number should be 514229")
