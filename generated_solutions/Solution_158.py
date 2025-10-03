def find_max(words: list[str]) -> str | None:
    """
    Accepts a list of strings and returns the word with the maximum number
    of unique characters. If multiple strings have the maximum number of unique
    characters, it returns the one that comes first in lexicographical order.

    Args:
        words: A list of strings.

    Returns:
        The word with the maximum number of unique characters, or None if the
        input list is empty.
    """
    if not words:
        return None  # Return None for an empty input list

    max_unique_count = -1  # Initialize with a value lower than any possible unique char count
    result_string = None   # Initialize as None, to easily handle the first word

    for word in words:
        # Calculate the number of unique characters in the current word
        current_unique_count = len(set(word))

        if result_string is None:
            # This is the first word we're processing, so it's the best candidate so far
            max_unique_count = current_unique_count
            result_string = word
        elif current_unique_count > max_unique_count:
            # Found a word with more unique characters, so it's the new best
            max_unique_count = current_unique_count
            result_string = word
        elif current_unique_count == max_unique_count:
            # Found a word with the same number of unique characters (a tie)
            # Apply the tie-breaker: lexicographical order
            # If the current word comes earlier alphabetically, it's the new best
            if word < result_string:
                result_string = word
    
    return result_string