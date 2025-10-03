import math

def is_prime(n: int) -> bool:
    """
    Checks if a given integer n is a prime number.
    """
    if n <= 1:
        return False
    if n <= 3:  # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # Multiples of 2 or 3 are not prime
        return False
    
    # Check for primes of the form 6k ± 1
    # All primes greater than 3 can be expressed in this form.
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_digits(n: int) -> int:
    """
    Calculates the sum of the digits of a given integer n.
    """
    # Convert to string and sum the integer value of each character
    return sum(int(digit) for digit in str(n))

def find_largest_prime_value_and_sum_its_digits(lst: list[int]) -> int:
    """
    Finds the largest prime value in a list of integers and returns the sum of its digits.

    Args:
        lst: A list of integers.

    Returns:
        The sum of the digits of the largest prime found in the list.
        Returns 0 if no prime numbers are found in the list (or if the list is empty).
    """
    largest_prime = -1  # Initialize with a value that any prime (>=2) will exceed

    for num in lst:
        if is_prime(num):
            if num > largest_prime:
                largest_prime = num
    
    # If largest_prime is still -1, it means no primes were found in the list.
    if largest_prime == -1:
        return 0  # Or raise an error, depending on problem specific handling for this case
    else:
        return sum_digits(largest_prime)