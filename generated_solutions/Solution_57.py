def monotonic(arr):
    """
    Return True if list elements are monotonically increasing or decreasing.

    An empty list or a list with one element is considered monotonic.

    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    >>> monotonic([])
    True
    >>> monotonic([5])
    True
    >>> monotonic([1, 1, 2, 3])
    True
    >>> monotonic([3, 2, 2, 1])
    True
    >>> monotonic([1, 5, 2])
    False
    """
    # A list is monotonically increasing if every element is greater than or
    # equal to the previous one.
    # The range(1, len(arr)) ensures we compare arr[i] with arr[i-1].
    # For empty or single-element lists, the generator expression is empty,
    # and all([]) returns True, correctly handling these base cases.
    is_increasing = all(arr[i] >= arr[i-1] for i in range(1, len(arr)))

    # A list is monotonically decreasing if every element is less than or
    # equal to the previous one.
    is_decreasing = all(arr[i] <= arr[i-1] for i in range(1, len(arr)))

    # If the list is either increasing or decreasing, it is monotonic.
    return is_increasing or is_decreasing