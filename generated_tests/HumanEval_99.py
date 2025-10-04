import unittest

class TestClosestInteger(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(closest_integer("10"), 10)

    def test_positive_round_down(self):
        self.assertEqual(closest_integer("15.3"), 15)

    def test_negative_round_down_abs(self): # Effectively rounds towards zero
        self.assertEqual(closest_integer("-15.3"), -15)

    def test_positive_equidistant(self): # Rounds away from zero
        self.assertEqual(closest_integer("14.5"), 15)

    def test_negative_equidistant(self): # Rounds away from zero
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_zero(self):
        self.assertEqual(closest_integer("0"), 0)

    def test_small_positive_equidistant(self):
        self.assertEqual(closest_integer("0.5"), 1)

    def test_small_negative_equidistant(self):
        self.assertEqual(closest_integer("-0.5"), -1)

    def test_positive_round_up(self):
        self.assertEqual(closest_integer("15.7"), 16)

    def test_negative_round_up_abs(self): # Effectively rounds away from zero
        self.assertEqual(closest_integer("-15.7"), -16)
    def test_positive_numbers_round_down(self):
            # Covers fractional_part < 0.5, positive f_num
            self.assertEqual(closest_integer("10.3"), 10)
            self.assertEqual(closest_integer("0.1"), 0)
            self.assertEqual(closest_integer("15.49"), 15) # Just under .5

    def test_positive_numbers_round_up(self):
            # Covers fractional_part > 0.5, positive f_num
            self.assertEqual(closest_integer("10.7"), 11)
            self.assertEqual(closest_integer("0.9"), 1)
            self.assertEqual(closest_integer("15.51"), 16) # Just over .5

    def test_positive_numbers_round_half_away_from_zero(self):
            # Covers fractional_part == 0.5 and f_num >= 0 (rounds up)
            self.assertEqual(closest_integer("10.5"), 11)
            self.assertEqual(closest_integer("0.5"), 1)
            self.assertEqual(closest_integer("14.5"), 15)

    def test_negative_numbers_round_down(self):
            # Covers fractional_part < 0.5, negative f_num
            # Example: -14.7 -> floor(-14.7) = -15. fractional_part = -14.7 - (-15) = 0.3 < 0.5 -> -15
            self.assertEqual(closest_integer("-14.7"), -15)
            self.assertEqual(closest_integer("-0.1"), 0) # f_num=-0.1, floor=-1, frac_part=0.9 > 0.5 -> 0. This is a round up case.
                                                         # Correct test for round down (fractional_part < 0.5):
            self.assertEqual(closest_integer("-10.9"), -11) # f_num=-10.9, floor=-11, frac_part=0.1 < 0.5 -> -11
            self.assertEqual(closest_integer("-2.99"), -3) # f_num=-2.99, floor=-3, frac_part=0.01 < 0.5 -> -3

    def test_negative_numbers_round_up(self):
            # Covers fractional_part > 0.5, negative f_num
            # Example: -14.3 -> floor(-14.3) = -15. fractional_part = -14.3 - (-15) = 0.7 > 0.5 -> -14
            self.assertEqual(closest_integer("-14.3"), -14)
            self.assertEqual(closest_integer("-0.3"), 0)
            self.assertEqual(closest_integer("-1.1"), -1)
            self.assertEqual(closest_integer("-10.01"), -10) # f_num=-10.01, floor=-11, frac_part=0.99 > 0.5 -> -10

    def test_negative_numbers_round_half_away_from_zero(self):
            # Covers fractional_part == 0.5 and f_num < 0 (rounds down)
            self.assertEqual(closest_integer("-10.5"), -11)
            self.assertEqual(closest_integer("-0.5"), -1)
            self.assertEqual(closest_integer("-14.5"), -15)

    def test_exact_integers(self):
            # Covers cases where the input is an integer (positive, negative, zero)
            self.assertEqual(closest_integer("0"), 0)
            self.assertEqual(closest_integer("0.0"), 0)
            self.assertEqual(closest_integer("123"), 123)
            self.assertEqual(closest_integer("-456"), -456)

    def test_edge_cases_floating_point_precision(self):
            # Test values very close to .5 boundaries due to float precision
            self.assertEqual(closest_integer("10.4999999999999999"), 10) # Should round down
            self.assertEqual(closest_integer("10.5000000000000001"), 11) # Should round up
            self.assertEqual(closest_integer("-10.4999999999999999"), -10) # frac_part approx 0.50..01 -> round up (-10)
            self.assertEqual(closest_integer("-10.5000000000000001"), -11) # frac_part approx 0.49..99 -> round down (-11)

    def test_large_and_small_numbers(self):
            # Test with very large and very small numbers
            self.assertEqual(closest_integer("1.23e+20"), 123000000000000000000)
            self.assertEqual(closest_integer("-1.23e+20"), -123000000000000000000)
            self.assertEqual(closest_integer("1.23e-10"), 0) # Closer to 0
            self.assertEqual(closest_integer("-1.23e-10"), 0) # Closer to 0
            self.assertEqual(closest_integer("12345678901234567890.5"), 12345678901234567891)
            self.assertEqual(closest_integer("-12345678901234567890.5"), -12345678901234567891)

    def test_invalid_string_input(self):
            # Test non-numeric string inputs which should raise ValueError from float()
            with self.assertRaises(ValueError):
                closest_integer("not_a_number")
            with self.assertRaises(ValueError):
                closest_integer("abc1.23")
            with self.assertRaises(ValueError):
                closest_integer("") # Empty string is not a valid float

    def test_non_string_input_type(self):
            # Test non-string input types which should raise TypeError from float()
            with self.assertRaises(TypeError):
                closest_integer(12.3) # Integer input instead of string
            with self.assertRaises(TypeError):
                closest_integer(None)
            with self.assertRaises(TypeError):
                closest_integer([10.5])
