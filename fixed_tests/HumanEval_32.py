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
            # The `find_zero` function is designed for odd-degree polynomials,
            # which means the list of coefficients `xs` must have an even length.
            # A constant polynomial like P(x) = 5 (coefficients xs = [5])
            # has degree 0, and its coefficient list has an odd length (1).
            # Therefore, calling `find_zero` with `xs = [5]` should raise a ValueError
            # due to the input constraints.
            xs = [5]
            with self.assertRaises(ValueError) as cm:
                find_zero(xs)
            self.assertIn("even number of elements", str(cm.exception))
    def test_linear_polynomial_at_zero(self):
            # For P(x) = 3 + 2x, the root (x where P(x)=0) is at x = -1.5
            xs = [3, 2]
            expected_root = -1.5
            # The find_zero function calculates the root of the polynomial.
            # We use assertAlmostEqual for float comparison due to numerical methods.
            self.assertAlmostEqual(find_zero(xs), expected_root, places=7)
    def test_linear_polynomial_at_one(self):
            # For the polynomial P(x) = 3 + 2x, find_zero should return its root.
            # The root is when 3 + 2x = 0, which means 2x = -3, so x = -1.5.
            xs = [3, 2] # Represents P(x) = 3 + 2x
            expected_root = -1.5

            # Call the function under test: find_zero
            actual_root = find_zero(xs)

            # Assert that the returned root is approximately the expected value.
            # Using assertAlmostEqual for float comparisons.
            self.assertAlmostEqual(actual_root, expected_root, places=7) # Using a reasonable precision
    def test_quadratic_polynomial_positive_x(self):
            # The function `find_zero` is designed to find roots for odd-degree polynomials.
            # It explicitly requires the length of the coefficients list (degree + 1) to be an even number.
            # A quadratic polynomial (degree 2) has 3 coefficients, meaning `len(xs)` is 3, which is an odd number.
            # Therefore, calling `find_zero` with coefficients for a quadratic polynomial is expected to raise a ValueError,
            # as it violates the function's input constraints.
            xs = [1, -4, 1] # Coefficients for x^2 - 4x + 1 (a quadratic polynomial)

            with self.assertRaisesRegex(ValueError, "Input coefficients list must be non-empty and have an even number of elements."):
                find_zero(xs)
    def test_quadratic_polynomial_negative_x(self):
                # The function `find_zero` requires an odd-degree polynomial,
                # meaning the length of the coefficients list `xs` must be an even number.
                # The original test attempted a quadratic polynomial (degree 2), which has
                # an odd number of coefficients (length 3), violating `find_zero`'s constraint.
                #
                # We need to test `find_zero` with an odd-degree polynomial that has a negative root,
                # and ideally only one real root, to ensure the bisection method converges to it.
                # Let's use a cubic polynomial: P(x) = x^3 + 1
                # This polynomial has one real root at x = -1.
                # The coefficients are [constant, x^1, x^2, x^3] = [1, 0, 0, 1].
                # Length of xs is 4 (even), so it satisfies `find_zero`'s input constraints.

                xs = [1, 0, 0, 1]  # Coefficients for P(x) = x^3 + 1
                expected_root = -1.0 # The single real root is -1.0

                # `find_zero` returns a float, and internally uses a tolerance.
                # `assertAlmostEqual` is appropriate for comparing float results.
                # We use `places=7` to accommodate the internal tolerance of 1e-8.
                self.assertAlmostEqual(find_zero(xs), expected_root, places=7)
    def test_cubic_polynomial_mixed_coefficients(self):
            # P(x) = 2 - x + 0x^2 + 3x^3.
            # We need to find a root for this polynomial, not evaluate it at a specific x.
            # Let's check x = -1: P(-1) = 2 - (-1) + 0*(-1)^2 + 3*(-1)^3 = 2 + 1 + 0 - 3 = 0.
            # So, x = -1 is a root for this polynomial.
            xs = [2, -1, 0, 3]
            expected_root = -1.0

            # Call the function under test, which is find_zero, to find a root.
            actual_root = find_zero(xs)

            # Assert that the found root is almost equal to the expected root due to floating point precision.
            self.assertAlmostEqual(actual_root, expected_root, delta=1e-5)
    def test_all_zero_coefficients(self):
            # The input xs = [0, 0, 0] has an odd number of coefficients (3).
            # The function `find_zero` explicitly raises a ValueError if `len(xs)` is not an even number.
            # Therefore, this test should assert that a ValueError is raised for this input.
            xs = [0, 0, 0]
            with self.assertRaises(ValueError):
                find_zero(xs)
    def test_polynomial_with_float_x(self):
            # The function under test is 'find_zero'.
            # 'find_zero' expects a polynomial with an even number of coefficients
            # and returns a root, not an evaluation.

            # P(x) = 1 + 2x, which has coefficients [1, 2].
            # The length of xs (2) is even, satisfying the constraint for find_zero.
            # The root for 1 + 2x = 0 is x = -0.5.

            xs = [1, 2]
            expected_root = -0.5

            # Call the actual function under test, which is 'find_zero'.
            actual_root = find_zero(xs)

            # Assert that the found root is almost equal to the expected root.
            # find_zero uses a tolerance of 1e-8.
            self.assertAlmostEqual(actual_root, expected_root, places=7)
    def test_higher_degree_at_one(self):
                # The function under test, find_zero, is designed to find roots of polynomials.
                # It requires the polynomial to be of odd degree (i.e., an even number of coefficients).
                # P(x) = (x - 1)^3 = x^3 - 3x^2 + 3x - 1 is an odd-degree polynomial (degree 3).
                # This polynomial has a single real root at x=1.
                # Coefficients are [a0, a1, a2, a3] where a0 is the constant term.
                xs = [-1, 3, -3, 1] # Corresponds to x^3 - 3x^2 + 3x - 1
                expected_root = 1.0

                # Call find_zero to find a root of the polynomial
                actual_root = find_zero(xs)

                # Use assertAlmostEqual for float comparisons, considering the internal tolerance
                self.assertAlmostEqual(actual_root, expected_root, places=6)
    def test_higher_degree_at_negative_one(self):
            # P(x) = x^3 + x^2 + x + 1, which has a root at x = -1.
            # This polynomial is (x+1)(x^2+1).
            # Coefficients [a0, a1, a2, a3] are [1, 1, 1, 1].
            # The length of xs (4) is even, satisfying the function's constraint.
            xs = [1, 1, 1, 1]
            expected_root = -1.0

            # The function under test, find_zero, finds a root, not evaluates a polynomial.
            # Use assertAlmostEqual for floating point comparison of the root.
            self.assertAlmostEqual(find_zero(xs), expected_root, delta=1e-6)
