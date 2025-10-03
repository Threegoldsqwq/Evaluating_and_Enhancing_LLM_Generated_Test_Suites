def concatenate(strings):
    """
    Concatenates a list of strings into a single string.

    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['hello', ' ', 'world'])
    'hello world'
    """
    return "".join(strings)