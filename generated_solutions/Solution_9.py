def rolling_max(numbers: list[int]) -> list[int]:
    """
    Generates a list of rolling maximum elements from a given sequence of integers.

    For each position in the input list, the corresponding element in the output list
    is the maximum value found in the input list up to that position.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers representing the rolling maximums.
        Returns an empty list if the input list is empty.

    Examples:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
        >>> rolling_max([])
        []
        >>> rolling_max([5])
        [5]
        >>> rolling_max([10, 5, 12, 8, 15])
        [10, 10, 12, 12, 15]
        >>> rolling_max([-5, -2, -8, -1])
        [-5, -2, -2, -1]
    """
    if not numbers:
        return []

    rolling_max_list = []
    # Initialize current_max with a value guaranteed to be smaller than any
    # possible integer in the list, so the first actual number becomes the max.
    # float('-inf') works well for this as it's less than any int.
    current_max = float('-inf') 

    for num in numbers:
        # Update current_max: it's the maximum of its previous value and the current number
        current_max = max(current_max, num)
        # Append the current_max to our result list
        rolling_max_list.append(current_max)

    return rolling_max_list