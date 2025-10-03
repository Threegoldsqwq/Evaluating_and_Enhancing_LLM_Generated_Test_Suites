def count_even_odd_palindromes(n: int) -> tuple[int, int]:
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    even_palindromes = 0
    odd_palindromes = 0

    for i in range(1, n + 1):
        # Convert the number to a string to check if it's a palindrome
        s_i = str(i)
        
        # Check if the string is equal to its reverse
        if s_i == s_i[::-1]:
            # If it's a palindrome, check if it's even or odd
            if i % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1
                
    return (even_palindromes, odd_palindromes)