import math

# Pre-compute primes up to a certain limit (e.g., 99).
# Since 'a' is less than 100, the maximum number we need to factorize is 99.
# The largest possible prime factor for a number < 100 is 97.
# This list will be computed once when the module is loaded.
def _get_primes_up_to(limit: int) -> list[int]:
    """Generates a list of prime numbers up to a given limit using a sieve."""
    if limit < 2:
        return []
        
    is_prime_sieve = [True] * (limit + 1)
    is_prime_sieve[0] = is_prime_sieve[1] = False
    
    primes = []
    for p in range(2, limit + 1):
        if is_prime_sieve[p]:
            primes.append(p)
            # Mark multiples of p as not prime. Start from p*p for optimization.
            for multiple in range(p * p, limit + 1, p):
                is_prime_sieve[multiple] = False
    return primes

# Global list of primes, computed once for efficiency.
# We need primes up to 99 to factorize any number 'a' less than 100.
_ALL_PRIMES_UP_TO_99 = _get_primes_up_to(99)


def is_multiply_prime(a: int) -> bool:
    """
    Returns true if the given number is the multiplication of 3 prime numbers
    (interpreted as 3 distinct prime numbers) and false otherwise.
    Knowing that (a) is less then 100.

    Args:
        a (int): The number to check. Must be a positive integer less than 100.

    Returns:
        bool: True if 'a' is the product of 3 distinct prime numbers, False otherwise.
    """
    # Input validation based on problem statement "a is less then 100"
    if not isinstance(a, int) or a <= 0 or a >= 100:
        # For this problem, we'll return False for invalid inputs that
        # fall outside the specified range and type.
        return False

    # Smallest product of 3 distinct primes is 2 * 3 * 5 = 30.
    # Any number smaller than 30 cannot satisfy the condition.
    if a < 30:
        return False

    factors = []
    temp_a = a  # Use a temporary variable for factorization

    # Iterate through the pre-computed primes to find factors
    for p in _ALL_PRIMES_UP_TO_99:
        # Optimization: If p*p is greater than the remaining temp_a,
        # it means temp_a must either be 1 (fully factored) or a prime itself.
        if p * p > temp_a:
            break
        
        while temp_a % p == 0:
            factors.append(p)
            temp_a //= p
        
        # If temp_a becomes 1, all factors have been found
        if temp_a == 1:
            break

    # If temp_a is still greater than 1 after the loop, it means
    # the remaining temp_a is a prime factor itself (and it's larger than
    # any 'p' whose square was checked).
    # Since _ALL_PRIMES_UP_TO_99 covers all primes up to 97, and our max 'a' is 99,
    # any remaining temp_a must indeed be a prime number (e.g. for a=78, after 2,3 it is 13).
    if temp_a > 1:
        factors.append(temp_a)

    # Check the conditions based on the "distinct primes" interpretation:
    # 1. The total count of prime factors (including multiplicity) must be exactly 3.
    # 2. All these 3 prime factors must be distinct.
    return len(factors) == 3 and len(set(factors)) == 3