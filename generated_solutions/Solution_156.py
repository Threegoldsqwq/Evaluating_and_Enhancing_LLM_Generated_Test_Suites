def int_to_mini_roman(num: int) -> str:
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    The Roman numeral system is based on seven symbols:
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

    Numbers are formed by combining these symbols. Generally, symbols are placed
    from largest to smallest value from left to right. However, there are
    six special cases where a smaller value symbol is placed before a larger
    value symbol to indicate subtraction:
    IV = 4 (5 - 1)
    IX = 9 (10 - 1)
    XL = 40 (50 - 10)
    XC = 90 (100 - 10)
    CD = 400 (500 - 100)
    CM = 900 (1000 - 100)

    This function uses a greedy approach: it iterates through the Roman numeral
    values (including the subtractive combinations) from largest to smallest.
    For each value, it repeatedly subtracts it from the input number and appends
    the corresponding Roman symbol to the result until the input number is
    smaller than the current value.

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    >>> int_to_mini_roman(1) == 'i'
    >>> int_to_mini_roman(1000) == 'm'
    """
    if not (1 <= num <= 1000):
        raise ValueError("Input number must be between 1 and 1000, inclusive.")

    # Define the mapping of values to Roman numeral symbols,
    # sorted in descending order of value.
    # Include the special subtractive cases (e.g., 900, 400, 90, 40, 9, 4)
    # to ensure they are handled before their additive components.
    # The symbols are already in lowercase as required by the problem.
    roman_map = [
        (1000, 'm'),
        (900, 'cm'),
        (500, 'd'),
        (400, 'cd'),
        (100, 'c'),
        (90, 'xc'),
        (50, 'l'),
        (40, 'xl'),
        (10, 'x'),
        (9, 'ix'),
        (5, 'v'),
        (4, 'iv'),
        (1, 'i')
    ]

    result_parts = []
    
    # Iterate through the roman_map.
    # For each value-symbol pair, subtract the value from num as many times
    # as possible, appending the symbol to our result list each time.
    for value, symbol in roman_map:
        while num >= value:
            result_parts.append(symbol)
            num -= value
            
    # Join all the collected Roman numeral parts into a single string.
    return "".join(result_parts)