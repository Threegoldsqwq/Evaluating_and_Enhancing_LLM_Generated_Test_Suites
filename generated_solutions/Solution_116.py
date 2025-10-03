def sort_array(arr: list[int]) -> list[int]:
    """
    Sorts an array of integers according to the number of ones in their binary
    representation (ascending). For numbers with the same count of ones,
    they are sorted based on their decimal value (ascending).

    Interpretation of "number of ones" for all integers:
    - For non-negative integers (n >= 0), `n.bit_count()` is used (available in Python 3.10+).
    - For negative integers (n < 0), `abs(n).bit_count()` is used. This extends
      the concept of "number of ones in binary representation" to negative numbers
      in a common and general way, as Python's `int.bit_count()` raises an error
      for negative numbers, and no specific fixed-width two's complement
      representation is implied.

    Note on the provided examples in the problem description:
    The examples appear to demonstrate simple decimal sorting, not sorting by bit count,
    and thus contradict the stated sorting rule for positive numbers. The solution below
    strictly implements the *textual description* of the sorting rule.

    For clarity, here's how this implementation would process the examples:

    1. Input: `[1, 5, 2, 3, 4]`
       - 1 (0b1): 1 one
       - 2 (0b10): 1 one
       - 3 (0b11): 2 ones
       - 4 (0b100): 1 one
       - 5 (0b101): 2 ones
       - Pairs (ones_count, value): `(1, 1), (1, 2), (1, 4), (2, 3), (2, 5)`
       - **Result:** `[1, 2, 4, 3, 5]` (Problem's expected: `[1, 2, 3, 4, 5]`)

    2. Input: `[-2, -3, -4, -5, -6]`
       - -2 (abs: 2, 0b10): 1 one
       - -3 (abs: 3, 0b11): 2 ones
       - -4 (abs: 4, 0b100): 1 one
       - -5 (abs: 5, 0b101): 2 ones
       - -6 (abs: 6, 0b110): 2 ones
       - Pairs (ones_count, value): `(1, -2), (2, -3), (1, -4), (2, -5), (2, -6)`
       - Sorted: `(1, -4), (1, -2), (2, -6), (2, -5), (2, -3)`
       - **Result:** `[-4, -2, -6, -5, -3]` (Problem's expected: `[-6, -5, -4, -3, -2]`)

    3. Input: `[1, 0, 2, 3, 4]`
       - 0 (0b0): 0 ones
       - 1 (0b1): 1 one
       - 2 (0b10): 1 one
       - 3 (0b11): 2 ones
       - 4 (0b100): 1 one
       - Pairs (ones_count, value): `(0, 0), (1, 1), (1, 2), (1, 4), (2, 3)`
       - **Result:** `[0, 1, 2, 4, 3]` (Problem's expected: `[0, 1, 2, 3, 4]`)
    """

    def get_ones_count(n: int) -> int:
        """
        Calculates the number of set bits (ones) in the binary representation of n.
        For negative numbers, it counts ones in the absolute value's binary representation.
        """
        if n >= 0:
            return n.bit_count()
        else:
            # For negative numbers, Python's bit_count() raises an error.
            # We use the count of set bits in the absolute value, which is a common
            # and generally applicable interpretation when fixed-width two's complement
            # is not specified.
            return abs(n).bit_count()

    # The sorting key is a tuple: (primary_key, secondary_key).
    # Python's `sorted` function sorts tuples lexicographically:
    # it first compares the first elements, then the second if the first are equal, and so on.
    return sorted(arr, key=lambda x: (get_ones_count(x), x))