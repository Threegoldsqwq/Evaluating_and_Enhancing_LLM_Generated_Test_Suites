def encode(message: str) -> str:
    """
    Encodes a message by swapping the case of all letters and replacing vowels.

    The encoding process is as follows for each character:
    1. If the character is not a letter (e.g., space, punctuation), it is kept as is.
    2. If the character is a letter:
        a. The original case of the letter determines its final case:
           If original was lowercase, final will be uppercase.
           If original was uppercase, final will be lowercase.
        b. If the letter is a vowel (a, e, i, o, u, case-insensitive),
           it is replaced by the letter 2 places ahead in the alphabet,
           preserving its current case (e.g., 'a' -> 'c', 'A' -> 'C').
        c. The letter (potentially replaced) is then converted to its final
           case as determined in step 2a.

    Args:
        message: The input string message to be encoded.

    Returns:
        The encoded string.

    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    >>> encode('Hello World')
    'hGLLQ wQRLD'
    >>> encode('')
    ''
    >>> encode('123!@#')
    '123!@#'
    """
    encoded_chars = []
    # Use a set for efficient vowel lookup (case-insensitive)
    LOWER_VOWELS = {'a', 'e', 'i', 'o', 'u'}

    for char in message:
        if not char.isalpha():
            # If not a letter, append as is
            encoded_chars.append(char)
            continue

        # Step 2a: Determine if the original character was lowercase
        # This will be used to decide the FINAL case (swapped)
        is_original_char_lower = char.islower()
        
        # Step 2b: Determine the character to potentially shift
        # We start with the original character
        char_to_modify = char

        # Check if the character is a vowel (case-insensitive)
        if char.lower() in LOWER_VOWELS:
            # If it's a vowel, replace with letter 2 places ahead.
            # The shift should maintain the current case context (e.g., 'a' -> 'c', 'A' -> 'C').
            # For standard English vowels, adding 2 to the ordinal value is sufficient
            # and does not require wrap-around logic as they are not near the end of the alphabet.
            shifted_ord = ord(char_to_modify) + 2
            char_to_modify = chr(shifted_ord)
        
        # Step 2c: Apply the final case swap
        # If the original character was lowercase, the final char becomes uppercase.
        # If the original character was uppercase, the final char becomes lowercase.
        if is_original_char_lower:
            encoded_chars.append(char_to_modify.upper())
        else: # Original char was uppercase
            encoded_chars.append(char_to_modify.lower())
            
    return "".join(encoded_chars)