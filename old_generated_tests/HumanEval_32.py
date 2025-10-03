import unittest

# Assume the function 'evaluate_polynomial' exists globally or in a class for testing.
# For demonstration purposes, let's define a dummy one here that the tests will call.
# In a real scenario, this would be imported or part of the class being tested.
# def evaluate_polynomial(xs, x):
#     """
#     Evaluates polynomial with coefficients xs at point x.
#     return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
#     """
#     result = 0
#     for i, coeff in enumerate(xs):
#         result += coeff * (x ** i)
#     return result

class TestEvaluatePolynomial(unittest.TestCase):

    def test_constant_polynomial(self):
        # P(x) = 5
        xs = [5]
        x = 2
        self.assertEqual(evaluate_polynomial(xs, x), 5)

    def test_linear_polynomial_at_zero(self):
        # P(x) = 3 + 2x, at x=0
        xs = [3, 2]
        x = 0
        self.assertEqual(evaluate_polynomial(xs, x), 3)

    def test_linear_polynomial_at_one(self):
        # P(x) = 3 + 2x, at x=1
        xs = [3, 2]
        x = 1
        self.assertEqual(evaluate_polynomial(xs, x), 5)

    def test_quadratic_polynomial_positive_x(self):
        # P(x) = 1 - 4x + x^2, at x=3
        xs = [1, -4, 1]
        x = 3
        expected = 1 - 4*3 + 1*(3**2)  # 1 - 12 + 9 = -2
        self.assertEqual(evaluate_polynomial(xs, x), expected)

    def test_quadratic_polynomial_negative_x(self):
        # P(x) = 1 - 4x + x^2, at x=-2
        xs = [1, -4, 1]
        x = -2
        expected = 1 - 4*(-2) + 1*((-2)**2) # 1 + 8 + 4 = 13
        self.assertEqual(evaluate_polynomial(xs, x), expected)

    def test_cubic_polynomial_mixed_coefficients(self):
        # P(x) = 2 - x + 0x^2 + 3x^3, at x=2
        xs = [2, -1, 0, 3]
        x = 2
        expected = 2 - 1*2 + 0*(2**2) + 3*(2**3) # 2 - 2 + 0 + 24 = 24
        self.assertEqual(evaluate_polynomial(xs, x), expected)

    def test_all_zero_coefficients(self):
        # P(x) = 0 + 0x + 0x^2, at any x
        xs = [0, 0, 0]
        x = 5
        self.assertEqual(evaluate_polynomial(xs, x), 0)

    def test_polynomial_with_float_x(self):
        # P(x) = x + x^2, at x=0.5
        xs = [0, 1, 1]
        x = 0.5
        expected = 0 + 1*0.5 + 1*(0.5**2) # 0.5 + 0.25 = 0.75
        self.assertAlmostEqual(evaluate_polynomial(xs, x), expected)

    def test_higher_degree_at_one(self):
        # P(x) = 1 + 2x + 3x^2 + 4x^3 + 5x^4, at x=1 (sum of coefficients)
        xs = [1, 2, 3, 4, 5]
        x = 1
        expected = 1 + 2 + 3 + 4 + 5 # 15
        self.assertEqual(evaluate_polynomial(xs, x), expected)

    def test_higher_degree_at_negative_one(self):
        # P(x) = 1 + 2x + 3x^2 + 4x^3 + 5x^4, at x=-1
        xs = [1, 2, 3, 4, 5]
        x = -1
        expected = 1 + 2*(-1) + 3*((-1)**2) + 4*((-1)**3) + 5*((-1)**4) # 1 - 2 + 3 - 4 + 5 = 3
        self.assertEqual(evaluate_polynomial(xs, x), expected)