def any_int(x, y, z):
    """
    Checks if one of the three numbers is equal to the sum of the other two,
    and all numbers are integers.

    Args:
        x (number): The first number.
        y (number): The second number.
        z (number): The third number.

    Returns:
        bool: True if all conditions are met, False otherwise.
    """
    
    # Condition 1: Check if all numbers are integers
    # We use isinstance(n, int) to strictly check for the 'int' type,
    # distinguishing it from floats like 2.0.
    all_are_integers = isinstance(x, int) and isinstance(y, int) and isinstance(z, int)

    # If not all numbers are integers, we immediately return False as per the problem.
    if not all_are_integers:
        return False

    # Condition 2: Check if one number is equal to the sum of the other two
    # This needs to be true for any of the three possible combinations.
    one_is_sum_of_others = (x == y + z) or \
                           (y == x + z) or \
                           (z == x + y)

    # If both conditions are met, return True. Otherwise, return False (which is implicitly handled
    # if all_are_integers was True but one_is_sum_of_others was False).
    return one_is_sum_of_others