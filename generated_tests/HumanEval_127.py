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
    def test_is_prime_edge_cases(self):
            # Covers n <= 1 branch (line 10)
            self.assertFalse(is_prime(1), "1 should not be prime")
            self.assertFalse(is_prime(0), "0 should not be prime")
            self.assertFalse(is_prime(-5), "Negative numbers should not be prime")

            # Covers n == 2 branch (line 12)
            self.assertTrue(is_prime(2), "2 should be prime")

            # Covers n % 2 == 0 branch (line 14) for n > 2
            self.assertFalse(is_prime(4), "4 should not be prime")
            self.assertFalse(is_prime(6), "6 should not be prime")
            self.assertFalse(is_prime(100), "100 should not be prime")

    def test_is_prime_odd_composites(self):
            # Covers while loop and n % i == 0 returning False (lines 19-20)
            self.assertFalse(is_prime(9), "9 should not be prime (3*3)")
            self.assertFalse(is_prime(15), "15 should not be prime (3*5)")
            self.assertFalse(is_prime(25), "25 should not be prime (5*5)")
            self.assertFalse(is_prime(49), "49 should not be prime (7*7)")
            self.assertFalse(is_prime(77), "77 should not be prime (7*11)")

    def test_is_prime_odd_primes(self):
            # Covers while loop completing and returning True (line 22)
            # Cases where loop does not run (i*i > n immediately)
            self.assertTrue(is_prime(3), "3 should be prime")
            self.assertTrue(is_prime(5), "5 should be prime")
            self.assertTrue(is_prime(7), "7 should be prime")

            # Cases where loop runs but finds no divisors
            self.assertTrue(is_prime(13), "13 should be prime")
            self.assertTrue(is_prime(17), "17 should be prime")
            self.assertTrue(is_prime(23), "23 should be prime")
            self.assertTrue(is_prime(97), "97 should be prime") # Larger prime

    def test_intersection_no_overlap(self):
            # Covers intersect_start > intersect_end branch (line 42)
            self.assertEqual(intersection((1, 2), (3, 4)), "NO", "No overlap, interval1 before interval2")
            self.assertEqual(intersection((3, 4), (1, 2)), "NO", "No overlap, interval1 after interval2")
            # No overlap with negative numbers
            self.assertEqual(intersection((-10, -8), (-5, -2)), "NO", "No overlap with negative intervals")

    def test_intersection_length_zero(self):
            # Covers cases where length is 0 (is_prime(0) -> False -> NO)
            self.assertEqual(intersection((1, 5), (5, 10)), "NO", "Touching intervals, length 0")
            self.assertEqual(intersection((5, 10), (1, 5)), "NO", "Touching intervals, length 0 (reversed)")
            self.assertEqual(intersection((5, 5), (5, 5)), "NO", "Point intervals, length 0")
            self.assertEqual(intersection((1, 1), (1, 1)), "NO", "Another point interval, length 0")

    def test_intersection_length_one(self):
            # Covers cases where length is 1 (is_prime(1) -> False -> NO)
            self.assertEqual(intersection((1, 6), (5, 10)), "NO", "Length 1 intersection (5,6)")
            self.assertEqual(intersection((0, 1), (0, 1)), "NO", "Identical interval, length 1 (0,1)")

    def test_intersection_prime_length(self):
            # Covers is_prime(length) returning True (line 48)
            self.assertEqual(intersection((1, 5), (3, 7)), "YES", "Length 2 intersection (3,5)")
            self.assertEqual(intersection((1, 7), (4, 9)), "YES", "Length 3 intersection (4,7)")
            self.assertEqual(intersection((0, 10), (5, 15)), "YES", "Length 5 intersection (5,10)")
            self.assertEqual(intersection((-5, 0), (-2, 3)), "YES", "Length 2 intersection with negative numbers (-2,0)")
            self.assertEqual(intersection((-10, -5), (-7, -2)), "YES", "Length 2 intersection with negative numbers (-7,-5)")
            self.assertEqual(intersection((1, 3), (1, 3)), "YES", "Identical interval, length 2 (1,3)")

    def test_intersection_composite_length(self):
            # Covers is_prime(length) returning False (line 50)
            self.assertEqual(intersection((1, 10), (3, 7)), "NO", "Length 4 intersection (3,7)")
            self.assertEqual(intersection((0, 10), (2, 8)), "NO", "Length 6 intersection (2,8)")
            self.assertEqual(intersection((0, 10), (0, 10)), "NO", "Identical interval, length 10")
            self.assertEqual(intersection((-5, 5), (-2, 2)), "NO", "Length 4 intersection with negative numbers (-2,2)")
