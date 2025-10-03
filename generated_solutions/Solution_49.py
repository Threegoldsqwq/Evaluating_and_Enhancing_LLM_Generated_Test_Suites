def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function calculates 2 raised to the power of n, then takes the
    result modulo p. It uses modular exponentiation to handle potentially
    very large values of n efficiently and avoid overflow issues that
    would arise from calculating 2**n directly for large n.

    Args:
        n: The exponent (non-negative integer).
        p: The modulus (positive integer).

    Returns:
        The result of (2^n) % p.

    Examples:
        >>> modp(3, 5)
        3
        >>> modp(1101, 101)
        2
        >>> modp(0, 101)
        1
        >>> modp(3, 11)
        8
        >>> modp(100, 101)
        1
    """
    # Python's built-in pow() function with three arguments performs
    # modular exponentiation efficiently and correctly handles large
    # exponents (n) and the modulo operation at each step, preventing
    # intermediate results from becoming too large.
    # It computes (base ** exp) % mod.
    return pow(2, n, p)