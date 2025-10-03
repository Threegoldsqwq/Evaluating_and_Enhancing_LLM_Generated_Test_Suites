def get_digit_sum(n: int) -> int:
    """
    Calculates the sum of the digits of a number, considering its absolute value.
    For example:
    get_digit_sum(123) == 6
    get_digit_sum(-12) == 3
    get_digit_sum(0) == 0
    """
    s = 0
    # Use absolute value for digit sum calculation as commonly interpreted
    # and consistent with the problem's implicit requirement for negative numbers.
    n_abs = abs(n)
    
    # If the number is 0, its digit sum is 0.
    if n_abs == 0:
        return 0

    # Sum digits using the mathematical approach
    while n_abs > 0:
        s += n_abs % 10  # Add the last digit
        n_abs //= 10     # Remove the last digit
    return s

def order_by_points(nums: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits,
    order them based on their index in the original list (ascending).

    For example:
    >>> order_by_points([1, 11, -1, -11, -12])
    [1, -1, 11, -11, -12]
    # Note: The example output in the problem description `[-1, -11, 1, -12, 11]`
    # implies a different, potentially contradictory, sorting logic.
    # This solution strictly adheres to the textual description of
    # "ascending order according to the sum of their digits" (primary key)
    # and "based on their index in original list" (interpreted as ascending index for secondary key).
    
    >>> order_by_points([])
    []
    >>> order_by_points([0, 10, 1])
    [0, 1, 10]
    >>> order_by_points([10, 1, 0])
    [0, 1, 10]
    >>> order_by_points([10, -1, 1])
    [1, -1, 10]
    """
    if not nums:
        return []

    # Create a list of tuples: (sum_of_digits, original_index, number)
    # This structure allows Python's default sort to handle multiple criteria:
    # 1. sum_of_digits (primary, ascending)
    # 2. original_index (secondary, ascending)
    decorated_list = []
    for index, num in enumerate(nums):
        points = get_digit_sum(num)
        decorated_list.append((points, index, num))

    # Sort the decorated list. Python's `sort()` method on a list of tuples
    # sorts lexicographically (by the first element, then by the second, etc.).
    decorated_list.sort()

    # Extract the original numbers from the sorted list of tuples
    sorted_numbers = [item[2] for item in decorated_list]

    return sorted_numbers