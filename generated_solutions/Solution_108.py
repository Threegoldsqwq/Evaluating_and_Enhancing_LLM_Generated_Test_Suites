def count_nums(arr: list[int]) -> int:
    """
    Counts the number of elements in an array of integers where the sum of
    its signed digits is greater than 0.

    If a number is negative, then its first signed digit will be negative.
    e.g. -123 has signed digits -1, 2, and 3.

    >>> count_nums([])
    0
    >>> count_nums([-1, 11, -11])
    1
    >>> count_nums([1, 1, 2])
    3
    >>> count_nums([-12, 12, -3])
    1
    >>> count_nums([0, 10, -10])
    1
    """

    def sum_signed_digits(n: int) -> int:
        """
        Calculates the sum of signed digits for a given integer n.
        The first digit is negative if n is negative, otherwise all digits are positive.
        """
        if n == 0:
            return 0
        
        s = str(n)
        digit_sum = 0
        
        if s[0] == '-':
            # For negative numbers, the first digit is negative
            # Example: -123 -> s = "-123"
            # s[1] is '1', so -int(s[1]) gives -1
            digit_sum += -int(s[1])
            # Remaining digits are positive
            for char_digit in s[2:]:
                digit_sum += int(char_digit)
        else:
            # For positive numbers, all digits are positive
            # Example: 123 -> s = "123"
            for char_digit in s:
                digit_sum += int(char_digit)
        
        return digit_sum

    count = 0
    for num in arr:
        if sum_signed_digits(num) > 0:
            count += 1
            
    return count