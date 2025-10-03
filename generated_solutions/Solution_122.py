import math

def sum_at_most_two_digits_from_first_k(arr: list[int], k: int) -> int:
    """
    Calculates the sum of elements with at most two digits from the first k elements of arr.

    Args:
        arr: A non-empty list of integers.
        k: An integer representing the number of initial elements to consider.

    Returns:
        The sum of qualifying elements.
    """
    total_sum = 0

    # Iterate through the first k elements of the array
    # The range function goes from 0 up to k-1
    for i in range(k):
        current_num = arr[i]

        # Check if the number has at most two digits.
        # This means its absolute value must be less than 100.
        # Examples:
        #   3   -> abs(3) = 3   < 100 (True)
        #   21  -> abs(21) = 21 < 100 (True)
        #   -5  -> abs(-5) = 5  < 100 (True)
        #   -99 -> abs(-99) = 99 < 100 (True)
        #   111 -> abs(111) = 111 < 100 (False)
        #   -100 -> abs(-100) = 100 < 100 (False)
        if abs(current_num) < 100:
            total_sum += current_num

    return total_sum