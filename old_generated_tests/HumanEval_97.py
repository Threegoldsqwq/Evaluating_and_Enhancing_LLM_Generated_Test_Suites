import unittest

class TestMultiplyUnitDigits(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(multiply(148, 412), 16)

    def test_example_2(self):
        self.assertEqual(multiply(19, 28), 72)

    def test_example_3(self):
        self.assertEqual(multiply(2020, 1851), 0)

    def test_example_4_one_negative(self):
        self.assertEqual(multiply(14, -15), 20)

    def test_both_negative(self):
        self.assertEqual(multiply(-17, -23), 21)

    def test_one_number_is_zero(self):
        self.assertEqual(multiply(0, 123), 0)

    def test_both_numbers_are_zero(self):
        self.assertEqual(multiply(0, 0), 0)

    def test_large_numbers(self):
        self.assertEqual(multiply(987654321, 123456789), 9) # 1 * 9

    def test_single_digit_numbers(self):
        self.assertEqual(multiply(5, 7), 35)

    def test_numbers_ending_in_one(self):
        self.assertEqual(multiply(11, 21), 1)