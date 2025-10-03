def count_distinct_characters(s: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    The function iterates through the input string, converts each character to lowercase
    (to handle case-insensitivity), and adds it to a set. A set naturally stores only
    unique elements. Finally, the size of the set is returned, which represents the
    count of distinct characters.

    Args:
        s: The input string.

    Returns:
        The number of distinct characters in the string, ignoring case.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
        >>> count_distinct_characters('apple')
        3
        >>> count_distinct_characters('')
        0
        >>> count_distinct_characters('AaBbCc')
        3
        >>> count_distinct_characters('Mississippi')
        4
    """
    distinct_chars = set()
    for char in s:
        # Convert character to lowercase before adding to the set
        # This ensures 'a' and 'A' are treated as the same character
        distinct_chars.add(char.lower())
    
    return len(distinct_chars)