def sort_numbers(number_string: str) -> str:
    """
    Sorts a space-delimited string of number words from 'zero' to 'nine'
    by their numerical value.

    Args:
        number_string: A string containing space-delimited number words
                       (e.g., 'three one five').

    Returns:
        A string with the number words sorted from smallest to largest,
        space-delimited (e.g., 'one three five').

    Examples:
        >>> sort_numbers('three one five')
        'one three five'
        >>> sort_numbers('nine two zero eight')
        'zero two eight nine'
        >>> sort_numbers('four')
        'four'
        >>> sort_numbers('')
        ''
    """
    # 1. Create a mapping from number words to their integer values
    word_to_int = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    # 2. Split the input string into a list of number words
    words = number_string.split()

    # 3. Sort the list of words using the integer mapping as the key
    # The 'key' argument takes a function that is called on each element
    # of the list to produce a comparison key.
    sorted_words = sorted(words, key=lambda word: word_to_int[word])

    # 4. Join the sorted words back into a single space-delimited string
    return ' '.join(sorted_words)