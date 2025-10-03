def multiply(num1: int, num2: int) -> int:
    """
    Takes two integers and returns the product of their unit digits.

    The unit digit of an integer n is n % 10.
    For negative numbers, Python's % operator returns a result with the same
    sign as the divisor (which is positive 10 here), effectively giving
    the "mathematical" unit digit if considered from 0-9.
    For example, -15 % 10 evaluates to 5.

    Args:
        num1: The first integer.
        num2: The second integer.

    Returns:
        The product of the unit digits of num1 and num2.

    Examples:
        multiply(148, 412) == 16  (8 * 2)
        multiply(19, 28) == 72    (9 * 8)
        multiply(2020, 1851) == 0 (0 * 1)
        multiply(14, -15) == 20   (4 * 5, as -15 % 10 is 5)
    """
    # Get the unit digit of the first number
    unit_digit_1 = num1 % 10

    # Get the unit digit of the second number
    unit_digit_2 = num2 % 10

    # Return the product of their unit digits
    return unit_digit_1 * unit_digit_2