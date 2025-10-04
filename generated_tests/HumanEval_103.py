import unittest

class TestRoundedAvg(unittest.TestCase):

    def test_n_greater_than_m(self):
        # Test case where n is greater than m
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(100, 99), -1)

    def test_n_equals_m(self):
        # Test case where n equals m, average is n
        self.assertEqual(rounded_avg(7, 7), "0b111") # Avg 7, Rounded 7, Binary 0b111
        self.assertEqual(rounded_avg(1, 1), "0b1")   # Avg 1, Rounded 1, Binary 0b1

    def test_average_is_integer(self):
        # Test case where the average is a whole number (no rounding needed)
        self.assertEqual(rounded_avg(1, 5), "0b11")     # Avg 3, Rounded 3, Binary 0b11
        self.assertEqual(rounded_avg(10, 20), "0b1111") # Avg 15, Rounded 15, Binary 0b1111
        self.assertEqual(rounded_avg(4, 8), "0b110")    # Avg 6, Rounded 6, Binary 0b110

    def test_average_ends_in_point_five_rounds_to_even_down(self):
        # Test case where average ends in .5 and rounds down to the nearest even integer
        # e.g., round(2.5) == 2 (2 is even)
        self.assertEqual(rounded_avg(2, 3), "0b10")     # Avg 2.5, Rounded 2, Binary 0b10
        self.assertEqual(rounded_avg(20, 33), "0b11010") # Avg 26.5, Rounded 26, Binary 0b11010

    def test_average_ends_in_point_five_rounds_to_even_up(self):
        # Test case where average ends in .5 and rounds up to the nearest even integer
        # e.g., round(1.5) == 2 (2 is even)
        # e.g., round(3.5) == 4 (4 is even)
        self.assertEqual(rounded_avg(1, 2), "0b10")   # Avg 1.5, Rounded 2, Binary 0b10
        self.assertEqual(rounded_avg(3, 4), "0b100")  # Avg 3.5, Rounded 4, Binary 0b100
        self.assertEqual(rounded_avg(99, 100), "0b1100100") # Avg 99.5, Rounded 100, Binary 0b1100100

    def test_larger_numbers(self):
        # Test case with larger input numbers
        self.assertEqual(rounded_avg(100, 200), "0b10010110") # Avg 150, Rounded 150, Binary 0b10010110

    def test_another_n_greater_than_m(self):
        # Another test for n > m
        self.assertEqual(rounded_avg(50, 49), -1)

    def test_consecutive_numbers_even_sum(self):
        # Average of consecutive numbers where sum is even (integer result)
        self.assertEqual(rounded_avg(5, 7), "0b110") # Avg 6, Rounded 6, Binary 0b110

    def test_consecutive_numbers_odd_sum(self):
        # Average of consecutive numbers where sum is odd (X.5 result)
        self.assertEqual(rounded_avg(6, 7), "0b110") # Avg 6.5, Rounded 6, Binary 0b110 (round half to even)

    def test_wide_range_average_integer(self):
        # Test with a wider range where average is an integer
        self.assertEqual(rounded_avg(1, 19), "0b1010") # Avg (1+19)/2 = 10, Rounded 10, Binary 0b1010
    def test_n_greater_than_m(self):
            # Test case for the branch where n > m, expecting -1
            self.assertEqual(rounded_avg(5, 1), -1)
            self.assertEqual(rounded_avg(10, 0), -1)
            self.assertEqual(rounded_avg(2, 1), -1)
