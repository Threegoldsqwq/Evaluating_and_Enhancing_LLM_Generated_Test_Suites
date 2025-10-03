def unique_digits(x: list[int]) -> list[int]:
    """
    Given a list of positive integers x, return a sorted list of all 
    elements that hasn't any even digit.

    Args:
        x: A list of positive integers.

    Returns:
        A sorted list of integers from x that contain only odd digits.
    """
    
    def has_only_odd_digits(n: int) -> bool:
        """
        Helper function to check if an integer contains only odd digits.
        """
        # If the number is 0 (though problem states positive integers,
        # 0 as a digit needs to be handled)
        # The digit 0 is even.
        if n == 0: 
            return False 
            
        current_num = n
        while current_num > 0:
            digit = current_num % 10  # Get the last digit
            if digit % 2 == 0:        # Check if the digit is even
                return False          # If any digit is even, return False immediately
            current_num //= 10        # Remove the last digit
        return True                   # If loop completes, all digits were odd

    result = []
    for number in x:
        if has_only_odd_digits(number):
            result.append(number)
            
    result.sort() # Sort the collected numbers in increasing order
    return result