def is_simple_power(x: int, n: int) -> bool:
    """
    Checks if a number x is a simple power of n.
    x is a simple power of n if n**k = x for some non-negative integer k.

    Args:
        x (int): The number to check.
        n (int): The base.

    Returns:
        bool: True if x is a simple power of n, False otherwise.
    """

    # According to the examples, x and n are positive integers.
    # We are looking for a non-negative integer exponent k (k >= 0).

    # Case 1: x is 1
    # Any positive integer n raised to the power of 0 is 1 (n**0 = 1).
    # This covers examples like is_simple_power(1, 4) => True
    if x == 1:
        return True

    # After this point, x must be greater than 1 for it to be a simple power
    # (since 0**k = 0 or 1, negative**k = +/- 1 or other, but examples show positive)

    # Case 2: n is 1 (and x is not 1, handled above)
    # If n is 1, then 1 raised to any non-negative power is always 1.
    # Since x is not 1, it cannot be a power of 1.
    # This covers examples like is_simple_power(3, 1) => False
    if n == 1:
        return False

    # Case 3: x < n (and x > 1, n > 1 from previous checks)
    # If x is smaller than n, and both are greater than 1,
    # then n**k for k >= 1 will always be greater than x.
    # (n**0 = 1, already handled). So, x cannot be a power of n.
    # Example: is_simple_power(2, 3) would return False here.
    if x < n:
        return False

    # Case 4: x > 1 and n > 1
    # Repeatedly divide x by n. If it's a perfect power, x will eventually become 1.
    # At each step, x must be perfectly divisible by n.
    current_x = x
    while current_x > 1:
        # If current_x is not divisible by n, then x is not a power of n.
        if current_x % n != 0:
            return False
        # Divide current_x by n using integer division.
        current_x //= n

    # If the loop completes, it means current_x was successfully reduced to 1,
    # indicating that x was a simple power of n.
    return True