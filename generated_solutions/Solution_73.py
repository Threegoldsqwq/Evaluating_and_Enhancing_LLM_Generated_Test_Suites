def smallest_change(arr: list[int]) -> int:
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. In one change, you can
    change one element to any other element.
    """
    n = len(arr)
    changes = 0

    # We only need to iterate up to the middle of the array.
    # For an array of length n, we compare arr[i] with arr[n - 1 - i].
    # The loop goes from i = 0 up to n // 2 - 1.
    # If n is odd, the middle element arr[n // 2] does not need a change
    # to satisfy the palindrome property, so it's naturally excluded.
    for i in range(n // 2):
        # If the element at the beginning and its symmetric counterpart
        # at the end are different, we need one change.
        if arr[i] != arr[n - 1 - i]:
            changes += 1
            
    return changes