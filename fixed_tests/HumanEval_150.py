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

if __name__ == '__main__':
    unittest.main()