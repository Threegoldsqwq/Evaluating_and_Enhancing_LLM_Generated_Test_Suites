def pairs_sum_to_zero(numbers: list[int]) -> bool:
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    >>> pairs_sum_to_zero([-1, 1])
    True
    >>> pairs_sum_to_zero([0, 0]) # Two distinct zeros sum to zero
    True
    >>> pairs_sum_to_zero([])
    False
    """
    # We use a set to keep track of numbers we have already seen.
    # Sets provide efficient O(1) average time complexity for lookups (checking if an element exists).
    seen_numbers = set()

    for num in numbers:
        # For each number 'num', we are looking for its complement '-num'.
        # If 'num' and '-num' exist in the list and are distinct, they sum to zero.
        # By checking if '-num' is in 'seen_numbers', we ensure that 'num' and '-num'
        # are distinct in terms of their position in the list (one was seen before the other).
        # This also correctly handles the case of two zeros: if the first 0 is added to
        # seen_numbers, the second 0 will find its complement (0) in seen_numbers.
        if -num in seen_numbers:
            return True
        
        # If the complement is not found, add the current number to the set of seen numbers.
        seen_numbers.add(num)
    
    # If we iterate through the entire list and don't find any such pair, return False.
    return False