def count_n_digit_start_end_with_1(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.

    Args:
        n: A positive integer representing the number of digits.

    Returns:
        The count of n-digit positive integers that start or end with 1.
    """
    if n == 1:
        # For n=1, the only 1-digit number that starts or ends with 1 is '1' itself.
        # (1-digit positive integers are 1, 2, ..., 9)
        # Numbers starting with 1: {1} (count = 1)
        # Numbers ending with 1: {1} (count = 1)
        # Numbers starting AND ending with 1: {1} (count = 1)
        # Using inclusion-exclusion: 1 + 1 - 1 = 1
        return 1
    else:
        # For n >= 2, we apply the Principle of Inclusion-Exclusion:
        # Count(A or B) = Count(A) + Count(B) - Count(A and B)

        # Count(A): Numbers that start with 1.
        # The first digit is 1 (1 choice). The remaining (n-1) digits can be 0-9 (10 choices each).
        # Count_starts_with_1 = 1 * 10**(n - 1)

        # Count(B): Numbers that end with 1.
        # The last digit is 1 (1 choice). The first digit can be 1-9 (9 choices).
        # The (n-2) middle digits can be 0-9 (10 choices each).
        # Count_ends_with_1 = 9 * 10**(n - 2) * 1

        # Count(A and B): Numbers that start AND end with 1.
        # The first digit is 1, the last digit is 1.
        # The (n-2) middle digits can be 0-9 (10 choices each).
        # Count_starts_and_ends_with_1 = 1 * 10**(n - 2) * 1

        # Total count = Count_starts_with_1 + Count_ends_with_1 - Count_starts_and_ends_with_1
        # Total count = 10**(n - 1) + 9 * 10**(n - 2) - 10**(n - 2)
        # Total count = 10**(n - 1) + (9 - 1) * 10**(n - 2)
        # Total count = 10 * 10**(n - 2) + 8 * 10**(n - 2)
        # Total count = (10 + 8) * 10**(n - 2)
        # Total count = 18 * 10**(n - 2)
        return 18 * (10**(n - 2))