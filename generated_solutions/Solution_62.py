def derivative(xs):
    """
    xs represent coefficients of a polynomial.
        xs[0] + xs[1] * x + xs[2] * x^2 + ....
         Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    n = len(xs)

    # Handle edge cases for an empty or constant polynomial
    if n == 0:
        return []  # Derivative of an empty polynomial is an empty polynomial
    if n == 1:
        return [0] # Derivative of a constant (e.g., P(x)=3) is 0 (e.g., [0])

    # For P(x) = xs[0] + xs[1]*x + xs[2]*x^2 + ... + xs[n-1]*x^(n-1)
    # P'(x) = 1*xs[1] + 2*xs[2]*x + 3*xs[3]*x^2 + ... + (n-1)*xs[n-1]*x^(n-2)
    #
    # We iterate from the second coefficient (index 1) of the original polynomial,
    # as the first coefficient (index 0) represents the constant term which becomes 0.
    #
    # For each original coefficient xs[i] (which is the coefficient for x^i),
    # its derivative term contributes (xs[i] * i) to the new coefficient for x^(i-1).
    #
    # The list comprehension `[xs[i] * i for i in range(1, n)]` directly calculates
    # these new coefficients:
    # - For i=1: xs[1] * 1 (new coefficient for x^0)
    # - For i=2: xs[2] * 2 (new coefficient for x^1)
    # - ...
    # - For i=n-1: xs[n-1] * (n-1) (new coefficient for x^(n-2))
    
    return [xs[i] * i for i in range(1, n)]