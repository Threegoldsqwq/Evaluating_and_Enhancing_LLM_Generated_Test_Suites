def all_prefixes(s: str) -> list[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    >>> all_prefixes('hello')
    ['h', 'he', 'hel', 'hell', 'hello']
    >>> all_prefixes('')
    []
    >>> all_prefixes('a')
    ['a']
    """
    prefixes = []
    # Iterate from 1 up to the length of the string (inclusive)
    # i represents the length of the current prefix
    for i in range(1, len(s) + 1):
        # s[0:i] extracts the substring from the beginning up to index i (exclusive)
        # This gives a prefix of length i
        prefixes.append(s[0:i])
    return prefixes