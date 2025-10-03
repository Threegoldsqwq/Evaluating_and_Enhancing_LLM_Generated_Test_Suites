def fib4(n: int) -> int:
    """
    Computes the n-th element of the Fib4 number sequence efficiently without recursion.

    The Fib4 sequence is defined as:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

    Args:
        n: The index of the Fib4 number to compute (non-negative integer).

    Returns:
        The n-th Fib4 number.

    Examples:
    >>> fib4(0)
    0
    >>> fib4(1)
    0
    >>> fib4(2)
    2
    >>> fib4(3)
    0
    >>> fib4(4)
    2
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    # Handle base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize the last four values for n >= 4
    # These correspond to fib4(0), fib4(1), fib4(2), fib4(3)
    # Let f0 = fib4(i-4), f1 = fib4(i-3), f2 = fib4(i-2), f3 = fib4(i-1)
    f0 = 0  # fib4(0)
    f1 = 0  # fib4(1)
    f2 = 2  # fib4(2)
    f3 = 0  # fib4(3)

    # Iterate from i = 4 up to n
    for _ in range(4, n + 1):
        # Calculate the current fib4(i)
        next_fib = f0 + f1 + f2 + f3
        
        # Shift the values for the next iteration
        f0 = f1
        f1 = f2
        f2 = f3
        f3 = next_fib
    
    # After the loop, f3 holds the value of fib4(n)
    return f3