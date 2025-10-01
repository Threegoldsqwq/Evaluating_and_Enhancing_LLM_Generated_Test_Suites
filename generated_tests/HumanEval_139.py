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