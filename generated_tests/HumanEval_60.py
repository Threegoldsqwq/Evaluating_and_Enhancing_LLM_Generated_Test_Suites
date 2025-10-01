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