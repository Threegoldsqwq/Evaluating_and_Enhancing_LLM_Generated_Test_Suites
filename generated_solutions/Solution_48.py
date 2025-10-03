def is_palindrome(s: str) -> bool:
    """
    Checks if given string is a palindrome
        >>> is_palindrome('')
        True
        >>> is_palindrome('aba')
        True
        >>> is_palindrome('aaaaa')
        True
        >>> is_palindrome('zbcd')
        False
    """
    return s == s[::-1]