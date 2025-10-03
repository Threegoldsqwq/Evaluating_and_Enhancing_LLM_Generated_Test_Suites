def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b using the Euclidean algorithm.

    The Euclidean algorithm is based on the principle that the greatest common divisor of two
    numbers does not change if the larger number is replaced by its difference with the
    smaller number. This process is repeated until one of the numbers is zero, and the other
    number is then the GCD. A more efficient version uses the modulo operator.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The greatest common divisor of a and b.

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
        >>> greatest_common_divisor(10, 0)
        10
        >>> greatest_common_divisor(0, 10)
        10
        >>> greatest_common_divisor(0, 0)
        0
    """
    while b:  # Continue as long as b is not zero
        # In each step, the old 'b' becomes the new 'a', and
        # the remainder of 'a' divided by 'b' becomes the new 'b'.
        a, b = b, a % b
    return a