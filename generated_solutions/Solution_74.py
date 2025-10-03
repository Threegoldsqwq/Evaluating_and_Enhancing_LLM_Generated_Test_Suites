def total_match(lst1: list[str], lst2: list[str]) -> list[str]:
    """
    Accepts two lists of strings and returns the list that has
    a total number of characters (sum of lengths of all strings)
    less than the other list.

    If the two lists have the same total number of characters,
    the first list (lst1) is returned.

    Examples:
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    """
    # Calculate the total number of characters for the first list
    total_chars_lst1 = sum(len(s) for s in lst1)

    # Calculate the total number of characters for the second list
    total_chars_lst2 = sum(len(s) for s in lst2)

    # Compare the totals and return the appropriate list
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    elif total_chars_lst2 < total_chars_lst1:
        return lst2
    else:
        # If the total number of characters is the same, return the first list
        return lst1