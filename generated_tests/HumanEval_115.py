import unittest
import math

# Assume the function 'empty_wells' is defined elsewhere, e.g.:
# def empty_wells(grid: list[list[int]], bucket_capacity: int) -> int:
#     total_lowerings = 0
#     for row in grid:
#         water_in_well = sum(row)
#         if water_in_well > 0:
#             total_lowerings += math.ceil(water_in_well / bucket_capacity)
#     return total_lowerings

class TestEmptyWells(unittest.TestCase):

    def test_example_1(self):
        """Test with example 1 from the problem description."""
        grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
        bucket_capacity = 1
        # Well 1: 1 unit -> 1 lowering
        # Well 2: 1 unit -> 1 lowering
        # Well 3: 4 units -> 4 lowerings
        # Total: 1 + 1 + 4 = 6
        self.assertEqual(empty_wells(grid, bucket_capacity), 6)

    def test_example_2(self):
        """Test with example 2 from the problem description."""
        grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
        bucket_capacity = 2
        # Well 1: 2 units -> ceil(2/2) = 1 lowering
        # Well 2: 0 units -> 0 lowerings
        # Well 3: 4 units -> ceil(4/2) = 2 lowerings
        # Well 4: 3 units -> ceil(3/2) = 2 lowerings
        # Total: 1 + 0 + 2 + 2 = 5
        self.assertEqual(empty_wells(grid, bucket_capacity), 5)

    def test_example_3_empty_grid(self):
        """Test with all wells being empty."""
        grid = [[0,0,0], [0,0,0]]
        bucket_capacity = 5
        self.assertEqual(empty_wells(grid, bucket_capacity), 0)

    def test_single_well_capacity_one(self):
        """Test a single well with capacity 1."""
        grid = [[1,0,1,1]]
        bucket_capacity = 1
        # Well 1: 3 units -> 3 lowerings
        self.assertEqual(empty_wells(grid, bucket_capacity), 3)

    def test_single_well_perfect_division(self):
        """Test a single well where water is perfectly divisible by capacity."""
        grid = [[1,1,1,1,1,1]] # 6 units
        bucket_capacity = 3
        # Well 1: 6 units -> ceil(6/3) = 2 lowerings
        self.assertEqual(empty_wells(grid, bucket_capacity), 2)

    def test_single_well_with_remainder(self):
        """Test a single well where water leaves a remainder with capacity."""
        grid = [[1,1,1,1,1]] # 5 units
        bucket_capacity = 3
        # Well 1: 5 units -> ceil(5/3) = 2 lowerings
        self.assertEqual(empty_wells(grid, bucket_capacity), 2)

    def test_multiple_wells_mixed_division(self):
        """Test multiple wells with varying water amounts and capacity, some perfect, some remainder."""
        grid = [[1,0,1,0], [1,1,1,1], [0,0,1,1,1]]
        bucket_capacity = 3
        # Well 1 (2 units): ceil(2/3) = 1
        # Well 2 (4 units): ceil(4/3) = 2
        # Well 3 (3 units): ceil(3/3) = 1
        # Total: 1 + 2 + 1 = 4
        self.assertEqual(empty_wells(grid, bucket_capacity), 4)

    def test_all_wells_full_large_capacity(self):
        """Test a grid where all wells are full, and capacity is larger than individual well contents."""
        grid = [[1,1,1], [1,1,1], [1,1,1]] # 3 units per well
        bucket_capacity = 5 # Larger than any single well's content
        # Well 1 (3 units): ceil(3/5) = 1
        # Well 2 (3 units): ceil(3/5) = 1
        # Well 3 (3 units): ceil(3/5) = 1
        # Total: 1 + 1 + 1 = 3
        self.assertEqual(empty_wells(grid, bucket_capacity), 3)

    def test_large_grid_various_wells(self):
        """Test with a larger, more complex grid and medium capacity."""
        grid = [[1,1,0,0,1], [0,0,0,0,0], [1,1,1,1,1], [0,1,0,1,0], [1,1,1,1,0], [0,0,0,1,1]]
        bucket_capacity = 4
        # Well 1 (3 units): ceil(3/4) = 1
        # Well 2 (0 units): 0
        # Well 3 (5 units): ceil(5/4) = 2
        # Well 4 (2 units): ceil(2/4) = 1
        # Well 5 (4 units): ceil(4/4) = 1
        # Well 6 (2 units): ceil(2/4) = 1
        # Total: 1 + 0 + 2 + 1 + 1 + 1 = 6
        self.assertEqual(empty_wells(grid, bucket_capacity), 6)

    def test_max_constraints_with_mixed_water(self):
        """Test with grid dimensions near max constraints and mixed water levels."""
        # Grid: 3 rows, 100 columns
        grid = [
            [1] * 100,             # 100 units of water
            [1] * 50 + [0] * 50,   # 50 units of water
            [0] * 20 + [1] * 80    # 80 units of water
        ]
        bucket_capacity = 1
        # Well 1 (100 units): 100/1 = 100
        # Well 2 (50 units): 50/1 = 50
        # Well 3 (80 units): 80/1 = 80
        # Total: 100 + 50 + 80 = 230
        self.assertEqual(empty_wells(grid, bucket_capacity), 230)

    def test_empty_grid(self):
            # Test case for an empty grid, expecting 0 total lowerings.
            # Ensures the loop handles an empty iterable correctly.
            grid = []
            bucket_capacity = 5
            self.assertEqual(empty_wells(grid, bucket_capacity), 0)

    def test_grid_with_only_empty_wells(self):
            # Test case for a grid containing only empty wells.
            # This covers the 'if water_in_well > 0:' condition evaluating to False
            # for all wells, ensuring no lowerings are counted.
            grid = [[0, 0], [], [0, 0, 0]]
            bucket_capacity = 3
            self.assertEqual(empty_wells(grid, bucket_capacity), 0)

    def test_mixed_empty_and_non_empty_wells(self):
            # Test case with a mix of empty and non-empty wells.
            # This ensures both branches of 'if water_in_well > 0:' are exercised.
            # Also tests different water amounts and bucket capacities.
            grid = [
                [1, 0, 1],       # water_in_well = 2
                [0, 0],          # water_in_well = 0
                [1, 1, 1, 1]     # water_in_well = 4
            ]
            bucket_capacity = 3
            # Well 1: 2 units, capacity 3 -> ceil(2/3) = 1 lowering
            # Well 2: 0 units, capacity 3 -> 0 lowerings
            # Well 3: 4 units, capacity 3 -> ceil(4/3) = 2 lowerings
            # Total = 1 + 0 + 2 = 3
            self.assertEqual(empty_wells(grid, bucket_capacity), 3)

    def test_bucket_capacity_one(self):
            # Test case where bucket capacity is 1, ensuring each unit of water
            # requires a separate lowering.
            grid = [
                [1, 1],        # water_in_well = 2
                [1, 0, 1, 1]   # water_in_well = 3
            ]
            bucket_capacity = 1
            # Well 1: 2 units, capacity 1 -> ceil(2/1) = 2 lowerings
            # Well 2: 3 units, capacity 1 -> ceil(3/1) = 3 lowerings
            # Total = 2 + 3 = 5
            self.assertEqual(empty_wells(grid, bucket_capacity), 5)

    def test_large_bucket_capacity(self):
            # Test case where bucket capacity is larger than water in any well.
            # Each non-empty well should require exactly one lowering.
            grid = [
                [1],           # water_in_well = 1
                [1, 1, 1],     # water_in_well = 3
                [0,0,0,0,1,1]  # water_in_well = 2
            ]
            bucket_capacity = 10
            # Well 1: 1 unit, capacity 10 -> ceil(1/10) = 1 lowering
            # Well 2: 3 units, capacity 10 -> ceil(3/10) = 1 lowering
            # Well 3: 2 units, capacity 10 -> ceil(2/10) = 1 lowering
            # Total = 1 + 1 + 1 = 3
            self.assertEqual(empty_wells(grid, bucket_capacity), 3)

    def test_well_water_exactly_divisible_by_capacity(self):
            # Test case where water_in_well is perfectly divisible by bucket_capacity,
            # ensuring ceiling division behaves as expected (e.g., 6/2 = 3).
            grid = [
                [1,1,1,1,1,1], # water_in_well = 6
                [1,1]          # water_in_well = 2
            ]
            bucket_capacity = 2
            # Well 1: 6 units, capacity 2 -> ceil(6/2) = 3 lowerings
            # Well 2: 2 units, capacity 2 -> ceil(2/2) = 1 lowering
            # Total = 3 + 1 = 4
            self.assertEqual(empty_wells(grid, bucket_capacity), 4)

    def test_well_water_not_exactly_divisible_by_capacity(self):
            # Test case where water_in_well is not perfectly divisible by bucket_capacity,
            # ensuring ceiling division correctly rounds up (e.g., 5/2 = 2.5 rounds to 3).
            grid = [
                [1,1,1,1,1], # water_in_well = 5
                [1,1,1,1]    # water_in_well = 4
            ]
            bucket_capacity = 2
            # Well 1: 5 units, capacity 2 -> ceil(5/2) = 3 lowerings
            # Well 2: 4 units, capacity 2 -> ceil(4/2) = 2 lowerings
            # Total = 3 + 2 = 5
            self.assertEqual(empty_wells(grid, bucket_capacity), 5)
if __name__ == '__main__':
    # This is a placeholder for the actual function.
    # In a real scenario, this function would be imported or defined here.
    # def empty_wells(grid: list[list[int]], bucket_capacity: int) -> int:
    #     total_lowerings = 0
    #     for row in grid:
    #         water_in_well = sum(row)
    #         if water_in_well > 0:
    #             total_lowerings += math.ceil(water_in_well / bucket_capacity)
    #     return total_lowerings

    unittest.main(argv=['first-arg-is-ignored'], exit=False)