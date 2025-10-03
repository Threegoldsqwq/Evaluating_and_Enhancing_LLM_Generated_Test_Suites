def move_one_ball(arr: list[int]) -> bool:
    """
    Determines if an array can be sorted in non-decreasing order by performing
    right shift operations.

    Args:
        arr: A list of N integers with unique elements.

    Returns:
        True if the array can be sorted by right shifts, False otherwise.
        Returns True if the array is empty.
    """
    n = len(arr)

    # An empty array is considered sorted.
    # An array with one element is always sorted.
    if n <= 1:
        return True

    # Count the number of "breaks" where arr[i] > arr[i+1].
    # For a cyclically sorted array (a rotated sorted array), there should be
    # at most one such point of decrease when traversing linearly from left to right.
    # E.g., for [3, 4, 5, 1, 2], the break is 5 > 1.
    # For [1, 2, 3, 4, 5], there are no breaks.
    # For [3, 5, 4, 1, 2], there are two breaks: 5 > 4 and 4 > 1.
    
    count_decreases = 0
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            count_decreases += 1

    # Case 1: No decreases found. The array is already sorted.
    if count_decreases == 0:
        return True
    
    # Case 2: Exactly one decrease found.
    # This is characteristic of a rotated sorted array.
    # To confirm it's a valid rotation, the last element must be less than
    # or equal to the first element (i.e., the "tail" of the rotated part
    # should be smaller than the "head" of the remaining part to complete the cycle).
    # Since elements are unique, it must be strictly less than.
    elif count_decreases == 1:
        if arr[n-1] <= arr[0]:
            return True
        else:
            return False
            # Example that fails this check: [2, 1, 3]
            #   Break at 2 > 1. count_decreases = 1.
            #   arr[2]=3, arr[0]=2. 3 <= 2 is False. Correctly returns False.
            #   (Because [2, 1, 3] cannot be sorted by right shifts:
            #    [2, 1, 3] -> [3, 2, 1] -> [1, 3, 2] -> [2, 1, 3])
            
    # Case 3: More than one decrease found.
    # This means the array is not a simple cyclic shift of a sorted array.
    else: # count_decreases > 1
        return False