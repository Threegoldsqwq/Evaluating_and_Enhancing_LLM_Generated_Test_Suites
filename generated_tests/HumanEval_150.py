import unittest

# Assume the function x_or_y exists and is imported or defined elsewhere
# For the purpose of these tests, we are testing its expected behavior.
# def x_or_y(n, x, y):
#     """
#     Returns the value of x if n is a prime number and returns the value of y otherwise.
#     """
#     if n < 2:
#         return y
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return y
#     return x

class TestXOrY(unittest.TestCase):

    def test_example_prime(self):
        # Example from problem description: n=7 (prime), should return x=34
        self.assertEqual(x_or_y(7, 34, 12), 34)

    def test_example_not_prime(self):
        # Example from problem description: n=15 (not prime), should return y=5
        self.assertEqual(x_or_y(15, 8, 5), 5)

    def test_smallest_prime(self):
        # n=2 is the smallest prime number
        self.assertEqual(x_or_y(2, 100, 200), 100)

    def test_another_prime(self):
        # n=3 is a prime number
        self.assertEqual(x_or_y(3, -5, 5), -5)

    def test_smallest_composite(self):
        # n=4 is the smallest composite number
        self.assertEqual(x_or_y(4, 10, 20), 20)

    def test_n_is_one(self):
        # n=1 is neither prime nor composite, so it should be treated as "not prime"
        self.assertEqual(x_or_y(1, 1000, 2000), 2000)

    def test_n_is_zero(self):
        # n=0 is not prime
        self.assertEqual(x_or_y(0, 300, 400), 400)

    def test_larger_prime(self):
        # n=13 is a prime number
        self.assertEqual(x_or_y(13, 77, 88), 77)

    def test_larger_composite(self):
        # n=25 is a composite number (5*5)
        self.assertEqual(x_or_y(25, 11, 22), 22)

    def test_even_composite(self):
        # n=6 is an even composite number
        self.assertEqual(x_or_y(6, 50, 60), 60)

    def test_is_prime_less_than_or_equal_to_1(self):
            # Covers the 'if num <= 1:' branch (line 26) and 'return False' (line 27)
            self.assertFalse(is_prime(0))
            self.assertFalse(is_prime(1))
            self.assertFalse(is_prime(-10))

    def test_is_prime_equals_2(self):
            # Covers the 'if num == 2:' branch (line 28) and 'return True' (line 29)
            self.assertTrue(is_prime(2))

    def test_is_prime_even_numbers_greater_than_2(self):
            # Covers the 'if num % 2 == 0:' branch (line 30) and 'return False' (line 31)
            self.assertFalse(is_prime(4))
            self.assertFalse(is_prime(6))
            self.assertFalse(is_prime(100))

    def test_is_prime_odd_primes_no_loop_entry(self):
            # Covers 'i = 3' (line 35), 'while i * i <= num:' (line 36) where condition is immediately False,
            # and 'return True' (line 40)
            self.assertTrue(is_prime(3)) # 3*3 > 3, loop not entered
            self.assertTrue(is_prime(5)) # 3*3 > 5, loop not entered
            self.assertTrue(is_prime(7)) # 3*3 > 7, loop not entered

    def test_is_prime_odd_primes_with_loop_iterations(self):
            # Covers 'i = 3' (line 35), 'while i * i <= num:' (line 36) where loop is entered,
            # 'if num % i == 0:' where condition is always False (line 37),
            # 'i += 2' (line 39), and 'return True' (line 40)
            self.assertTrue(is_prime(13)) # Checks 3, then 5 (3*3 <= 13, 13%3!=0; 5*5 > 13)
            self.assertTrue(is_prime(23)) # Checks 3, 5 (3*3 <= 23, 23%3!=0; 5*5 <= 23, 23%5!=0; 7*7 > 23)
            self.assertTrue(is_prime(97)) # Larger prime, multiple iterations

    def test_is_prime_odd_composites_with_loop_iterations(self):
            # Covers 'i = 3' (line 35), 'while i * i <= num:' (line 36) where loop is entered,
            # 'if num % i == 0:' where condition is True (line 37),
            # and 'return False' (line 38)
            self.assertFalse(is_prime(9))   # Divisible by 3
            self.assertFalse(is_prime(25))  # Divisible by 5
            self.assertFalse(is_prime(33))  # Divisible by 3
            self.assertFalse(is_prime(49))  # Divisible by 7
            self.assertFalse(is_prime(121)) # Divisible by 11

    def test_x_or_y_with_prime_n(self):
            # Covers 'if is_prime(n):' branch (line 47) and 'return x' (line 48)
            self.assertEqual(x_or_y(7, "prime", "not_prime"), "prime")
            self.assertEqual(x_or_y(2, 100, 200), 100)
            self.assertEqual(x_or_y(13, True, False), True)
            self.assertEqual(x_or_y(97, "found", "missed"), "found")

    def test_x_or_y_with_composite_n(self):
            # Covers 'else:' branch (line 49) and 'return y' (line 50)
            self.assertEqual(x_or_y(1, "prime", "not_prime"), "not_prime") # n <= 1
            self.assertEqual(x_or_y(0, 100, 200), 200) # n <= 1
            self.assertEqual(x_or_y(4, "hello", "world"), "world") # even composite
            self.assertEqual(x_or_y(9, True, False), False) # odd composite
            self.assertEqual(x_or_y(49, None, "default"), "default") # odd composite
if __name__ == '__main__':
    unittest.main()