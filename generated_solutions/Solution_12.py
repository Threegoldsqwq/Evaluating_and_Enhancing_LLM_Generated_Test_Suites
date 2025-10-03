def longest(strings: list[str]) -> str | None:
    """
    Out of list of strings, return the longest one.
    Return the first one in case of multiple strings of the same length.
    Return None in case the input list is empty.

    >>> longest([]) is None
    True
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['apple', 'banana', 'grape'])
    'banana'
    >>> longest(['hello', 'world', 'a', 'test'])
    'hello'
    """
    if not strings:
        return None
    
    # The built-in max() function can take a 'key' argument.
    # When key=len, it finds the item for which len(item) is maximized.
    # In case of ties (multiple items with the same maximum length),
    # max() returns the first item encountered in the iterable,
    # which satisfies the problem's tie-breaking rule.
    return max(strings, key=len)