from collections import Counter

def remove_duplicates(numbers: list[int]) -> list[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    First, count the occurrences of each number in the input list.
    Then, iterate through the original list again and add only those numbers
    to the result list that appeared exactly once.

    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    >>> remove_duplicates([1, 1, 2, 3, 3, 4, 5, 5])
    [2, 4]
    >>> remove_duplicates([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> remove_duplicates([])
    []
    >>> remove_duplicates([7, 7, 7, 7])
    []
    """
    # Step 1: Count occurrences of each number in the input list.
    # collections.Counter is an efficient way to create a frequency map.
    # For example, Counter([1, 2, 3, 2, 4]) will result in {1: 1, 2: 2, 3: 1, 4: 1}
    counts = Counter(numbers)

    # Step 2: Build the result list.
    # Iterate through the original list to preserve the order of elements.
    # Add a number to the result only if its count is exactly 1.
    result = []
    for number in numbers:
        if counts[number] == 1:
            result.append(number)

    return result