from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transform to a list of numbers such that the smallest
    number becomes 0 and the largest becomes 1.

    Args:
        numbers: A list of numbers (float or int), guaranteed to have at least
                 two elements.

    Returns:
        A new list with the numbers rescaled to the [0.0, 1.0] range.

    Examples:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
        >>> rescale_to_unit([10, 20, 0])
        [0.5, 1.0, 0.0]
        >>> rescale_to_unit([5.0, 5.0, 5.0])
        [0.0, 0.0, 0.0]
        >>> rescale_to_unit([-1.0, 0.0, 1.0])
        [0.0, 0.5, 1.0]
    """
    if not numbers:
        # Although problem states "at least two elements", defensive programming
        # for empty list.
        return []

    min_val = min(numbers)
    max_val = max(numbers)

    data_range = max_val - min_val

    # Handle the edge case where all numbers are identical
    if data_range == 0:
        # If min_val == max_val, all elements are the same.
        # According to "smallest becomes 0", they all map to 0.0.
        return [0.0] * len(numbers)
    
    rescaled_list = []
    for num in numbers:
        # Linear transformation formula: (value - min) / (max - min)
        scaled_num = (num - min_val) / data_range
        rescaled_list.append(scaled_num)
        
    return rescaled_list