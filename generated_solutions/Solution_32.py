import math

def _evaluate_poly_horner(xs, x):
    """
    Evaluates a polynomial with coefficients xs at point x using Horner's method.
    The polynomial is defined as: xs[0] + xs[1]*x + xs[2]*x^2 + ... + xs[n]*x^n.
    
    Args:
        xs (list): A list of polynomial coefficients [a0, a1, ..., an].
        x (float): The point at which to evaluate the polynomial.
        
    Returns:
        float: The value of the polynomial at point x.
    """
    if not xs:
        return 0.0
    
    # Start with the highest degree term's coefficient (an)
    result = float(xs[-1])
    
    # Iterate from the second highest degree coefficient (an-1) down to the constant term (a0)
    for i in range(len(xs) - 2, -1, -1):
        result = result * x + xs[i]
        
    return result

def find_zero(xs):
    """
    Finds a single real root for a polynomial with coefficients xs.

    The function adheres to the problem's constraints:
    1. xs is a list of coefficients [a0, a1, ..., an] where a0 is the constant term.
    2. len(xs) is an even number, implying the polynomial's degree (len(xs) - 1) is odd.
    3. The largest non-zero coefficient (xs[-1]) is guaranteed to be non-zero,
       which ensures it's an odd-degree polynomial, always having at least one real root.

    Uses the bisection method to efficiently find one such root.

    Args:
        xs (list): A list of polynomial coefficients.

    Returns:
        float: A single real root of the polynomial.

    Raises:
        ValueError: If input constraints (non-empty, even number of coefficients) are not met.
        Exception: If a bracketing interval cannot be found within extremely wide bounds.

    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x, root at -0.5
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = x^3 - 6x^2 + 11x - 6. One root is 1.
    1.0
    >>> round(find_zero([0, 0, 0, 1]), 2) # f(x) = x^3, root at 0.0
    0.0
    >>> round(find_zero([-0.5, 0, 0, 1]), 2) # f(x) = x^3 - 0.5, root at 0.79
    0.79
    """
    # 1. Validate input as per problem constraints
    if not xs or len(xs) % 2 != 0:
        raise ValueError("Input coefficients list must be non-empty and have an even number of elements.")
    
    # The problem guarantees that xs[-1] is non-zero, making it a true odd-degree polynomial.
    # This ensures a real root exists.
    
    # 2. Bisection method parameters
    tolerance = 1e-8 # Desired precision for the root or the interval size
    max_iterations = 100 # Safety limit to prevent infinite loops

    # 3. Initial search interval [a, b]
    # For odd-degree polynomials, roots aren't necessarily close to zero.
    # We need a robust way to find an interval [a, b] where f(a) and f(b) have opposite signs.
    # Start with a reasonably wide interval and expand if necessary.
    a = -10.0
    b = 10.0

    fa = _evaluate_poly_horner(xs, a)
    fb = _evaluate_poly_horner(xs, b)

    # 4. Handle edge cases where initial bounds might be very close to a root
    if abs(fa) < tolerance:
        return a
    if abs(fb) < tolerance:
        return b

    # 5. Expand the search range until f(a) and f(b) have opposite signs.
    # For an odd-degree polynomial, this is guaranteed to happen eventually,
    # as the polynomial goes to +/- infinity at the extremes.
    # We add a safety check for extremely large ranges.
    range_expansion_limit = 1e18 
    while fa * fb >= 0:
        a *= 2.0  # Expand lower bound
        b *= 2.0  # Expand upper bound
        fa = _evaluate_poly_horner(xs, a)
        fb = _evaluate_poly_horner(xs, b)

        # Check for root at newly expanded bounds
        if abs(fa) < tolerance:
            return a
        if abs(fb) < tolerance:
            return b

        # Prevent infinite loop if something goes wrong (e.g., coefficients are all zero,
        # though this should be prevented by problem constraints implying xs[-1] != 0).
        if abs(b - a) > range_expansion_limit:
            raise Exception("Could not find a bracketing interval for the root within reasonable bounds. "
                            "This might indicate an issue with polynomial coefficients or an extremely large root.")

    # 6. Now we have a valid interval [a, b] where f(a) and f(b) have opposite signs.
    # Apply the bisection method.
    for _ in range(max_iterations):
        c = (a + b) / 2.0
        fc = _evaluate_poly_horner(xs, c)

        # If fc is very close to zero, or the interval is sufficiently small, we found our root.
        if abs(fc) < tolerance or (b - a) / 2.0 < tolerance:
            return c
        
        # Determine which sub-interval contains the root
        if fa * fc < 0: # Root is in [a, c]
            b = c
            fb = fc # Update fb to fc for the next iteration
        else: # Root is in [c, b] (implies fc * fb < 0)
            a = c
            fa = fc # Update fa to fc for the next iteration

    # 7. If max_iterations reached without satisfying tolerance, return the midpoint
    # of the current interval. This provides the best estimate found within the limit.
    return (a + b) / 2.0