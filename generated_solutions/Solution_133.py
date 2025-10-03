import math

def sum_of_ceiling_squares(lst: list[float]) -> int:
    """
    Calculates the sum of squared numbers after rounding each element
    in the list to the upper integer (ceiling).

    Args:
        lst: A list of numbers (integers or floats).

    Returns:
        The sum of the squares of the ceiling-rounded numbers.
    """
    total_sum = 0
    for number in lst:
        # Step 1: Round the number up to the nearest integer (ceiling)
        ceiled_number = math.ceil(number)
        
        # Step 2: Square the ceiled number
        squared_number = ceiled_number ** 2
        
        # Step 3: Add the squared number to the total sum
        total_sum += squared_number
        
    return total_sum