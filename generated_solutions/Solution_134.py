def check_if_last_char_is_a_letter(s: str) -> bool:
    """
    Returns True if the last character of a given string is an alphabetical character
    and is not a part of a word, and False otherwise.

    "word" is a group of characters separated by space.
    This means the last alphabetical character must either be the only character
    in the string, or be immediately preceded by a space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False
    check_if_last_char_is_a_letter("a") ➞ True
    check_if_last_char_is_a_letter(" a") ➞ True
    check_if_last_char_is_a_letter("word") ➞ False
    """
    # 1. Handle empty string: Cannot have a last character.
    if not s:
        return False

    last_char = s[-1]

    # 2. Check if the last character is alphabetical.
    if not last_char.isalpha():
        return False

    # At this point, we know the last character is an alphabet.
    # Now, check if it's "not a part of a word".
    # This means it's a standalone character word.

    # 3. Check if it's a standalone character word.
    if len(s) == 1:
        # If the string has only one character, and it's alphabetical,
        # it is a standalone word.
        return True
    else:
        # If the string has more than one character, check the character
        # immediately before the last one.
        second_to_last_char = s[-2]
        if second_to_last_char == ' ':
            # If the character before the last one is a space,
            # the last_char is a standalone word.
            return True
        else:
            # Otherwise, the last_char is part of a multi-character word.
            return False