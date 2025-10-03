def list_sort(string_list: list[str]) -> list[str]:
    """
    Filters a list of strings to include only those with even lengths,
    then sorts the remaining strings. The sorting order is primarily
    by length (ascending) and secondarily alphabetically (ascending)
    for strings of the same length.

    Args:
        string_list: A list of strings. This list may contain duplicates.

    Returns:
        A new list containing only the even-length strings, sorted according
        to the specified rules.
    """

    # Step 1: Filter out strings that have an odd length.
    # A list comprehension efficiently creates a new list with only even-length strings.
    even_length_strings = [s for s in string_list if len(s) % 2 == 0]

    # Step 2: Sort the filtered list.
    # The 'sorted()' function returns a new sorted list without modifying the original.
    # The 'key' argument takes a function that extracts a comparison key from each element.
    # By returning a tuple (len(s), s), Python's default tuple comparison will:
    # 1. Compare the first elements (lengths). If different, that determines the order.
    # 2. If the first elements (lengths) are equal, it then compares the second elements (strings),
    #    which sorts them alphabetically.
    sorted_result = sorted(even_length_strings, key=lambda s: (len(s), s))

    return sorted_result