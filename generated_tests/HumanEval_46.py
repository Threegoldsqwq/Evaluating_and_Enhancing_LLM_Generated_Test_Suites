import unittest

# Assume the fib4 function exists and is imported or defined elsewhere.
# For the purpose of running these tests independently, a mock fib4 function is provided.
# In a real scenario, you would remove this mock and ensure the actual fib4 is available.

# --- MOCK fib4 FUNCTION (DO NOT INCLUDE IN FINAL SUBMISSION IF fib4 IS ALREADY DEFINED) ---
# This is just for local testing of the test cases themselves.
# def fib4(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 0
#     if n == 2:
#         return 2
#     if n == 3:
#         return 0
#     if n < 0:
#         raise ValueError("Input must be a non-negative integer")
#
#     a, b, c, d = 0, 0, 2, 0  # fib4(0), fib4(1), fib4(2), fib4(3)
#     for _ in range(4, n + 1):
#         next_fib = d + c + b + a
#         a, b, c, d = b, c, d, next_fib
#     return d
# --- END MOCK FUNCTION ---


class TestFib4(unittest.TestCase):

    def test_fib4_0(self):
        self.assertEqual(fib4(0), 0)

    def test_fib4_1(self):
        self.assertEqual(fib4(1), 0)

    def test_fib4_2(self):
        self.assertEqual(fib4(2), 2)

    def test_fib4_3(self):
        self.assertEqual(fib4(3), 0)

    def test_fib4_4(self):
        # fib4(4) = fib4(3) + fib4(2) + fib4(1) + fib4(0) = 0 + 2 + 0 + 0 = 2
        self.assertEqual(fib4(4), 2)

    def test_fib4_5(self):
        # fib4(5) = fib4(4) + fib4(3) + fib4(2) + fib4(1) = 2 + 0 + 2 + 0 = 4
        self.assertEqual(fib4(5), 4)

    def test_fib4_6(self):
        # fib4(6) = fib4(5) + fib4(4) + fib4(3) + fib4(2) = 4 + 2 + 0 + 2 = 8
        self.assertEqual(fib4(6), 8)

    def test_fib4_7(self):
        # fib4(7) = fib4(6) + fib4(5) + fib4(4) + fib4(3) = 8 + 4 + 2 + 0 = 14
        self.assertEqual(fib4(7), 14)

    def test_fib4_8(self):
        # fib4(8) = fib4(7) + fib4(6) + fib4(5) + fib4(4) = 14 + 8 + 4 + 2 = 28
        self.assertEqual(fib4(8), 28)

    def test_fib4_12(self):
        # fib4(9) = 28 + 14 + 8 + 4 = 54
        # fib4(10) = 54 + 28 + 14 + 8 = 104
        # fib4(11) = 104 + 54 + 28 + 14 = 200
        # fib4(12) = 200 + 104 + 54 + 28 = 386
        self.assertEqual(fib4(12), 386)

    def test_fib4_extended_sequence(self):
            """Test fib4 for larger values of n beyond docstring examples."""
            self.assertEqual(fib4(8), 28)
            self.assertEqual(fib4(9), 54)
            self.assertEqual(fib4(10), 104)
            self.assertEqual(fib4(11), 200) # 28 + 54 + 104 + 14 = 200, (fib4(8)+fib4(9)+fib4(10)+fib4(7))

    def test_fib4_negative_input(self):
            """
            Test fib4 with negative integer input.
            The function definition specifies 'non-negative integer' for n.
            However, the current implementation implicitly handles negative 'n' by
            skipping the loop and returning 0, which is an execution path.
            This test covers that specific behavior.
            """
            self.assertEqual(fib4(-1), 0)
            self.assertEqual(fib4(-5), 0)
            self.assertEqual(fib4(-100), 0)

    def test_fib4_non_integer_input(self):
            """
            Test fib4 with non-integer input to cover implicit type checking.
            The `range()` function expects integer arguments, so passing a non-integer
            for `n` will cause a TypeError, covering this implicit error path
            related to the function's argument type hint.
            """
            # Test with float, which will cause TypeError in range(4, n+1)
            with self.assertRaises(TypeError):
                fib4(4.0)
            with self.assertRaises(TypeError):
                fib4(5.5)

            # Test with string, will cause TypeError in "abc" + 1 or range(4, str)
            with self.assertRaises(TypeError):
                fib4("abc")

            # Test with other invalid types
            with self.assertRaises(TypeError):
                fib4([1, 2])
            with self.assertRaises(TypeError):
                fib4(None)
# To run these tests:
# if __name__ == '__main__':
#     # If running directly, make sure fib4 function is defined or imported.
#     # For example, if fib4 is in a file named 'fib4_solver.py':
#     # from fib4_solver import fib4
#     unittest.main(argv=['first-arg-is-ignored'], exit=False)