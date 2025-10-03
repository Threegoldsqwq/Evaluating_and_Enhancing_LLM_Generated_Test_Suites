import math

def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
        an integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number.

    For example:
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(1.0)
    0.0
    >>> truncate_number(0.123)
    0.123
    >>> truncate_number(99.999)
    0.999
    """
    # For a positive number, the integer part (largest integer smaller than or equal to the number)
    # can be obtained by simply casting to an integer. This operation truncates
    # the decimal part towards zero.
    # For example: int(3.5) == 3, int(0.123) == 0, int(1.0) == 1.
    integer_part = int(number)

    # The decimal part is the original number minus its integer part.
    decimal_part = number - integer_part

    return decimal_part