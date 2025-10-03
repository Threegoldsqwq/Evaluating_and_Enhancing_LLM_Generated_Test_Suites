import math

def sum_product(numbers: list[int]) -> tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product
    of all the integers in a list.

    Empty sum should be equal to 0 and empty product should be equal to 1.

    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([5])
    (5, 5)
    >>> sum_product([-1, 2, -3])
    (-2, 6)
    >>> sum_product([0, 1, 2])
    (3, 0)
    """
    total_sum = 0
    total_product = 1

    # Iterate through each number in the list
    for num in numbers:
        total_sum += num        # Add the number to the running sum
        total_product *= num    # Multiply the number with the running product

    # Return the sum and product as a tuple
    return (total_sum, total_product)