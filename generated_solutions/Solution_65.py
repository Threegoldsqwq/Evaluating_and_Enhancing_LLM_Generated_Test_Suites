def circular_shift(x: int, shift: int) -> str:
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    >>> circular_shift(123, 1) # Shift 1 right: 123 -> 312
    "312"
    >>> circular_shift(123, 3) # Shift 3 right: 123 -> 312 -> 231 -> 123
    "123"
    >>> circular_shift(123, 4) # Shift 4 right, which is > num_digits (3)
    "321"
    >>> circular_shift(5, 1) # Single digit, shift 1 right
    "5"
    >>> circular_shift(5, 2) # Single digit, shift 2 right (2 > 1)
    "5"
    >>> circular_shift(12345, 100) # Shift 100 right (100 > 5)
    "54321"
    >>> circular_shift(0, 1)
    "0"
    >>> circular_shift(0, 5)
    "0"
    """
    x_str = str(x)
    num_digits = len(x_str)

    # Special case: If shift is greater than the number of digits,
    # return the digits reversed.
    if shift > num_digits:
        return x_str[::-1]

    # Calculate the effective shift amount.
    # This handles shifts that are multiples of num_digits (e.g., shifting 3 times for a 3-digit number)
    # where the result should be the original string.
    effective_shift = shift % num_digits

    # If effective_shift is 0, it means a full rotation or no shift,
    # so the string remains unchanged.
    if effective_shift == 0:
        return x_str
    
    # Perform the circular right shift using string slicing:
    # 1. Take the last 'effective_shift' characters.
    # 2. Take the first 'num_digits - effective_shift' characters.
    # 3. Concatenate them with the last part first.
    shifted_part = x_str[-effective_shift:]
    remaining_part = x_str[:-effective_shift]
    
    return shifted_part + remaining_part