from typing import List

def unique(input_list: List[int]) -> List[int]:
    """
    Returns a new list containing all unique elements from the input list,
    sorted in ascending order.

    Args:
        input_list: The list from which to extract unique sorted elements.

    Returns:
        A new list with unique elements, sorted.

    Examples:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
        >>> unique([])
        []
        >>> unique([1, 1, 1])
        [1]
        >>> unique([3, 1, 2])
        [1, 2, 3]
        >>> unique([-5, 0, 5, -5])
        [-5, 0, 5]
    """
    # Convert the list to a set to automatically handle uniqueness.
    # Sets do not maintain insertion order, but they are efficient for removing duplicates.
    unique_elements = set(input_list)

    # Convert the set back to a list and sort it.
    # The sorted() function returns a new sorted list.
    return sorted(unique_elements)