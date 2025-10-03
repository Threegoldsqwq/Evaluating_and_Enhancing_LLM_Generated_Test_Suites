def flip_case(text: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    Characters that are not letters (e.g., numbers, symbols, spaces) remain unchanged.

    Args:
        text: The input string.

    Returns:
        The string with the case of letters flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
        >>> flip_case('pYtHoN 123!')
        'PyThOn 123!'
        >>> flip_case('TEST')
        'test'
        >>> flip_case('test')
        'TEST'
        >>> flip_case('')
        ''
        >>> flip_case('AbC-DeF')
        'aBc-dEf'
    """
    flipped_chars = []
    for char in text:
        if char.islower():
            # If the character is lowercase, convert it to uppercase
            flipped_chars.append(char.upper())
        elif char.isupper():
            # If the character is uppercase, convert it to lowercase
            flipped_chars.append(char.lower())
        else:
            # If the character is not an alphabet (e.g., number, symbol, space),
            # or if it's neither upper nor lower (like some Unicode characters),
            # append it as is.
            flipped_chars.append(char)

    # Join the list of characters back into a single string
    return "".join(flipped_chars)