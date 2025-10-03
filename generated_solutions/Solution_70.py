def strange_sort_list(integers: list) -> list:
    """
    Given a list of integers, return a list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    """
    if not integers:
        return []

    # Step 1: Sort the input list. This makes finding min/max efficient.
    # We create a copy to avoid modifying the original list.
    sorted_nums = sorted(integers)

    # Step 2: Initialize two pointers, one for the start (min) and one for the end (max).
    left = 0
    right = len(sorted_nums) - 1

    # Step 3: Initialize the result list.
    result = []

    # Step 4: Use a flag to alternate between picking the minimum and maximum.
    # Start with True to pick the minimum first.
    is_min_turn = True

    # Step 5: Loop until the pointers cross each other.
    while left <= right:
        if is_min_turn:
            # It's time to pick the current minimum
            result.append(sorted_nums[left])
            left += 1  # Move the left pointer inwards
        else:
            # It's time to pick the current maximum
            result.append(sorted_nums[right])
            right -= 1 # Move the right pointer inwards
        
        # Toggle the turn for the next iteration
        is_min_turn = not is_min_turn
        
    return result