def filter_by_prefix(strings: list[str], prefix: str) -> list[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings: A list of strings to filter.
        prefix: The prefix string to check against.

    Returns:
        A new list containing only the strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
        >>> filter_by_prefix(['apple', 'banana', 'apricot', 'orange'], 'ap')
        ['apple', 'apricot']
        >>> filter_by_prefix(['hello', 'world', 'hi'], 'w')
        ['world']
        >>> filter_by_prefix(['test', 'toast', 'tea'], 'z')
        []
    """
    result = []
    for s in strings:
        if s.startswith(prefix):
            result.append(s)
    return result