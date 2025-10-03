def specialFilter(numbers: list[int]) -> int:
    """
    Counts the number of elements in an array that are greater than 10 and 
    whose first and last digits are both odd.

    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in numbers:
        # Condition 1: The number must be greater than 10
        if num > 10:
            # Condition 2: Both the first and last digits must be odd.
            # We consider the digits of the absolute value of the number.
            
            # Get the absolute value to handle negative numbers consistently for digit extraction
            abs_num = abs(num)

            # Extract the last digit
            # For any integer N, the last digit is N % 10
            last_digit = abs_num % 10

            # Extract the first digit
            # Convert the number to a string to easily get its first character
            str_num = str(abs_num)
            first_digit = int(str_num[0])

            # Check if both extracted digits are odd
            # An odd number modulo 2 is 1 (or -1 for negative, but our digits are positive).
            # An even number modulo 2 is 0.
            if last_digit % 2 != 0 and first_digit % 2 != 0:
                count += 1
                
    return count