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
    def test_positive_integers_product(self):
            """Test with both numbers being positive integers."""
            self.assertEqual(16, multiply(148, 412)) # 8 * 2
            self.assertEqual(72, multiply(19, 28))   # 9 * 8
            self.assertEqual(21, multiply(13, 17))   # 3 * 7
            self.assertEqual(2, multiply(11, 12))    # 1 * 2

    def test_one_negative_integer_product(self):
            """Test with one positive and one negative integer."""
            self.assertEqual(20, multiply(14, -15))  # 4 * ((-15)%10=5) = 20
            self.assertEqual(45, multiply(-25, 19))  # ((-25)%10=5) * 9 = 45
            self.assertEqual(49, multiply(7, -3))    # 7 * ((-3)%10=7) = 49
            self.assertEqual(10, multiply(-18, 5))   # ((-18)%10=2) * 5 = 10

    def test_both_negative_integers_product(self):
            """Test with both numbers being negative integers."""
            self.assertEqual(72, multiply(-1, -2))   # ((-1)%10=9) * ((-2)%10=8) = 72
            self.assertEqual(25, multiply(-5, -15))  # ((-5)%10=5) * ((-15)%10=5) = 25
            self.assertEqual(72, multiply(-12, -21)) # ((-12)%10=8) * ((-21)%10=9) = 72
            self.assertEqual(2, multiply(-9, -8))    # ((-9)%10=1) * ((-8)%10=2) = 2

    def test_zero_unit_digits(self):
            """Test cases involving numbers with a unit digit of zero."""
            self.assertEqual(0, multiply(2020, 1851)) # 0 * 1 = 0
            self.assertEqual(0, multiply(10, 5))      # 0 * 5 = 0
            self.assertEqual(0, multiply(-10, 7))     # ((-10)%10=0) * 7 = 0
            self.assertEqual(0, multiply(23, 0))      # 3 * 0 = 0
            self.assertEqual(0, multiply(0, 0))       # 0 * 0 = 0
            self.assertEqual(0, multiply(100, 200))   # 0 * 0 = 0
            self.assertEqual(0, multiply(0, -9))      # 0 * ((-9)%10=1) = 0

    def test_large_numbers_product(self):
            """Test with very large positive and negative numbers."""
            self.assertEqual(9, multiply(123456789, 987654321)) # 9 * 1 = 9
            self.assertEqual(1, multiply(10**18 + 1, 10**18 + 1)) # 1 * 1 = 1
            # Test with very large negative numbers ending in specific digits
            self.assertEqual(72, multiply(int('-1' + '0'*100 + '1'), int('-1' + '0'*100 + '2'))) # ((-...1)%10=9) * ((-...2)%10=8) = 72
            self.assertEqual(1, multiply(int('1' + '0'*100 + '1'), int('-1' + '0'*100 + '1'))) # 1 * ((-...1)%10=9) = 9. No, 1 * 9 = 9.
            self.assertEqual(9, multiply(int('1' + '0'*100 + '1'), int('-1' + '0'*100 + '1')))

    def test_single_digit_inputs(self):
            """Test cases where inputs are single-digit numbers."""
            self.assertEqual(25, multiply(5, 5))
            self.assertEqual(0, multiply(0, 7))
            self.assertEqual(63, multiply(7, 9))
            self.assertEqual(6, multiply(2, 3))
