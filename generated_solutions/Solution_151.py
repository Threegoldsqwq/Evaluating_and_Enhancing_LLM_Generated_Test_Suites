def double_the_difference(numbers: list) -> int:
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.

    For example:
    double_the_difference([1, 3, 2, 0]) == 10  (1*1 + 3*3)
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81 (9*9)
    double_the_difference([0]) == 0
    double_the_difference([]) == 0
    """
    total_sum_of_squares = 0

    for num in numbers:
        # 1. Check if the number is an integer
        # This handles cases like floats (e.g., 3.5), strings, etc., which are ignored.
        # Note: In Python, `True` and `False` are instances of `int`.
        # True is 1, False is 0. If True (1) is in the list, it's an odd positive integer.
        # If False (0) is in the list, it's an even non-negative integer.
        if isinstance(num, int):
            # 2. Check if the integer is non-negative (not negative)
            if num >= 0:
                # 3. Check if the non-negative integer is odd
                if num % 2 != 0:
                    # If all conditions are met, square the number and add to the total
                    total_sum_of_squares += num * num
    
    return total_sum_of_squares