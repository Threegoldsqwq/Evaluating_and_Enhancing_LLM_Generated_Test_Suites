def is_happy(s: str) -> bool:
    """
    Checks if a string is happy.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

    Args:
        s: The input string.

    Returns:
        True if the string is happy, False otherwise.
    """
    # Condition 1: The string's length must be at least 3.
    if len(s) < 3:
        return False

    # Condition 2: Every 3 consecutive letters must be distinct.
    # We iterate through the string, considering each possible starting position 'i'
    # for a 3-letter sequence (s[i], s[i+1], s[i+2]).
    # The loop should go up to len(s) - 3, because s[i+2] would be the last character
    # of the triplet, meaning 'i' can be at most len(s) - 3.
    for i in range(len(s) - 2):
        char1 = s[i]
        char2 = s[i + 1]
        char3 = s[i + 2]

        # Check if any two characters in the current triplet are the same.
        # If they are, the triplet is not distinct, and thus the string is not happy.
        if char1 == char2 or char1 == char3 or char2 == char3:
            return False

    # If the loop completes without returning False, it means all 3-letter
    # consecutive sequences were distinct. Combined with the initial length check,
    # this means the string is happy.
    return True