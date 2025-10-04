import unittest

class TestFibonacci(unittest.TestCase):

    def test_fib_1(self):
        self.assertEqual(fib(1), 1)

    def test_fib_2(self):
        self.assertEqual(fib(2), 1)

    def test_fib_3(self):
        self.assertEqual(fib(3), 2)

    def test_fib_4(self):
        self.assertEqual(fib(4), 3)

    def test_fib_5(self):
        self.assertEqual(fib(5), 5)

    def test_fib_8(self):
        self.assertEqual(fib(8), 21)

    def test_fib_10(self):
        self.assertEqual(fib(10), 55)

    def test_fib_13(self):
        self.assertEqual(fib(13), 233)

    def test_fib_15(self):
        self.assertEqual(fib(15), 610)

    def test_fib_20(self):
        self.assertEqual(fib(20), 6765)