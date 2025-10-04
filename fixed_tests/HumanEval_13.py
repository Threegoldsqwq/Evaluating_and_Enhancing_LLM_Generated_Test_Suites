import unittest

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_coprime_numbers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_numbers_with_common_factor(self):
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_one_number_is_multiple_of_other(self):
        self.assertEqual(greatest_common_divisor(10, 5), 5)
        self.assertEqual(greatest_common_divisor(12, 4), 4)

    def test_first_number_is_zero(self):
        self.assertEqual(greatest_common_divisor(0, 7), 7)

    def test_second_number_is_zero(self):
        self.assertEqual(greatest_common_divisor(13, 0), 13)

    def test_both_numbers_are_zero(self):
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_negative_first_number(self):
        self.assertEqual(greatest_common_divisor(-10, 5), 5)

    def test_negative_second_number(self):
        self.assertEqual(greatest_common_divisor(15, -25), -5)
    def test_both_numbers_negative(self):
        self.assertEqual(greatest_common_divisor(-10, -15), -5)
    def test_large_numbers(self):
        self.assertEqual(greatest_common_divisor(1071, 462), 21)