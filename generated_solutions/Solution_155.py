def even_odd_count(number: int) -> tuple[int, int]:
    """
    Given an integer, return a tuple that has the number of even and odd digits respectively.

    Args:
        number: The input integer.

    Returns:
        A tuple (even_digit_count, odd_digit_count).
    """
    even_count = 0
    odd_count = 0

    # Convert the absolute value of the number to a string to easily iterate through its digits.
    # Taking the absolute value ensures that a negative sign doesn't interfere with digit processing.
    num_str = str(abs(number))

    for digit_char in num_str:
        digit = int(digit_char)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)