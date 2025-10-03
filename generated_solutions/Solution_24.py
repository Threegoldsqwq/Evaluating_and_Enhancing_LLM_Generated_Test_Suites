def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n: The integer number for which to find the largest divisor.
           Assumes n > 1 based on common problem interpretations and the example.

    Returns:
        The largest divisor of n that is strictly smaller than n.

    Raises:
        ValueError: If n is less than or equal to 1, as there are no
                    divisors strictly smaller than n in those cases.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(10)
        5
        >>> largest_divisor(7) # For prime numbers, the largest divisor smaller than n is 1
        1
        >>> largest_divisor(1)
        Traceback (most recent call last):
        ...
        ValueError: Input n must be greater than 1.
    """
    if n <= 1:
        raise ValueError("Input n must be greater than 1.")

    # Iterate downwards from n-1 to 1
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

    # This part should ideally not be reached if n > 1,
    # as 1 is always a divisor for any integer.
    # However, it's good practice to consider all code paths.
    # For n > 1, the loop will always find '1' at least.
    return 1 # Fallback, though the loop for n > 1 always finds 1.