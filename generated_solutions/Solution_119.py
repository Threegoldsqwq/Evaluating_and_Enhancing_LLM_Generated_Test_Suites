def is_good(s: str) -> bool:
    """
    Checks if a string of parentheses is balanced (good).

    Args:
        s: The input string consisting only of '(' and ')'.

    Returns:
        True if the string is balanced, False otherwise.
    """
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        
        # If balance ever drops below zero, it means we have a closing
        # parenthesis without a corresponding open one, so it's not good.
        if balance < 0:
            return False
            
    # For a string to be good, the final balance must be zero, meaning
    # all open parentheses have been matched by a closing one.
    return balance == 0

def match_parens(lst: list[str]) -> str:
    """
    Checks if it's possible to concatenate two strings of parentheses
    in some order to form a good (balanced) string.

    Args:
        lst: A list of two strings, both consisting of '(' and ')'.

    Returns:
        'Yes' if a good string can be formed, 'No' otherwise.
    """
    s1 = lst[0]
    s2 = lst[1]

    # Try concatenating s1 followed by s2
    combined1 = s1 + s2
    if is_good(combined1):
        return 'Yes'

    # If the first order didn't work, try s2 followed by s1
    combined2 = s2 + s1
    if is_good(combined2):
        return 'Yes'

    # If neither order results in a good string
    return 'No'