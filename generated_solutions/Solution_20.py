import math

def find_closest_elements(numbers: list) -> tuple:
    """
    From a supplied list of numbers (of length at least two) select and return
    two that are the closest to each other and return them in order
    (smaller number, larger number).

    Args:
        numbers: A list of numbers (integers or floats), of length at least two.

    Returns:
        A tuple containing the two closest numbers in (smaller, larger) order.

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
        >>> find_closest_elements([10, 5, 12, 8])
        (8, 10)
        >>> find_closest_elements([1, 100])
        (1, 100)
        >>> find_closest_elements([3, 1, 2])
        (1, 2)
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers.")

    # Sort the list of numbers. This is crucial as it ensures that
    # the closest elements will be adjacent to each other.
    sorted_numbers = sorted(numbers)

    min_diff = float('inf')  # Initialize with a very large difference
    closest_pair = (None, None)

    # Iterate through the sorted list, comparing adjacent elements
    for i in range(len(sorted_numbers) - 1):
        num1 = sorted_numbers[i]
        num2 = sorted_numbers[i+1]
        current_diff = abs(num2 - num1)

        # If the current difference is smaller than min_diff, update
        if current_diff < min_diff:
            min_diff = current_diff
            closest_pair = (num1, num2)

    return closest_pair