import unittest

# Assume the function 'intersection' exists as described:
# def intersection(interval1, interval2):
#     """
#     Determines if the length of the intersection of two closed intervals
#     is a prime number.
#     Returns "YES" if the length is prime, "NO" otherwise or if no intersection.
#     """
#     # Implementation would go here.
#     # For these tests, we assume it's correctly implemented elsewhere.
#     pass


class TestIntersectionLengthPrime(unittest.TestCase):

    def test_1_intervals_touch_length_zero(self):
        # Intervals touch at a single point. Intersection (2,2), length 0. Not prime.
        self.assertEqual("NO", intersection((1, 2), (2, 3)))

    def test_2_overlap_length_one(self):
        # Standard overlap resulting in length 1. Not prime.
        self.assertEqual("NO", intersection((-1, 1), (0, 4)))

    def test_3_overlap_length_two_prime_with_negatives(self):
        # Overlap with negative numbers, resulting in length 2. 2 is prime.
        self.assertEqual("YES", intersection((-3, -1), (-5, 5)))

    def test_4_no_overlap_separated(self):
        # Intervals are completely separated with a gap. Length 0. Not prime.
        self.assertEqual("NO", intersection((10, 20), (1, 5)))

    def test_5_simple_overlap_length_two_prime(self):
        # Simple overlap, resulting in length 2. 2 is prime.
        self.assertEqual("YES", intersection((1, 5), (3, 7)))

    def test_6_one_interval_contains_other_length_three_prime(self):
        # One interval fully contains the other, length 3. 3 is prime.
        self.assertEqual("YES", intersection((1, 10), (4, 7)))

    def test_7_one_interval_contains_other_length_four_composite(self):
        # One interval fully contains the other, length 4. 4 is not prime.
        self.assertEqual("NO", intersection((1, 10), (4, 8)))

    def test_8_overlap_length_five_prime(self):
        # Overlap resulting in length 5. 5 is prime.
        self.assertEqual("YES", intersection((0, 10), (3, 8)))

    def test_9_no_overlap_separated_other_order(self):
        # Intervals are completely separated with a gap, order reversed from test_4. Length 0. Not prime.
        self.assertEqual("NO", intersection((0, 10), (11, 15)))

    def test_10_identical_intervals_length_zero(self):
        # Identical single-point intervals. Intersection (5,5), length 0. Not prime.
        self.assertEqual("NO", intersection((5, 5), (5, 5)))