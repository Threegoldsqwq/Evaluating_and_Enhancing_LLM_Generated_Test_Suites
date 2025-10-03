def generate_integers(a: int, b: int) -> list[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # 1. Determine the actual lower and upper bounds of the range
    low = min(a, b)
    high = max(a, b)

    result = []
    
    # 2. The even digits are 0, 2, 4, 6, 8.
    # Since 'a' and 'b' are positive integers (>= 1), the smallest possible 'low' is 1.
    # Therefore, 0 will never satisfy the condition 'low <= 0 <= high'.
    # We only need to check the even digits from 2 upwards.
    
    # 3. Iterate through possible even digits (2, 4, 6, 8)
    for digit in [2, 4, 6, 8]:
        # 4. Check if the current digit falls within the specified range
        if low <= digit <= high:
            # 5. If it does, add it to the result list
            result.append(digit)
            
    # 6. Return the list of even digits found in ascending order
    return result