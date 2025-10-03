import math

def is_prime(n):
    """
    Checks if a number n is prime.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if n <= 1:
        return False  # 0, 1, and negative numbers are not prime
    if n == 2:
        return True   # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Other even numbers are not prime

    # Check for odd divisors from 3 up to sqrt(n)
    # We only need to check up to the square root of n because if n has a divisor
    # larger than its square root, it must also have a divisor smaller than its square root.
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  # Increment by 2 to check only odd numbers
    return True


def intersection(interval1, interval2):
    """
    Determines whether the length of the intersection of two intervals is a prime number.

    Args:
        interval1: A tuple (start, end) representing the first closed interval.
        interval2: A tuple (start, end) representing the second closed interval.
        
    Returns:
        "YES" if the length of the intersection is a prime number, "NO" otherwise.
    """
    s1, e1 = interval1
    s2, e2 = interval2

    # Calculate the start and end of the intersection interval
    intersect_start = max(s1, s2)
    intersect_end = min(e1, e2)

    # Check if there is an actual intersection.
    # If intersect_start > intersect_end, the intervals do not overlap.
    if intersect_start > intersect_end:
        return "NO"

    # Calculate the length of the intersection
    length = intersect_end - intersect_start

    # Check if the calculated length is a prime number
    if is_prime(length):
        return "YES"
    else:
        return "NO"