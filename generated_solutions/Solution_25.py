def factorize(n: int) -> list[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []

    # Handle edge cases for n <= 1
    # Prime factorization is typically defined for integers n > 1.
    # For n=1, the list of prime factors is empty.
    # For n=0 or negative numbers, it's not well-defined in this context,
    # so returning an empty list is a safe default.
    if n <= 1:
        return []

    # Handle factor 2
    # Divide by 2 until n is odd
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Handle odd factors
    # We only need to check for prime factors up to the square root of n.
    # Start from 3 and increment by 2 (to check only odd numbers).
    i = 3
    while i * i <= n:
        # If i is a factor, add it to the list and divide n by i
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # If n is still greater than 1 after the loop, it means the remaining n
    # itself is a prime factor (it's the largest one, and it's greater than
    # sqrt(original_n) or the remaining sqrt(n)).
    # This covers cases where the original n was a prime number
    # (e.g., factorize(7) -> n remains 7, then 7 is added)
    # or if the largest prime factor is greater than sqrt(n)
    # (e.g., factorize(14) -> after 2, n becomes 7, then 7 is added).
    if n > 1:
        factors.append(n)

    return factors