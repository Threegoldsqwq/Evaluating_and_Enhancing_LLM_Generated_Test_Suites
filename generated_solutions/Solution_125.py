def split_words(text: str):
    """
    Given a string of words, return a list of words split on whitespace,
    if no whitespaces exists in the text you should split on commas ',',
    if no commas exists you should return the number of lower-case letters
    with odd order in the alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    """

    # Rule 1: Check for whitespace. If found, split by whitespace.
    # The any() function combined with char.isspace() efficiently checks for any whitespace character.
    if any(char.isspace() for char in text):
        return text.split()

    # Rule 2: If no whitespace, check for commas. If found, split by commas.
    if ',' in text:
        return text.split(',')

    # Rule 3: If neither whitespace nor commas are found, count odd-ordered lowercase letters.
    odd_order_count = 0
    for char in text:
        # Check if the character is a lowercase English letter.
        if 'a' <= char <= 'z':
            # Calculate the 0-indexed alphabetical order.
            # 'a' is 0, 'b' is 1, 'c' is 2, etc.
            order = ord(char) - ord('a')
            # Check if the order is an odd number.
            if order % 2 != 0:
                odd_order_count += 1
    return odd_order_count