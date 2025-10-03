def common(list1, list2):
    """
    Returns sorted unique common elements for two lists.

    Args:
        list1 (list): The first list of elements.
        list2 (list): The second list of elements.

    Returns:
        list: A sorted list of unique elements that are present in both input lists.

    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
        >>> common([], [1, 2, 3])
        []
        >>> common([1, 1, 2, 2], [2, 2, 3, 3])
        [2]
    """
    # Convert both lists to sets. This automatically handles:
    # 1. Removing duplicate elements within each list.
    # 2. Providing efficient operations for finding common elements (intersection).
    set1 = set(list1)
    set2 = set(list2)

    # Find the intersection of the two sets.
    # The intersection will contain only elements that are present in both sets,
    # and it will naturally be unique.
    common_elements_set = set1.intersection(set2)
    # Alternatively, you can use the '&' operator for intersection:
    # common_elements_set = set1 & set2

    # Convert the resulting set of common elements back into a list.
    common_elements_list = list(common_elements_set)

    # Sort the list in ascending order as required by the problem description.
    common_elements_list.sort()

    return common_elements_list