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