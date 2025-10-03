def is_prime(num):
    """
    Checks if a number is prime.
    """
    if num < 2:
        return False
    # Check for factors from 2 up to the square root of num
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def prime_fib(n):
    """
    Returns the n-th number that is a Fibonacci number and is also prime.

    Args:
        n (int): The 1-indexed position of the desired prime Fibonacci number.

    Returns:
        int: The n-th prime Fibonacci number.

    Raises:
        ValueError: If n is not a positive integer.

    Examples:
        >>> prime_fib(1)
        2
        >>> prime_fib(2)
        3
        >>> prime_fib(3)
        5
        >>> prime_fib(4)
        13
        >>> prime_fib(5)
        89
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")

    count = 0
    # Initialize Fibonacci sequence: F(0)=0, F(1)=1
    a, b = 0, 1

    while True:
        # 'b' always holds the current Fibonacci number to check
        # We start checking from the Fibonacci sequence generated after F(0) and F(1).
        # F(0)=0 and F(1)=1 are not prime, so they won't pass is_prime().
        # The sequence generated is:
        # (a, b) -> current_fib
        # (0, 1) -> 1 (not prime)
        # (1, 1) -> 1 (not prime)
        # (1, 2) -> 2 (prime!)
        # (2, 3) -> 3 (prime!)
        # (3, 5) -> 5 (prime!)
        # (5, 8) -> 8 (not prime)
        # (8, 13) -> 13 (prime!)
        # etc.
        
        current_fib = b

        if is_prime(current_fib):
            count += 1
            if count == n:
                return current_fib
        
        # Generate the next Fibonacci number
        a, b = b, a + b