import math

def empty_wells(grid: list[list[int]], bucket_capacity: int) -> int:
    """
    Calculates the total number of times buckets need to be lowered to empty all wells.

    Args:
        grid: A rectangular grid where each row represents a well and 1s represent
              units of water.
        bucket_capacity: The capacity of each bucket.

    Returns:
        The total number of times buckets need to be lowered.
    """
    total_bucket_lowerings = 0

    for well in grid:
        water_in_well = sum(well)  # Count the 1s to find total water in the current well

        if water_in_well > 0:
            # Calculate the number of times the bucket needs to be lowered for this well.
            # This is equivalent to ceil(water_in_well / bucket_capacity).
            # Using integer division: (numerator + denominator - 1) // denominator
            # handles the ceiling division correctly for positive numbers.
            lowerings_for_this_well = (water_in_well + bucket_capacity - 1) // bucket_capacity
            total_bucket_lowerings += lowerings_for_this_well
            
    return total_bucket_lowerings