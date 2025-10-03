def separate_paren_groups(paren_string: str) -> list[str]:
    """
    Separates a string containing multiple groups of nested parentheses into a list of
    individual group strings.

    Separate groups are balanced and not nested within each other.
    Spaces in the input string are ignored.

    Args:
        paren_string: A string containing groups of parentheses and spaces.

    Returns:
        A list of strings, where each string is a separate, balanced parenthesis group.

    Examples:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
        >>> separate_paren_groups('')
        []
        >>> separate_paren_groups('()')
        ['()']
        >>> separate_paren_groups('(())')
        ['(())']
        >>> separate_paren_groups('   (  )   ( ( ) ) ')
        ['()', '(())']
    """
    # 1. Ignore any spaces by creating a filtered string.
    filtered_string = paren_string.replace(' ', '')

    result = []
    current_group_chars = []
    balance = 0

    # 2. Iterate through the characters of the filtered string.
    for char in filtered_string:
        # Add the current character to the temporary group builder.
        current_group_chars.append(char)

        # Update the balance counter.
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1

        # If balance returns to 0, it signifies the end of a complete,
        # top-level parenthesis group.
        if balance == 0:
            # Join the characters collected for this group and add to the result.
            result.append("".join(current_group_chars))
            # Reset the temporary group builder for the next group.
            current_group_chars = []
            
        # Note: If balance becomes negative, it implies an invalid input string
        # (e.g., ')(' without preceding '('). The problem statement implies valid
        # groupings for the *separate* groups. Our logic handles it by simply
        # continuing, and only capturing groups that eventually balance to 0.
        # If the input ends with a non-zero balance (e.g., '(('), the remaining
        # `current_group_chars` will not be added to the result, which is correct
        # as it's not a balanced group.

    return result