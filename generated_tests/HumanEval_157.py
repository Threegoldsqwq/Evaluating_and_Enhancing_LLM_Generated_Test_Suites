import unittest

class TestRightAngleTriangle(unittest.TestCase):

    def test_basic_pythagorean_triple(self):
        # Classic 3-4-5 triangle
        self.assertTrue(right_angle_triangle(3, 4, 5))

    def test_another_pythagorean_triple(self):
        # Another common triple 5-12-13
        self.assertTrue(right_angle_triangle(5, 12, 13))

    def test_sides_out_of_order(self):
        # Sides given in a different order
        self.assertTrue(right_angle_triangle(4, 5, 3))

    def test_scaled_pythagorean_triple(self):
        # A scaled version of 3-4-5 (e.g., 6-8-10)
        self.assertTrue(right_angle_triangle(6, 8, 10))

    def test_non_right_triangle_generic(self):
        # A general triangle that is not right-angled
        self.assertFalse(right_angle_triangle(2, 3, 4))

    def test_degenerate_triangle(self):
        # A degenerate triangle (1+2=3) which is not right-angled
        self.assertFalse(right_angle_triangle(1, 2, 3))

    def test_equilateral_triangle(self):
        # An equilateral triangle (all angles 60 degrees)
        self.assertFalse(right_angle_triangle(2, 2, 2))

    def test_close_but_not_right(self):
        # A triangle very close to a right triangle but not exactly
        self.assertFalse(right_angle_triangle(6, 8, 9)) # 6^2+8^2=100, 9^2=81


    def test_floating_point_non_right_triangle(self):
        # Floating point sides not forming a right triangle
        self.assertFalse(right_angle_triangle(3.0, 4.0, 6.0)) # 3^2+4^2=25, 6^2=36
    def test_basic_right_angle_triangle_integers(self):
            # Covers the True branch with standard integer Pythagorean triples
            self.assertTrue(right_angle_triangle(3, 4, 5))
            self.assertTrue(right_angle_triangle(5, 12, 13))
            self.assertTrue(right_angle_triangle(8, 15, 17))

    def test_right_angle_triangle_with_unordered_sides(self):
            # Covers the True branch and implicitly checks that sorting works correctly
            self.assertTrue(right_angle_triangle(5, 3, 4))
            self.assertTrue(right_angle_triangle(13, 5, 12))
            self.assertTrue(right_angle_triangle(17, 8, 15))

    def test_right_angle_triangle_with_float_sides(self):
            # Covers the True branch with floating-point inputs
            self.assertTrue(right_angle_triangle(0.3, 0.4, 0.5))
            self.assertTrue(right_angle_triangle(6.0, 8.0, 10.0))
            # Example with a square root, for direct equality to work, use known exact values
            # For instance, a right isosceles triangle (1, 1, sqrt(2)) can't be exactly represented
            # without precision issues for direct equality unless we construct the 'hypotenuse'
            # based on exact squares. The current function uses direct `==`.
            # So we stick to numbers that result in exact squares.
            self.assertTrue(right_angle_triangle(1.5, 2.0, 2.5)) # (3/2, 4/2, 5/2)

    def test_not_right_angle_triangle_integers(self):
            # Covers the False branch with various non-right angle integer triangles
            self.assertFalse(right_angle_triangle(2, 3, 4))
            self.assertFalse(right_angle_triangle(7, 8, 9))
            self.assertFalse(right_angle_triangle(1, 1, 1)) # Equilateral triangle
            self.assertFalse(right_angle_triangle(5, 5, 6)) # Isosceles, not right

    def test_not_right_angle_triangle_float_sides(self):
            # Covers the False branch with various non-right angle float triangles
            self.assertFalse(right_angle_triangle(1.0, 1.0, 1.5))
            self.assertFalse(right_angle_triangle(2.5, 3.5, 4.5))

    def test_degenerate_triangle_conditions(self):
            # Tests cases that might be geometrically degenerate but processed by the code.
            # Sides form a line (e.g., 1+2=3), not a triangle, should return False.
            self.assertFalse(right_angle_triangle(1, 2, 3))
            self.assertFalse(right_angle_triangle(1, 1, 2))
            # Sides with zero length: (0, 3, 3) becomes [0, 3, 3]. 0^2 + 3^2 = 9. 3^2 = 9. True.
            # The function evaluates this as a right-angle degenerate triangle.
            self.assertTrue(right_angle_triangle(0, 3, 3))
            self.assertTrue(right_angle_triangle(3, 0, 3))
            self.assertTrue(right_angle_triangle(3, 3, 0)) # Checks sorting for zero

    def test_sides_with_negative_values(self):
            # Tests how the function handles negative inputs, as it doesn't validate for positive lengths.
            # The `sort()` function and `**2` operator will still produce numerical results.
            # Case 1: All sides negative. e.g., (-3, -4, -5) -> sorted [-5, -4, -3].
            # (-5)^2 + (-4)^2 = 25 + 16 = 41. (-3)^2 = 9. 41 != 9. False.
            self.assertFalse(right_angle_triangle(-3, -4, -5))
            self.assertFalse(right_angle_triangle(-5, -3, -4))

            # Case 2: Mixed signs, but mathematically forms a triple with absolute values.
            # e.g., (-3, -4, 5) -> sorted [-4, -3, 5].
            # (-4)^2 + (-3)^2 = 16 + 9 = 25. 5^2 = 25. True.
            self.assertTrue(right_angle_triangle(-3, -4, 5))
            self.assertTrue(right_angle_triangle(-4, -3, 5)) # Order doesn't matter due to sort

            # Case 3: One negative side, resulting in non-right angle calculation.
            # e.g., (3, 4, -5) -> sorted [-5, 3, 4].
            # (-5)^2 + 3^2 = 25 + 9 = 34. 4^2 = 16. 34 != 16. False.
            self.assertFalse(right_angle_triangle(3, 4, -5))

    def test_large_number_inputs(self):
            # Tests with larger numbers to ensure calculations hold
            self.assertTrue(right_angle_triangle(20000, 21000, 29000)) # Based on (20, 21, 29) triple
            self.assertFalse(right_angle_triangle(100000, 100001, 100002)) # Large non-right triangle
