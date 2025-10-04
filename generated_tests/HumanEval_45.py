import unittest

class TestTriangleArea(unittest.TestCase):
    def test_example_case(self):
        self.assertAlmostEqual(triangle_area(5, 3), 7.5)

    def test_basic_integers(self):
        self.assertAlmostEqual(triangle_area(10, 4), 20.0)

    def test_positive_floats(self):
        self.assertAlmostEqual(triangle_area(5.5, 3.2), 8.8)

    def test_zero_side(self):
        self.assertAlmostEqual(triangle_area(0, 10), 0.0)

    def test_zero_high(self):
        self.assertAlmostEqual(triangle_area(10, 0), 0.0)

    def test_both_zero(self):
        self.assertAlmostEqual(triangle_area(0, 0), 0.0)

    def test_large_integers(self):
        self.assertAlmostEqual(triangle_area(1000, 500), 250000.0)

    def test_large_floats(self):
                self.assertAlmostEqual(triangle_area(1234.56, 789.12), 487107.9936)
    def test_small_floats(self):
        self.assertAlmostEqual(triangle_area(0.1, 0.2), 0.01)

    def test_mixed_integer_float(self):
        self.assertAlmostEqual(triangle_area(7, 2.5), 8.75)

    def test_triangle_area_negative_side(self):
            # Test case where side is negative, high is positive
            with self.assertRaises(ValueError) as cm:
                triangle_area(-5, 3)
            self.assertEqual(str(cm.exception), "Side and high must be non-negative values.")

    def test_triangle_area_negative_high(self):
            # Test case where side is positive, high is negative
            with self.assertRaises(ValueError) as cm:
                triangle_area(10, -4)
            self.assertEqual(str(cm.exception), "Side and high must be non-negative values.")

    def test_triangle_area_both_negative(self):
            # Test case where both side and high are negative
            with self.assertRaises(ValueError) as cm:
                triangle_area(-7, -2)
            self.assertEqual(str(cm.exception), "Side and high must be non-negative values.")
# Assuming triangle_area function is defined elsewhere, e.g.:
# def triangle_area(side, high):
#     return (side * high) / 2

if __name__ == '__main__':
    unittest.main()