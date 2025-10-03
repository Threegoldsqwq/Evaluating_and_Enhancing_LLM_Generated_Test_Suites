def filter_by_substring(strings: list[str], substring: str) -> list[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    >>> filter_by_substring(['apple', 'banana', 'cherry'], 'ap')
    ['apple']
    >>> filter_by_substring(['hello', 'world'], 'xyz')
    []
    >>> filter_by_substring(['foo', 'bar', 'baz'], '') # Empty substring matches all
    ['foo', 'bar', 'baz']
    """
    return [s for s in strings if substring in s]