def can_arrange(arr: list[int]) -> int:
    """
    Returns the largest index of an element which is not greater than or equal
    to the element immediately preceding it. If no such element exists, returns -1.

    Args:
        arr: A list of integers, guaranteed not to contain duplicate values.

    Returns:
        The largest index i such that arr[i] < arr[i-1], or -1 if no such index exists.
    """
    # We need to compare arr[i] with arr[i-1], so the smallest possible index for 'i' is 1.
    # To find the LARGEST such index, we iterate backwards from the end of the array.
    # The loop should start from the last possible index to check (len(arr) - 1)
    # down to the first possible index to check (1).
    # The 'stop' value in range is exclusive, so it should be 0 to include index 1.
    for i in range(len(arr) - 1, 0, -1):
        # The condition "not greater than or equal to" is equivalent to "strictly less than".
        if arr[i] < arr[i-1]:
            return i  # Found the largest such index, return immediately.
            
    # If the loop completes, it means no such element was found.
    return -1