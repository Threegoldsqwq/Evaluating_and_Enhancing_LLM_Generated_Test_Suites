import unittest

# Assume the function `count_collisions(l_positions, r_positions)` exists.
# It takes two lists of integers (or floats), representing the initial positions
# of cars moving left-to-right (l_positions) and right-to-left (r_positions).
# All cars move at the same speed. Two cars collide if a left-to-right car
# starts to the left of a right-to-left car. Cars pass through each other.

class TestCollisions(unittest.TestCase):

    def test_01_basic_example_case(self):
        # L = [1, 5], R = [2, 6]
        # L[0]=1 vs R[0]=2 (1<2, collision)
        # L[0]=1 vs R[1]=6 (1<6, collision)
        # L[1]=5 vs R[0]=2 (5<2, no collision)
        # L[1]=5 vs R[1]=6 (5<6, collision)
        # Total = 3 collisions
        l_positions = [1, 5]
        r_positions = [2, 6]
        self.assertEqual(count_collisions(l_positions, r_positions), 3)

    def test_02_n_equals_one(self):
        # Single L-R car, single R-L car
        # L = [0], R = [10] -> 0 < 10, collision (1)
        self.assertEqual(count_collisions([0], [10]), 1)
        # L = [10], R = [0] -> 10 < 0, no collision (0)
        self.assertEqual(count_collisions([10], [0]), 0)

    def test_03_no_collisions(self):
        # All L-R cars are initially to the right of all R-L cars.
        # No L-R car can ever be to the left of an R-L car.
        l_positions = [100, 110, 120]
        r_positions = [10, 20, 30]
        self.assertEqual(count_collisions(l_positions, r_positions), 0)

    def test_04_maximum_collisions(self):
        # All L-R cars are initially to the left of all R-L cars.
        # Each of the n L-R cars will collide with each of the n R-L cars.
        # Total = n * n collisions. Here n=3, so 3*3 = 9.
        l_positions = [1, 2, 3]
        r_positions = [10, 11, 12]
        self.assertEqual(count_collisions(l_positions, r_positions), 9)

    def test_05_mixed_positions_some_collide_some_dont(self):
        # L = [0, 5, 10], R = [2, 7, 8]
        # L[0]=0: vs R[0]=2(C), vs R[1]=7(C), vs R[2]=8(C) -> 3
        # L[1]=5: vs R[0]=2(NC), vs R[1]=7(C), vs R[2]=8(C) -> 2
        # L[2]=10: vs R[0]=2(NC), vs R[1]=7(NC), vs R[2]=8(NC) -> 0
        # Total = 3 + 2 + 0 = 5 collisions
        l_positions = [0, 5, 10]
        r_positions = [2, 7, 8]
        self.assertEqual(count_collisions(l_positions, r_positions), 5)

    def test_06_duplicate_positions_within_sets(self):
        # Cars can have identical starting positions within their own group.
        # L = [1, 1], R = [2, 2]
        # L[0]=1: vs R[0]=2(C), vs R[1]=2(C) -> 2
        # L[1]=1: vs R[0]=2(C), vs R[1]=2(C) -> 2
        # Total = 4 collisions
        l_positions = [1, 1]
        r_positions = [2, 2]
        self.assertEqual(count_collisions(l_positions, r_positions), 4)

    def test_07_negative_positions(self):
        # Test with negative coordinates.
        # L = [-5, -1], R = [-3, 0]
        # L[0]=-5: vs R[0]=-3(C), vs R[1]=0(C) -> 2
        # L[1]=-1: vs R[0]=-3(NC), vs R[1]=0(C) -> 1
        # Total = 3 collisions
        l_positions = [-5, -1]
        r_positions = [-3, 0]
        self.assertEqual(count_collisions(l_positions, r_positions), 3)

    def test_08_interspersed_positions(self):
        # Positions are heavily interleaved.
        # L = [1, 3, 5], R = [2, 4, 6]
        # L[0]=1: vs R[0]=2(C), R[1]=4(C), R[2]=6(C) -> 3
        # L[1]=3: vs R[0]=2(NC), R[1]=4(C), R[2]=6(C) -> 2
        # L[2]=5: vs R[0]=2(NC), R[1]=4(NC), R[2]=6(C) -> 1
        # Total = 3 + 2 + 1 = 6 collisions
        l_positions = [1, 3, 5]
        r_positions = [2, 4, 6]
        self.assertEqual(count_collisions(l_positions, r_positions), 6)

    def test_09_larger_n_complex_distribution(self):
        # Test with a larger number of cars (n=5) and a more complex distribution.
        # L = [1, 4, 6, 8, 10]
        # R = [2, 3, 5, 7, 9]
        # L[0]=1: vs R[0]=2(C), R[1]=3(C), R[2]=5(C), R[3]=7(C), R[4]=9(C) -> 5
        # L[1]=4: vs R[0]=2(NC), R[1]=3(NC), R[2]=5(C), R[3]=7(C), R[4]=9(C) -> 3
        # L[2]=6: vs R[0]=2(NC), R[1]=3(NC), R[2]=5(NC), R[3]=7(C), R[4]=9(C) -> 2
        # L[3]=8: vs R[0]=2(NC), R[1]=3(NC), R[2]=5(NC), R[3]=7(NC), R[4]=9(C) -> 1
        # L[4]=10: vs all R (NC) -> 0
        # Total = 5 + 3 + 2 + 1 + 0 = 11 collisions
        l_positions = [1, 4, 6, 8, 10]
        r_positions = [2, 3, 5, 7, 9]
        self.assertEqual(count_collisions(l_positions, r_positions), 11)

    def test_10_cars_start_at_same_point(self):
        # If cars start at the exact same point, they move away from each other.
        # A left-to-right car moves right, a right-to-left car moves left.
        # They do not "hit" in the sense of one travelling towards the other.
        # The condition L_pos < R_pos ensures this (strict inequality).
        l_positions = [0, 0]
        r_positions = [0, 0]
        self.assertEqual(count_collisions(l_positions, r_positions), 0)