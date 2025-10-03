def below_threshold(l: list[int], t: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    >>> below_threshold([], 10) # An empty list should return True
    True
    >>> below_threshold([1, 2, 3], 3) # numbers must be strictly below the threshold
    False
    """
    for num in l:
        if num >= t:
            return False
    return True