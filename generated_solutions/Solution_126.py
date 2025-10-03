import collections

def is_sorted(numbers: list[int]) -> bool:
    """
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Args:
        numbers: A list of non-negative integers.

    Returns:
        True if the list is sorted in ascending order and no number appears
        more than twice; False otherwise.
    """

    # Condition 1: Check for duplicates exceeding two occurrences.
    # Use collections.Counter to get a frequency map of all numbers.
    counts = collections.Counter(numbers)

    # Iterate through the counts of each unique number.
    for num_count in counts.values():
        # If any number appears more than twice, return False.
        if num_count > 2:
            return False

    # Condition 2: Check if the list is sorted in ascending order.
    # An empty list or a list with one element is considered sorted by default.
    if len(numbers) <= 1:
        return True

    # Iterate through the list, comparing each element with its successor.
    # We only need to go up to the second-to-last element.
    for i in range(len(numbers) - 1):
        # If a number is greater than the one that follows it, the list is not sorted.
        if numbers[i] > numbers[i+1]:
            return False

    # If all checks pass (no excessive duplicates and list is in ascending order),
    # then the list meets the criteria.
    return True