def exchange(lst1, lst2):
    """
    Determines whether it is possible to perform an exchange of elements
    between lst1 and lst2 to make lst1 a list of only even numbers.

    Args:
        lst1: A list of integers. (Assumed non-empty)
        lst2: A list of integers. (Assumed non-empty)

    Returns:
        "YES" if it is possible, "NO" otherwise.
    """

    # Step 1: Count the number of odd elements in lst1.
    # These are the elements that need to be replaced.
    odds_in_lst1 = 0
    for number in lst1:
        if number % 2 != 0:  # If the number is odd
            odds_in_lst1 += 1

    # Step 2: Count the number of even elements in lst2.
    # These are the elements available to replace the odd numbers in lst1.
    evens_in_lst2 = 0
    for number in lst2:
        if number % 2 == 0:  # If the number is even
            evens_in_lst2 += 1

    # Step 3: Compare the counts.
    # If we have enough even numbers in lst2 to replace all the odd numbers in lst1,
    # then it's possible.
    if evens_in_lst2 >= odds_in_lst1:
        return "YES"
    else:
        return "NO"