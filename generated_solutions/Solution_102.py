def choose_num(x: int, y: int) -> int:
    """
    This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # If x is greater than y, the range is invalid, so no number can be chosen.
    if x > y:
        return -1

    # We want the biggest even number, so we start checking from y downwards.
    # If y is even, it's the biggest possible even number in the range.
    if y % 2 == 0:
        return y
    else:
        # If y is odd, the biggest possible even number must be y-1.
        # We need to ensure that y-1 is still within the range [x, y].
        # Since y-1 < y, we only need to check if y-1 is greater than or equal to x.
        if (y - 1) >= x:
            return y - 1
        else:
            # If y-1 is less than x, it means there are no even numbers
            # in the range [x, y] (because y is odd, and y-1 is too small).
            return -1