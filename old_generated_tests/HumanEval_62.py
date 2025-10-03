import unittest

class TestDerivative(unittest.TestCase):

    def test_example_1(self):
        # Test case provided in the problem description
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_example_2(self):
        # Test case provided in the problem description
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

    def test_constant_polynomial(self):
        # Derivative of a constant is 0, represented by an empty list
        self.assertEqual(derivative([5]), [])

    def test_zero_constant_polynomial(self):
        # Derivative of 0 is 0
        self.assertEqual(derivative([0]), [])

    def test_linear_polynomial(self):
        # Derivative of a + bx is b
        self.assertEqual(derivative([2, 3]), [3])

    def test_polynomial_with_negative_coefficients(self):
        # Test with negative coefficients
        self.assertEqual(derivative([1, -2, 3, -4]), [-2, 6, -12])

    def test_polynomial_with_zero_middle_coefficients(self):
        # Test with zero coefficients for some powers
        self.assertEqual(derivative([1, 0, -2, 5]), [0, -4, 15])

    def test_all_zero_coefficients_non_constant(self):
        # Test a polynomial where all coefficients are zero, and it's not just a constant 0.
        self.assertEqual(derivative([0, 0, 0, 0]), [0, 0, 0])

    def test_polynomial_with_float_coefficients(self):
        # Test with floating-point coefficients
        self.assertEqual(derivative([0.5, 1.5, -2.5]), [1.5, -5.0])

    def test_long_polynomial(self):
        # Test with a longer polynomial to ensure scaling works for higher powers
        self.assertEqual(derivative([1, 2, 3, 4, 5, 6, 7]), [2, 6, 12, 20, 30, 42])