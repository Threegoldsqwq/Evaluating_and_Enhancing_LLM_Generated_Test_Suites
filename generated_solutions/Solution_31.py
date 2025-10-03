import math

def is_prime(n: int) -> bool:
    """
    Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # All other even numbers are not prime
    if n % 2 == 0:
        return False

    # At this point, n is an odd number greater than 2.
    # We only need to check for odd divisors from 3 up to sqrt(n).
    # We can use math.isqrt for integer square root (Python 3.8+)
    # or int(math.sqrt(n)) for broader compatibility.
    limit = int(math.sqrt(n))

    # Check for odd divisors
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False  # Found a divisor, so n is not prime

    # If no divisors were found, n is prime
    return True