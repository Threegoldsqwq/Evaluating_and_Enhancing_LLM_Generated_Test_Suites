def encode_cyclic(s: str) -> str:
    """
    Encodes a string by cycling groups of three characters.
    Each group of characters is rotated left by one position.

    For a group 'abc', it becomes 'bca'.
    For a group 'ab', it becomes 'ba'.
    For a group 'a', it remains 'a'.

    Args:
        s: The input string to encode.

    Returns:
        The cyclically encoded string.
    """
    encoded_chars = []
    n = len(s)
    # Iterate through the string in chunks of 3 characters
    for i in range(0, n, 3):
        chunk = s[i:i+3]
        if chunk: # Only process if the chunk is not empty (e.g., for an empty input string)
            # Perform a left rotation by one position
            # Example: "abc" -> "bca", "ab" -> "ba", "a" -> "a"
            rotated_chunk = chunk[1:] + chunk[0]
            encoded_chars.append(rotated_chunk)
            
    return "".join(encoded_chars)


def decode_cyclic(encoded_s: str) -> str:
    """
    Takes as input a string encoded with the encode_cyclic function and returns the decoded string.
    The decoding reverses the cyclic shift performed during encoding.
    This means each group of characters is rotated right by one position.

    For an encoded group 'bca', it becomes 'abc'.
    For an encoded group 'ba', it becomes 'ab'.
    For an encoded group 'a', it remains 'a'.

    Args:
        encoded_s: The cyclically encoded string.

    Returns:
        The decoded string.
    """
    decoded_chars = []
    n = len(encoded_s)
    # Iterate through the encoded string in chunks of 3 characters
    for i in range(0, n, 3):
        chunk = encoded_s[i:i+3]
        if chunk: # Only process if the chunk is not empty
            # Perform a right rotation by one position
            # Example: "bca" -> "abc", "ba" -> "ab", "a" -> "a"
            rotated_chunk = chunk[-1] + chunk[:-1]
            decoded_chars.append(rotated_chunk)
            
    return "".join(decoded_chars)