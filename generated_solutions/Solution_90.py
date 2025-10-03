def next_smallest(numbers):
    """
    Returns the 2nd smallest unique element of the list.
    Returns None if there is no such element (e.g., list is empty,
    has only one unique element, or fewer than two elements).
    """
    # 1. Handle empty list immediately
    if not numbers:
        return None

    # 2. Get unique elements and sort them
    # Converting to a set removes duplicates, then converting back to a list
    # allows sorting.
    unique_sorted_numbers = sorted(list(set(numbers)))

    # 3. Check if there are at least two unique elements
    if len(unique_sorted_numbers) < 2:
        # If there are 0 or 1 unique elements, there's no 2nd smallest
        return None
    else:
        # The second smallest unique element is at index 1 (0-indexed)
        return unique_sorted_numbers[1]