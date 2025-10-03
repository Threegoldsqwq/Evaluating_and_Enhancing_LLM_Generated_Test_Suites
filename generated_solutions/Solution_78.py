def count_prime_hex_digits(hex_string: str) -> int:
    """
    Counts the number of hexadecimal digits in a string that are prime numbers.

    Args:
        hex_string: A string representing a hexadecimal number.
                    Assumed to be valid or empty, with A-F being uppercase.

    Returns:
        The total count of prime hexadecimal digits.
    """
    # Define a set of hexadecimal digits that represent prime numbers.
    # This provides efficient O(1) average time complexity for lookups.
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}

    count = 0
    for digit in hex_string:
        if digit in prime_hex_digits:
            count += 1
            
    return count