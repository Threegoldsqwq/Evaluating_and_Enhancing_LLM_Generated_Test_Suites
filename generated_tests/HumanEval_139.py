import unittest

class TestBrazilianFactorial(unittest.TestCase):

    def test_brazilian_factorial_1(self):
        # brazilian_factorial(1) = 1! = 1
        self.assertEqual(brazilian_factorial(1), 1)

    def test_brazilian_factorial_2(self):
        # brazilian_factorial(2) = 2! * 1! = 2 * 1 = 2
        self.assertEqual(brazilian_factorial(2), 2)

    def test_brazilian_factorial_3(self):
        # brazilian_factorial(3) = 3! * 2! * 1! = 6 * 2 * 1 = 12
        self.assertEqual(brazilian_factorial(3), 12)

    def test_brazilian_factorial_4(self):
        # brazilian_factorial(4) = 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288 (example case)
        self.assertEqual(brazilian_factorial(4), 288)

    def test_brazilian_factorial_5(self):
        # brazilian_factorial(5) = 5! * 4! * 3! * 2! * 1! = 120 * 24 * 6 * 2 * 1 = 34560
        self.assertEqual(brazilian_factorial(5), 34560)

    def test_brazilian_factorial_6(self):
        # brazilian_factorial(6) = 6! * 5! * 4! * 3! * 2! * 1! = 720 * 120 * 24 * 6 * 2 * 1 = 24883200
        self.assertEqual(brazilian_factorial(6), 24883200)

    def test_brazilian_factorial_7(self):
        # brazilian_factorial(7) = 7! * ... * 1! = 5040 * 24883200 = 125419968000
        self.assertEqual(brazilian_factorial(7), 125419968000)

    def test_brazilian_factorial_8(self):
        # brazilian_factorial(8) = 8! * ... * 1! = 40320 * 125419968000 = 5054890659840000
        self.assertEqual(brazilian_factorial(8), 5054890659840000)

    def test_brazilian_factorial_9(self):
        # brazilian_factorial(9) = 9! * ... * 1! = 362880 * 5054890659840000 = 1833136616086784000000
        self.assertEqual(brazilian_factorial(9), 1833136616086784000000)

    def test_brazilian_factorial_10(self):
        # brazilian_factorial(10) = 10! * ... * 1! = 3628800 * 1833136616086784000000 = 6649712530349341491200000000
        self.assertEqual(brazilian_factorial(10), 6649712530349341491200000000)
    def test_type_error_non_integer(self):
            # Covers the `if not isinstance(n, int):` branch (True) and raises TypeError
            with self.assertRaises(TypeError) as cm:
                brazilian_factorial(3.14)
            self.assertEqual(str(cm.exception), "Input 'n' must be an integer.")

            with self.assertRaises(TypeError) as cm:
                brazilian_factorial("abc")
            self.assertEqual(str(cm.exception), "Input 'n' must be an integer.")

            with self.assertRaises(TypeError) as cm:
                brazilian_factorial(None)
            self.assertEqual(str(cm.exception), "Input 'n' must be an integer.")

    def test_value_error_zero(self):
            # Covers the `if n <= 0:` branch (True) for n=0 and raises ValueError
            with self.assertRaises(ValueError) as cm:
                brazilian_factorial(0)
            self.assertEqual(str(cm.exception), "Input 'n' must be a positive integer (n > 0).")

    def test_value_error_negative(self):
            # Covers the `if n <= 0:` branch (True) for n < 0 and raises ValueError
            with self.assertRaises(ValueError) as cm:
                brazilian_factorial(-5)
            self.assertEqual(str(cm.exception), "Input 'n' must be a positive integer (n > 0).")

    def test_brazilian_factorial_one(self):
            # Covers the main calculation logic for the smallest valid input (n=1)
            # and implicitly covers lines 22 (total_product = 1) and 24 (for loop) if they were previously missed.
            self.assertEqual(brazilian_factorial(1), 1)

    def test_brazilian_factorial_two(self):
            # Covers the main calculation logic for n=2.
            self.assertEqual(brazilian_factorial(2), 2) # 2! * 1! = 2 * 1 = 2

    def test_brazilian_factorial_three(self):
            # Covers the main calculation logic for n=3.
            self.assertEqual(brazilian_factorial(3), 12) # 3! * 2! * 1! = 6 * 2 * 1 = 12

    def test_brazilian_factorial_four(self):
            # Covers the main calculation logic for n=4, as per docstring example.
            self.assertEqual(brazilian_factorial(4), 288) # 4! * 3! * 2! * 1! = 24 * 6 * 2 * 1 = 288

    def test_brazilian_factorial_five(self):
            # Covers the main calculation logic for a slightly larger input (n=5).
            # 5! * 4! * 3! * 2! * 1! = 120 * 24 * 6 * 2 * 1 = 34560
            self.assertEqual(brazilian_factorial(5), 34560)
