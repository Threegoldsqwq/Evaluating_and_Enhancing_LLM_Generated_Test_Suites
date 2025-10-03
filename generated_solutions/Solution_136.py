def largest_smallest_integers(numbers: list) -> tuple:
    """
    Returns a tuple (a, b), where 'a' is the largest of negative integers,
    and 'b' is the smallest of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    This function iterates through the list once, keeping track of the
    largest negative and smallest positive number encountered.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    largest_smallest_integers([-5, -2, -8, 10, 3, 1]) == (-2, 1)
    largest_smallest_integers([-1, -2, -3]) == (-1, None)
    largest_smallest_integers([10, 20, 30]) == (None, 10)
    """
    largest_negative = None
    smallest_positive = None

    for num in numbers:
        if num < 0:
            # If this is the first negative number encountered, or
            # if the current negative number is larger (closer to zero)
            # than the previously recorded largest_negative.
            if largest_negative is None or num > largest_negative:
                largest_negative = num
        elif num > 0:
            # If this is the first positive number encountered, or
            # if the current positive number is smaller (closer to zero)
            # than the previously recorded smallest_positive.
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num

    return (largest_negative, smallest_positive)