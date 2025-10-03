def digits(n: int) -> int:
    """
    Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.

    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product_of_odd_digits = 1  # Initialize product to 1
    found_odd_digit = False    # Flag to track if any odd digit was found

    # Use a temporary variable to iterate through digits without modifying the original n
    current_number = n

    # Loop as long as there are digits left in the number
    while current_number > 0:
        digit = current_number % 10  # Get the last digit
        
        # Check if the digit is odd
        if digit % 2 != 0:
            product_of_odd_digits *= digit  # Multiply if odd
            found_odd_digit = True          # Set flag to True
        
        current_number //= 10  # Remove the last digit

    # After checking all digits, return the result based on the flag
    if found_odd_digit:
        return product_of_odd_digits
    else:
        return 0  # No odd digits found, so return 0