import math

def largest_prime_factor(n):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_factor = 1

    # Handle factor 2
    # If n is even, repeatedly divide by 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # Handle odd factors starting from 3
    # We only need to check up to sqrt(n) because if n has a prime factor
    # larger than sqrt(n), it can only have one such factor.
    # The remaining n after dividing out smaller factors will be this largest factor.
    i = 3
    while i * i <= n:
        # While i divides n, repeatedly divide n by i
        while n % i == 0:
            largest_factor = i
            n //= i
        i += 2  # Increment by 2 to check only odd numbers

    # If n is still greater than 1 after the loop, it means the remaining n
    # is a prime factor itself (and it must be the largest one).
    if n > 1:
        largest_factor = n

    return largest_factor