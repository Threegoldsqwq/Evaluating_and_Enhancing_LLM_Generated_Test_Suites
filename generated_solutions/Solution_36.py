def fizz_buzz(n):
    """
    Returns the number of times the digit 7 appears in integers less than n
    which are divisible by 11 or 13.

    This function's name is somewhat misleading given its specific requirements,
    but adheres to the name provided in the problem description.

    Args:
        n (int): The upper bound (exclusive) for checking integers.

    Returns:
        int: The total count of the digit 7.

    Examples:
        >>> fizz_buzz(50)
        0
        >>> fizz_buzz(78)
        2
        >>> fizz_buzz(79)
        3
        >>> fizz_buzz(1)
        0
        >>> fizz_buzz(0)
        0
        >>> fizz_buzz(14) # Numbers: 11, 13. No '7's.
        0
        >>> fizz_buzz(77) # Numbers: 11, 13, 22, 26, 33, 39, 44, 52, 55, 65, 66. No '7's.
        0
        >>> fizz_buzz(78) # Number 77 (divisible by 11) contains two '7's.
        2
        >>> fizz_buzz(79) # Number 77 (two '7's) + Number 78 (divisible by 13) (one '7'). Total 3.
        3
    """
    total_sevens_count = 0

    # Iterate through numbers from 1 up to n-1
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily count digit occurrences
            s_i = str(i)
            # Count how many times the digit '7' appears in the string
            total_sevens_count += s_i.count('7')

    return total_sevens_count