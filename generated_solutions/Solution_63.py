def fibfib(n: int) -> int:
    """
    Computes the n-th element of the FibFib number sequence efficiently.

    The sequence is defined as:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n > 2.

    This implementation uses dynamic programming with O(1) space complexity
    by only storing the last three computed values.

    Args:
        n: The index of the FibFib number to compute (non-negative integer).

    Returns:
        The n-th FibFib number.

    Examples:
        >>> fibfib(0)
        0
        >>> fibfib(1)
        0
        >>> fibfib(2)
        1
        >>> fibfib(3)
        1
        >>> fibfib(4)
        2
        >>> fibfib(5)
        4
        >>> fibfib(8)
        24
    """
    # Handle base cases as defined
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1

    # Initialize variables to represent fibfib(i-3), fibfib(i-2), fibfib(i-1)
    # These correspond to fibfib(0), fibfib(1), fibfib(2) at the start of the loop for i=3
    a = 0  # Represents fibfib(i-3) initially fibfib(0)
    b = 0  # Represents fibfib(i-2) initially fibfib(1)
    c = 1  # Represents fibfib(i-1) initially fibfib(2)

    # Iterate from i = 3 up to n to compute subsequent FibFib numbers
    for _ in range(3, n + 1):
        # Calculate the next FibFib number using the recurrence relation
        next_fib = a + b + c
        
        # Shift the values for the next iteration:
        # The previous fibfib(i-2) becomes the new fibfib(i-3)
        # The previous fibfib(i-1) becomes the new fibfib(i-2)
        # The newly computed next_fib becomes the new fibfib(i-1)
        a = b
        b = c
        c = next_fib

    # After the loop, 'c' holds the n-th FibFib number
    return c