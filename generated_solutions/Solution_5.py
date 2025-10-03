def intersperse(numbers, delimiter):
    """
    Insert a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
        numbers (list): The input list of numbers.
        delimiter: The value to insert between elements.

    Returns:
        list: A new list with the delimiter interspersed.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
        >>> intersperse([10], 0)
        [10]
        >>> intersperse(['a', 'b', 'c'], '-')
        ['a', '-', 'b', '-', 'c']
    """
    result = []
    # Iterate through the input list with index
    for i, num in enumerate(numbers):
        result.append(num)
        # If it's not the last element, append the delimiter
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result