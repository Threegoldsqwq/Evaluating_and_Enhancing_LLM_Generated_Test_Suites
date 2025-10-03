def find_k_largest_numbers(arr: list[int], k: int) -> list[int]:
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Args:
        arr: A list of integers.
        k: A non-negative integer representing the number of maximum elements to find.

    Returns:
        A sorted list of length k containing the k maximum numbers from arr.
        Returns an empty list if k is 0.
    """
    # Handle the edge case where k is 0.
    # According to constraints, 0 <= k <= len(arr).
    if k == 0:
        return []

    # Sort the array in ascending order.
    # This places the largest numbers at the end of the array.
    # Time complexity: O(N log N) where N is len(arr).
    # Space complexity: O(1) for in-place sort (Python's list.sort()).
    arr.sort()

    # The k largest numbers are the last k elements in the sorted array.
    # Slicing arr[-k:] extracts these elements.
    # This slice automatically returns them in sorted order.
    # Time complexity: O(k) for slicing.
    # Space complexity: O(k) for the new list created by the slice.
    result = arr[-k:]

    return result