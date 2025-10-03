def process_and_sum_list(lst: list[int]) -> int:
    """
    This function takes a list of integers. For all entries in the list, the function shall square
    the integer entry if its index is a multiple of 3 and will cube the integer entry if its index
    is a multiple of 4 and not a multiple of 3. The function will not change the entries in the
    list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries.

    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    total_sum = 0

    for index, value in enumerate(lst):
        if index % 3 == 0:
            # If the index is a multiple of 3, square the entry.
            # This condition takes precedence.
            total_sum += value ** 2
        elif index % 4 == 0:
            # If the index is a multiple of 4 AND not a multiple of 3 (because the
            # previous 'if' would have caught multiples of 3), cube the entry.
            total_sum += value ** 3
        else:
            # Otherwise (index is not a multiple of 3 and not a multiple of 4),
            # the entry remains unchanged.
            total_sum += value
            
    return total_sum