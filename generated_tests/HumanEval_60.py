import unittest

class TestSumToN(unittest.TestCase):

    def test_sum_to_n_1(self):
        self.assertEqual(sum_to_n(1), 1)

    def test_sum_to_n_2(self):
        self.assertEqual(sum_to_n(2), 3)

    def test_sum_to_n_5(self):
        self.assertEqual(sum_to_n(5), 15)

    def test_sum_to_n_7(self):
        self.assertEqual(sum_to_n(7), 28)

    def test_sum_to_n_10(self):
        self.assertEqual(sum_to_n(10), 55)

    def test_sum_to_n_13(self):
        self.assertEqual(sum_to_n(13), 91)

    def test_sum_to_n_20(self):
        self.assertEqual(sum_to_n(20), 210)

    def test_sum_to_n_30(self):
        self.assertEqual(sum_to_n(30), 465)

    def test_sum_to_n_100(self):
        self.assertEqual(sum_to_n(100), 5050)

    def test_sum_to_n_1000(self):
        self.assertEqual(sum_to_n(1000), 500500)
    def test_negative_n_raises_value_error(self):
            """
            Test that sum_to_n raises a ValueError for negative input 'n'.
            This covers the 'if n < 0:' branch (line 31) and the raise statement (line 32).
            """
            with self.assertRaises(ValueError) as cm:
                sum_to_n(-1)
            self.assertEqual(str(cm.exception), "n must be a non-negative integer")

            with self.assertRaises(ValueError) as cm:
                sum_to_n(-100)
            self.assertEqual(str(cm.exception), "n must be a non-negative integer")

    def test_sum_with_one(self):
            """
            Test sum_to_n with n=1, a simple positive base case.
            (Often useful for ensuring small positive values are correctly handled.)
            """
            self.assertEqual(sum_to_n(1), 1)

    def test_sum_with_large_number(self):
            """
            Test sum_to_n with a larger number to ensure formula works for bigger inputs.
            """
            self.assertEqual(sum_to_n(1000), 500500)
