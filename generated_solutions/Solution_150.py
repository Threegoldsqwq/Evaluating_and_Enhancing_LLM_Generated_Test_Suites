def x_or_y(n, x, y):
    """
    Returns the value of x if n is a prime number,
    and returns the value of y otherwise.

    Args:
        n (int): The number to check for primality.
        x (any): The value to return if n is prime.
        y (any): The value to return if n is not prime.

    Returns:
        any: x if n is prime, y otherwise.
    """
    if is_prime(n):
        return x
    else:
        return y

### Complete Program

def is_prime(num):
    """
    Checks if a given number is a prime number.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if num is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # Check for odd divisors from 3 up to the square root of num
    # We only need to check up to int(num**0.5) + 1
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2  # Increment by 2 to check only odd numbers
    return True

def x_or_y(n, x, y):
    """
    Returns the value of x if n is a prime number,
    and returns the value of y otherwise.

    Args:
        n (int): The number to check for primality.
        x (any): The value to return if n is prime.
        y (any): The value to return if n is not prime.

    Returns:
        any: x if n is prime, y otherwise.
    """
    if is_prime(n):
        return x
    else:
        return y

# --- Examples ---
# print(f"x_or_y(7, 34, 12) == {x_or_y(7, 34, 12)}") # Expected: 34 (7 is prime)
# print(f"x_or_y(15, 8, 5) == {x_or_y(15, 8, 5)}") # Expected: 5 (15 is not prime)
# print(f"x_or_y(2, 100, 200) == {x_or_y(2, 100, 200)}") # Expected: 100 (2 is prime)
# print(f"x_or_y(4, 'apple', 'banana') == {x_or_y(4, 'apple', 'banana')}") # Expected: banana (4 is not prime)
# print(f"x_or_y(1, 'prime', 'not prime') == {x_or_y(1, 'prime', 'not prime')}") # Expected: not prime (1 is not prime)
# print(f"x_or_y(11, 'found', 'missed') == {x_or_y(11, 'found', 'missed')}") # Expected: found (11 is prime)