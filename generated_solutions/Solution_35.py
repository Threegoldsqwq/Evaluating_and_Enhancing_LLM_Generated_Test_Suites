def max_element(data):
    """
    Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    >>> max_element([])
    Traceback (most recent call last):
        ...
    ValueError: max_element() arg is an empty sequence
    >>> max_element([-1, -5, -2])
    -1
    """
    if not data:
        raise ValueError("max_element() arg is an empty sequence")

    # Initialize max_val with the first element of the list
    max_val = data[0]

    # Iterate through the rest of the elements (starting from the second)
    # and update max_val if a larger element is found
    for element in data[1:]:
        if element > max_val:
            max_val = element

    return max_val