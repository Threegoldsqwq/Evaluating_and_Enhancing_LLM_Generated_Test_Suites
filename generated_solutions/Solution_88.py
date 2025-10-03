def sort_array(arr: list[int]) -> list[int]:
    """
    Sorts an array of non-negative integers based on the parity of the sum
    of its first and last elements.

    Args:
        arr: A list of non-negative integers.

    Returns:
        A new list, sorted according to the rules:
        - Ascending if sum(first, last) is odd.
        - Descending if sum(first, last) is even.
        Returns an empty list if the input is empty.
    """
    # 1. Handle the empty array edge case
    if not arr:
        return []

    # For arrays with a single element (e.g., [5]), arr[0] and arr[-1] will
    # both be that single element. The logic will correctly apply:
    # Example: [5] -> sum = 5+5=10 (even) -> sort descending -> [5]
    # So, no special handling for len(arr) == 1 is explicitly needed.

    # 2. Get the first and last elements and calculate their sum
    first_element = arr[0]
    last_element = arr[-1]
    elements_sum = first_element + last_element

    # 3. Determine sorting order and return the new sorted list
    if elements_sum % 2 != 0:  # Sum is odd
        # Sort in ascending order
        return sorted(arr)
    else:  # Sum is even
        # Sort in descending order
        return sorted(arr, reverse=True)