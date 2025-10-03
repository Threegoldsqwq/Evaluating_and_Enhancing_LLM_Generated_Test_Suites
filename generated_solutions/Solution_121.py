def solution(numbers):
    total_sum = 0  # Initialize a variable to store the sum of qualifying numbers

    # Iterate through the list, getting both the index and the number
    for index, num in enumerate(numbers):
        # Check if the current position (index) is even (0, 2, 4, ...)
        if index % 2 == 0:
            # If the position is even, now check if the number itself is odd
            if num % 2 != 0:
                # If both conditions are met, add the number to our total sum
                total_sum += num
                
    return total_sum # Return the final sum