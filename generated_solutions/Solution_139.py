import math

def brazilian_factorial(n: int) -> int:
    """
    Calculates the Brazilian factorial of a given integer n.

    The Brazilian factorial is defined as:
        brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
        where n > 0

    For example:
    >>> brazilian_factorial(4)
    288
    >>> brazilian_factorial(1)
    1
    >>> brazilian_factorial(2)
    2
    >>> brazilian_factorial(3)
    12
    """
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")
    if n <= 0:
        raise ValueError("Input 'n' must be a positive integer (n > 0).")

    total_product = 1
    # Iterate from 1 up to n (inclusive)
    for i in range(1, n + 1):
        # Calculate the standard factorial of the current number i
        current_factorial = math.factorial(i)
        # Multiply this factorial into our running total product
        total_product *= current_factorial
        
    return total_product