import math

def is_prime(num: int) -> bool:
    """
    Checks if a given non-negative integer is a prime number.

    Args:
        num: An integer to check for primality.

    Returns:
        True if num is prime, False otherwise.
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:  # All other even numbers are not prime
        return False
    
    # Check for odd divisors from 3 up to the square root of num.
    # We only need to check up to int(sqrt(num)) + 1 because if num has a divisor
    # d > sqrt(num), then it must also have a divisor num/d < sqrt(num).
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
            
    return True

def count_up_to(n: int) -> list[int]:
    """
    Returns an array of prime numbers that are strictly less than n.

    Args:
        n: A non-negative integer.

    Returns:
        A list of prime numbers less than n.
    """
    # Handle edge cases where no primes exist less than n
    if n <= 2:
        return []

    primes = []
    # Iterate from 2 up to n-1 (as primes must be less than n)
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
            
    return primes

# Example Usage:
print(f"count_up_to(5) => {count_up_to(5)}")
print(f"count_up_to(11) => {count_up_to(11)}")
print(f"count_up_to(0) => {count_up_to(0)}")
print(f"count_up_to(20) => {count_up_to(20)}")
print(f"count_up_to(1) => {count_up_to(1)}")
print(f"count_up_to(18) => {count_up_to(18)}")
print(f"count_up_to(2) => {count_up_to(2)}") # Test with n=2 explicitly
print(f"count_up_to(3) => {count_up_to(3)}") # Test with n=3 explicitly