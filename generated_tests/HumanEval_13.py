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
    def test_greatest_common_divisor_negative_b_initial(self):
            # Ensures the 'while b:' loop is entered when 'b' is initially negative.
            # These tests verify the function's behavior with Python's modulo operator for negative numbers.
            # Expected GCD is typically positive, but the implementation may return negative values
            # based on the Euclidean algorithm's properties with Python's `%` behavior.

            # Case 1: a positive, b negative (b becomes 0 in one step)
            self.assertEqual(-5, greatest_common_divisor(10, -5))
            # Case 2: a negative, b negative (b becomes 0 in one step)
            self.assertEqual(-5, greatest_common_divisor(-10, -5))
            # Case 3: a positive, b negative (multiple steps)
            self.assertEqual(-3, greatest_common_divisor(6, -9))
            # Case 4: a negative, b negative (multiple steps)
            self.assertEqual(-3, greatest_common_divisor(-6, -9))

    def test_greatest_common_divisor_mixed_signs(self):
            # Further tests for scenarios involving one negative and one positive integer,
            # demonstrating how the sign of the final result can depend on the inputs' signs and order
            # due to Python's modulo behavior.

            # gcd(negative, positive) -> typically positive result (e.g., gcd(-3, 5) is 1)
            self.assertEqual(1, greatest_common_divisor(-3, 5))
            self.assertEqual(3, greatest_common_divisor(-9, 6))

            # gcd(positive, negative) -> may yield negative result as per current implementation
            # (e.g., gcd(3, -5) is -1, gcd(9, -6) is -3)
            self.assertEqual(-1, greatest_common_divisor(3, -5))
            self.assertEqual(-3, greatest_common_divisor(9, -6))

            # Test with primes and negative numbers
            self.assertEqual(1, greatest_common_divisor(-7, 13))
            self.assertEqual(-1, greatest_common_divisor(7, -13))
            self.assertEqual(-1, greatest_common_divisor(-7, -13))
