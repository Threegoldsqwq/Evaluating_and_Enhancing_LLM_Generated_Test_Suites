import unittest

class TestFibFib(unittest.TestCase):

    def test_fibfib_0(self):
        self.assertEqual(fibfib(0), 0)

    def test_fibfib_1(self):
        self.assertEqual(fibfib(1), 0)

    def test_fibfib_2(self):
        self.assertEqual(fibfib(2), 1)

    def test_fibfib_3(self):
        # fibfib(3) = fibfib(2) + fibfib(1) + fibfib(0) = 1 + 0 + 0 = 1
        self.assertEqual(fibfib(3), 1)

    def test_fibfib_4(self):
        # fibfib(4) = fibfib(3) + fibfib(2) + fibfib(1) = 1 + 1 + 0 = 2
        self.assertEqual(fibfib(4), 2)

    def test_fibfib_5(self):
        # fibfib(5) = fibfib(4) + fibfib(3) + fibfib(2) = 2 + 1 + 1 = 4
        self.assertEqual(fibfib(5), 4)

    def test_fibfib_6(self):
        # fibfib(6) = fibfib(5) + fibfib(4) + fibfib(3) = 4 + 2 + 1 = 7
        self.assertEqual(fibfib(6), 7)

    def test_fibfib_7(self):
        # fibfib(7) = fibfib(6) + fibfib(5) + fibfib(4) = 7 + 4 + 2 = 13
        self.assertEqual(fibfib(7), 13)

    def test_fibfib_8(self):
        # fibfib(8) = fibfib(7) + fibfib(6) + fibfib(5) = 13 + 7 + 4 = 24
        self.assertEqual(fibfib(8), 24)

    def test_fibfib_10(self):
        # fibfib(9) = fibfib(8) + fibfib(7) + fibfib(6) = 24 + 13 + 7 = 44
        # fibfib(10) = fibfib(9) + fibfib(8) + fibfib(7) = 44 + 24 + 13 = 81
        self.assertEqual(fibfib(10), 81)
    def test_fibfib_additional_coverage(self):
            # Test base cases explicitly to ensure full coverage of initial 'if' statements
            self.assertEqual(fibfib(0), 0, "Failed for n=0")
            self.assertEqual(fibfib(1), 0, "Failed for n=1")
            self.assertEqual(fibfib(2), 1, "Failed for n=2")

            # Test the first value computed by the loop (n=3)
            # This ensures the loop is entered and the first iteration is correct
            self.assertEqual(fibfib(3), 1, "Failed for n=3") # fibfib(0)+fibfib(1)+fibfib(2) = 0+0+1 = 1

            # Test a few more values to ensure the loop's recurrence relation and state updates are robust
            self.assertEqual(fibfib(4), 2, "Failed for n=4") # fibfib(1)+fibfib(2)+fibfib(3) = 0+1+1 = 2
            self.assertEqual(fibfib(5), 4, "Failed for n=5") # fibfib(2)+fibfib(3)+fibfib(4) = 1+1+2 = 4
            self.assertEqual(fibfib(6), 7, "Failed for n=6") # fibfib(3)+fibfib(4)+fibfib(5) = 1+2+4 = 7
            self.assertEqual(fibfib(7), 13, "Failed for n=7") # fibfib(4)+fibfib(5)+fibfib(6) = 2+4+7 = 13
            self.assertEqual(fibfib(8), 24, "Failed for n=8") # fibfib(5)+fibfib(6)+fibfib(7) = 4+7+13 = 24
