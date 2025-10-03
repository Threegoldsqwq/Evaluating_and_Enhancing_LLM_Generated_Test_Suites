def fib(n: int) -> int:
    """
    Return n-th Fibonacci number.

    The Fibonacci sequence typically starts F(1)=1, F(2)=1, F(3)=2, ...
    This implementation handles n <= 0 by returning 0, consistent with F(0)=0.

    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(0)
    0
    >>> fib(-5)
    0
    """
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    # Initialize the first two Fibonacci numbers according to F(1)=1, F(2)=1
    # 'a' will store F(i-2) and 'b' will store F(i-1)
    a, b = 1, 1
    
    # Iterate from the 3rd number up to the n-th number
    # In each step, we calculate F(i) = F(i-1) + F(i-2)
    for _ in range(3, n + 1):
        # Calculate the next Fibonacci number
        next_fib = a + b
        
        # Update 'a' and 'b' for the next iteration:
        # The old 'b' becomes the new 'a'
        # The 'next_fib' becomes the new 'b'
        a = b
        b = next_fib
        
    # After the loop, 'b' will hold the n-th Fibonacci number
    return b