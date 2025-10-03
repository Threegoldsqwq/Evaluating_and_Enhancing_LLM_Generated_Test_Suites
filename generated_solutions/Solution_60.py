def sum_to_n(n):
    """
    Sums numbers from 1 to n using Gauss's formula.

    This function calculates the sum of all integers from 1 up to (and including) n.
    It uses the mathematical formula: sum = n * (n + 1) / 2, which is
    highly efficient (O(1) time complexity) as it involves a fixed number
    of arithmetic operations regardless of the size of n.

    Args:
        n (int): The upper limit of the sum. Must be a non-negative integer.

    Returns:
        int: The sum of numbers from 1 to n.

    Examples:
        >>> sum_to_n(30)
        465
        >>> sum_to_n(100)
        5050
        >>> sum_to_n(5)
        15
        >>> sum_to_n(10)
        55
        >>> sum_to_n(1)
        1
        >>> sum_to_n(0)
        0
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return n * (n + 1) // 2