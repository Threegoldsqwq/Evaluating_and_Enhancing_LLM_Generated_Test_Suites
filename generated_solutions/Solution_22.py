def filter_integers(values_list: list) -> list:
    """
    Filter given list of any python values only for integers.

    Args:
        values_list: A list containing various Python values.

    Returns:
        A new list containing only the integer values from the input list.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
        >>> filter_integers([])
        []
        >>> filter_integers(['hello', 1.0, True, None])
        []
        >>> filter_integers([10, -5, 0, 1/2]) # 1/2 is float, not int
        [10, -5, 0]
    """
    return [item for item in values_list if isinstance(item, int)]