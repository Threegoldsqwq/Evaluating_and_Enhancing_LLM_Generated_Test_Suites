def how_many_times(original_string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string,
    counting overlapping cases.

    Args:
        original_string: The string to search within.
        substring: The substring to search for.

    Returns:
        The number of times the substring appears, including overlaps.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
        >>> how_many_times('banana', 'ana')
        2
        >>> how_many_times('ababab', 'aba')
        2
        >>> how_many_times('abc', 'd')
        0
        >>> how_many_times('test', '') # Empty substring case
        0
        >>> how_many_times('', '') # Empty original and empty substring case
        0
    """
    count = 0

    # Handle the edge case where the substring is empty.
    # An empty substring is generally not considered "found" in this context.
    if not substring:
        return 0

    # Iterate through the original string, checking for the substring
    # at each possible starting position.
    # The loop should run from index 0 up to `len(original_string) - len(substring)`.
    # Adding 1 to the upper bound makes the range inclusive of this last valid index.
    for i in range(len(original_string) - len(substring) + 1):
        # Slice the original string from the current index `i`
        # for the length of the substring.
        if original_string[i : i + len(substring)] == substring:
            count += 1

    return count