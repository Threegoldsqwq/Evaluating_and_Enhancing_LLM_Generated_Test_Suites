def decimal_to_binary(decimal_num: int) -> str:
    """
    Converts a decimal number to its binary representation,
    formatted with 'db' prefix and suffix.

    Args:
        decimal_num: An integer in decimal form.

    Returns:
        A string representing the binary form,
        prefixed and suffixed with 'db'.
    """
    # Convert the decimal number to its binary string representation.
    # The built-in bin() function returns a string prefixed with "0b".
    # For example, bin(15) returns "0b1111".
    binary_representation = bin(decimal_num)

    # Remove the "0b" prefix from the binary string.
    # We slice the string starting from the third character (index 2).
    pure_binary_string = binary_representation[2:]

    # Add the 'db' prefix and 'db' suffix as required by the format.
    formatted_output = "db" + pure_binary_string + "db"

    return formatted_output