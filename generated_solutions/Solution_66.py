def digitSum(s: str) -> int:
    """
    Calculates the sum of ASCII codes of uppercase characters only in a given string.

    Args:
        s: The input string.

    Returns:
        The sum of ASCII codes of uppercase characters.
    """
    total_sum = 0
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Add its ASCII value to the total sum
            total_sum += ord(char)
    return total_sum