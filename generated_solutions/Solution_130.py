def tribonacci(n: int) -> list[int]:
    """
    Calculates the first n+1 numbers of the custom Tribonacci sequence.

    The sequence is defined as:
    tri(0) = 1 (inferred from example)
    tri(1) = 3
    tri(k) = 1 + k // 2, if k is even.
    tri(k) = tri(k - 1) + tri(k - 2) + tri(k + 1), if k is odd.

    Args:
        n: A non-negative integer, representing the upper bound of the
           sequence index. The function returns tri(0) to tri(n).

    Returns:
        A list of integers representing tri(0), tri(1), ..., tri(n).
    """

    if n < 0:
        # According to the problem statement, n is non-negative.
        # This case handles invalid input defensively.
        return []

    # Initialize a list to store the sequence values.
    # dp[k] will store the value of tri(k).
    dp = [0] * (n + 1)

    # Base cases for the sequence
    # tri(0) is inferred from the example output: tri(3) = [1, 3, 2, 8]
    dp[0] = 1

    # tri(1) is explicitly given in the problem definition
    if n >= 1:
        dp[1] = 3

    # Calculate subsequent terms using dynamic programming
    for i in range(2, n + 1):
        if i % 2 == 0:  # If i is an even number
            # tri(i) = 1 + i / 2 (using integer division)
            dp[i] = 1 + i // 2
        else:  # If i is an odd number
            # tri(i) = tri(i - 1) + tri(i - 2) + tri(i + 1)
            # tri(i - 1) and tri(i - 2) are already in dp
            # For tri(i + 1): since i is odd, i + 1 is even.
            # We can calculate tri(i + 1) using the even rule directly.
            tri_i_plus_1 = 1 + (i + 1) // 2
            dp[i] = dp[i - 1] + dp[i - 2] + tri_i_plus_1

    return dp