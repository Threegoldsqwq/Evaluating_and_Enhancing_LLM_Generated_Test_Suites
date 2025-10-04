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