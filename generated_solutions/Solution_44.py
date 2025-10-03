def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return "0"

    # The result will be built by prepending digits, so start with an empty string.
    result = ""
    
    # Loop until x becomes 0
    while x > 0:
        # Get the remainder, which is the next digit in the new base
        remainder = x % base
        
        # Prepend the digit to the result string
        # Since base is less than 10, remainder will be a single digit (0-9)
        result = str(remainder) + result
        
        # Update x by integer division
        x = x // base
        
    return result