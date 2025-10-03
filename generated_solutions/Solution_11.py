def string_xor(a: str, b: str) -> str:
    """
    Performs binary XOR on two input strings consisting only of '1's and '0's.

    Args:
        a: The first binary string.
        b: The second binary string.

    Returns:
        A string representing the result of the binary XOR operation.

    Raises:
        ValueError: If the input strings are not of equal length.
                    (Based on the problem description and example, equal length
                    is implicitly assumed, but it's good practice to handle.)

    Examples:
        >>> string_xor('010', '110')
        '100'
        >>> string_xor('10101', '01010')
        '11111'
        >>> string_xor('000', '000')
        '000'
        >>> string_xor('111', '111')
        '000'
    """
    if len(a) != len(b):
        raise ValueError("Input strings must be of equal length for XOR operation.")

    result_chars = []
    # Iterate through both strings simultaneously, character by character
    for char_a, char_b in zip(a, b):
        # Convert character '0' or '1' to integer 0 or 1
        int_a = int(char_a)
        int_b = int(char_b)

        # Perform the XOR operation
        xor_result = int_a ^ int_b

        # Convert the integer result (0 or 1) back to a character '0' or '1'
        result_chars.append(str(xor_result))

    # Join the list of result characters into a single string
    return "".join(result_chars)