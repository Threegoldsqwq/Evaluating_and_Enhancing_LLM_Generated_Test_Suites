def get_odd_collatz(n: int) -> list[int]:
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    odd_numbers = set()  # Use a set to store unique odd numbers
    current_num = n

    while True:
        # Check if the current number is odd and add it to the set
        if current_num % 2 != 0:
            odd_numbers.add(current_num)
        
        # If we reached 1, we stop the sequence
        if current_num == 1:
            break
        
        # Apply the Collatz rule to get the next number in the sequence
        if current_num % 2 == 0:  # If current_num is even
            current_num //= 2
        else:  # If current_num is odd
            current_num = 3 * current_num + 1
            
    # Convert the set of odd numbers to a list and sort it
    result_list = list(odd_numbers)
    result_list.sort()  # Sort in increasing order
    
    return result_list