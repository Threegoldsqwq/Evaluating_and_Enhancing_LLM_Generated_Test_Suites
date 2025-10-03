def total_sum_binary(N: int) -> str:
    """
    Given a positive integer N, return the total sum of its digits in binary.

    Args:
        N (int): The input integer. Constraints: 0 <= N <= 10000.

    Returns:
        str: A string representing the binary sum of N's decimal digits.
    """
    
    # Step 1: Calculate the sum of the decimal digits of N
    digit_sum = 0
    
    # Convert N to a string to easily iterate through its digits.
    # This approach handles N=0 correctly as str(0) is '0'.
    for digit_char in str(N):
        digit_sum += int(digit_char)
            
    # Step 2: Convert the calculated digit_sum to its binary representation.
    # The built-in bin() function returns a string prefixed with "0b".
    # We slice the string [2:] to remove this prefix.
    binary_string = bin(digit_sum)[2:]
    
    return binary_string