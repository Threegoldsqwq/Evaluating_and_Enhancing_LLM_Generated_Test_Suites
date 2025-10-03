def rounded_avg(n: int, m: int) -> str | int:
    """
    Computes the average of integers from n through m (inclusive),
    rounds the answer to the nearest integer, and converts that to binary.

    If n is greater than m, it returns -1.

    Args:
        n: A positive integer, the start of the range.
        m: A positive integer, the end of the range.

    Returns:
        A string representing the binary form of the rounded average (e.g., "0b11"),
        or -1 if n > m.
    """
    if n > m:
        return -1

    # Calculate the number of integers in the range [n, m]
    # count = m - n + 1
    num_elements = m - n + 1

    # Calculate the sum of integers from n to m using the arithmetic series formula:
    # Sum = (number of terms) * (first term + last term) / 2
    # We use integer division `//` here because (n + m) * num_elements is always even.
    # This avoids potential floating-point inaccuracies in intermediate sums.
    total_sum = (n + m) * num_elements // 2

    # Calculate the average. This division will result in a float.
    average = total_sum / num_elements

    # Round the average to the nearest integer.
    # Python's `round()` function rounds halves to the nearest even integer
    # (e.g., round(2.5) is 2, round(3.5) is 4), which matches the problem's examples.
    rounded_value = round(average)

    # Convert the rounded integer to its binary string representation.
    # The `bin()` function returns a string prefixed with "0b".
    binary_representation = bin(rounded_value)

    return binary_representation