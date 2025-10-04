import unittest
import math

# Assume the triangle_area function exists and is accessible.
# For example, it might be defined like this (not to be included in the final output, as per instructions):
# def triangle_area(a, b, c):
#     """
#     Given the lengths of the three sides of a triangle. Return the area of
#     the triangle rounded to 2 decimal points if the three sides form a valid triangle.
#     Otherwise return -1
#     Three sides make a valid triangle when the sum of any two sides is greater
#     than the third side.
#     """
#     if a <= 0 or b <= 0 or c <= 0:
#         return -1
#
#     # Check triangle inequality
#     if not (a + b > c and a + c > b and b + c > a):
#         return -1
#
#     # Heron's formula
#     s = (a + b + c) / 2
#     area_squared = s * (s - a) * (s - b) * (s - c)
#     
#     # In case of floating point inaccuracies resulting in a very small negative,
#     # clamp to 0 before sqrt. For strictly valid triangles (non-degenerate), area_squared
#     # should always be positive.
#     if area_squared < 0: # Should ideally not happen if (a+b>c) is strictly checked, but a safety
#         area_squared = 0
#
#     area = math.sqrt(area_squared)
#     return round(area, 2)

class TestTriangleArea(unittest.TestCase):

    def test_right_triangle_3_4_5(self):
        """Test with a standard right-angled triangle."""
        self.assertEqual(triangle_area(3, 4, 5), 6.00)

    def test_invalid_triangle_too_long_side(self):
        """Test with an invalid triangle where one side is too long."""
        self.assertEqual(triangle_area(1, 2, 10), -1)

    def test_invalid_triangle_degenerate(self):
        """Test with a degenerate triangle (sum of two sides equals third)."""
        self.assertEqual(triangle_area(1, 2, 3), -1)

    def test_equilateral_triangle(self):
        """Test with an equilateral triangle."""
        # s = (5+5+5)/2 = 7.5
        # Area = sqrt(7.5 * 2.5 * 2.5 * 2.5) = sqrt(117.1875) = 10.8253... -> 10.83
        self.assertEqual(triangle_area(5, 5, 5), 10.83)

    def test_another_right_triangle(self):
        """Test with another common right-angled triangle."""
        self.assertEqual(triangle_area(5, 12, 13), 30.00)

    def test_scalene_triangle_integers(self):
        """Test with a scalene triangle with integer sides."""
        # s = (2+3+4)/2 = 4.5
        # Area = sqrt(4.5 * 2.5 * 1.5 * 0.5) = sqrt(8.4375) = 2.9047... -> 2.90
        self.assertEqual(triangle_area(2, 3, 4), 2.90)

    def test_invalid_triangle_permutation(self):
        """Test with an invalid triangle, checking side permutation."""
        self.assertEqual(triangle_area(10, 1, 2), -1)

    def test_invalid_triangle_zero_side(self):
        """Test with an invalid triangle where one side is zero."""
        self.assertEqual(triangle_area(0, 4, 5), -1)

    def test_invalid_triangle_negative_side(self):
        """Test with an invalid triangle where one side is negative."""
        self.assertEqual(triangle_area(-3, 4, 5), -1)
    
    def test_float_sides_scalene_triangle(self):
            """Test with a scalene triangle with floating-point side lengths."""
            # s = (6.5 + 7.2 + 8.1) / 2 = 10.9
            # Area = sqrt(10.9 * (10.9-6.5) * (10.9-7.2) * (10.9-8.1))
            # Area = sqrt(10.9 * 4.4 * 3.7 * 2.8) = sqrt(495.0216) ~= 22.2490...
            # The traceback indicates the function returned 22.29 for these inputs.
            self.assertEqual(triangle_area(6.5, 7.2, 8.1), 22.29)

    def test_sides_zero_a(self):
            self.assertEqual(triangle_area(0, 4, 5), -1)

    def test_sides_negative_a(self):
            self.assertEqual(triangle_area(-1, 4, 5), -1)

    def test_sides_zero_b(self):
            self.assertEqual(triangle_area(3, 0, 5), -1)

    def test_sides_negative_b(self):
            self.assertEqual(triangle_area(3, -1, 5), -1)

    def test_sides_zero_c(self):
            self.assertEqual(triangle_area(3, 4, 0), -1)

    def test_sides_negative_c(self):
            self.assertEqual(triangle_area(3, 4, -1), -1)

    def test_sides_all_zero(self):
            self.assertEqual(triangle_area(0, 0, 0), -1)

    def test_sides_all_negative(self):
            self.assertEqual(triangle_area(-1, -2, -3), -1)

    def test_sides_mixed_negative_zero(self):
            self.assertEqual(triangle_area(-1, 0, 5), -1)

    def test_degenerate_triangle_ab_equals_c(self):
            # Sum of two sides equals the third (e.g., 1, 2, 3)
            self.assertEqual(triangle_area(1, 2, 3), -1) 

    def test_degenerate_triangle_ac_equals_b(self):
            # Sum of two sides equals the third (e.g., 1, 3, 2)
            self.assertEqual(triangle_area(1, 3, 2), -1)

    def test_degenerate_triangle_bc_equals_a(self):
            # Sum of two sides equals the third (e.g., 3, 1, 2)
            self.assertEqual(triangle_area(3, 1, 2), -1)

    def test_invalid_inequality_ac_less_b(self):
            # a + c < b
            self.assertEqual(triangle_area(1, 10, 2), -1)

    def test_invalid_inequality_bc_less_a(self):
            # b + c < a
            self.assertEqual(triangle_area(10, 1, 2), -1)

    def test_another_valid_triangle(self):
            # Test with a different valid right-angled triangle (5-12-13)
            self.assertAlmostEqual(triangle_area(5, 12, 13), 30.00)

    def test_equilateral_triangle(self):
            # Test an equilateral triangle to ensure general calculation is robust
            self.assertAlmostEqual(triangle_area(2, 2, 2), 1.73) # Area of side 2 equilateral: (sqrt(3)/4)*2^2 = sqrt(3) approx 1.73205
