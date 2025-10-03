def same_chars(word1: str, word2: str) -> bool:
    """
    Check if two words have the same characters.
    The order and frequency of characters do not matter, only the set of unique characters.

    Args:
        word1: The first word (string).
        word2: The second word (string).

    Returns:
        True if both words contain the exact same set of unique characters,
        False otherwise.

    Examples:
        >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
        True
        >>> same_chars('abcd', 'dddddddabc')
        True
        >>> same_chars('dddddddabc', 'abcd')
        True
        >>> same_chars('eabcd', 'dddddddabc')
        False
        >>> same_chars('abcd', 'dddddddabce')
        False
        >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
        False
        >>> same_chars('', '')
        True
        >>> same_chars('a', '')
        False
        >>> same_chars('a', 'A') # Case sensitive
        False
    """
    # Convert each word into a set of its unique characters.
    # Python's set() constructor directly creates a set of characters from a string.
    set1 = set(word1)
    set2 = set(word2)

    # Compare the two sets for equality.
    # Two sets are equal if and only if they contain the exact same elements.
    return set1 == set2