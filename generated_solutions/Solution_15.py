def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args:
        n: The upper bound for the sequence of numbers (inclusive).

    Returns:
        A string with numbers from 0 to n, separated by spaces.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
        >>> string_sequence(1)
        '0 1'
    """
    # Generate a sequence of numbers from 0 to n (inclusive)
    # range(n + 1) will produce numbers 0, 1, ..., n
    numbers = range(n + 1)

    # Convert each number in the sequence to its string representation
    string_numbers = [str(num) for num in numbers]

    # Join the list of string numbers with a space character as the delimiter
    return " ".join(string_numbers)