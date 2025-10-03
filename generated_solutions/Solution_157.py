def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    
    A right-angled triangle is a triangle in which one angle is a right angle (90 degrees).
    This can be checked using the Pythagorean theorem: a^2 + b^2 = c^2,
    where 'c' is the longest side (hypotenuse) and 'a' and 'b' are the other two sides (legs).
    
    Args:
        a (int or float): Length of the first side.
        b (int or float): Length of the second side.
        c (int or float): Length of the third side.
        
    Returns:
        bool: True if the sides form a right-angled triangle, False otherwise.
    """
    
    # 1. Put the side lengths into a list.
    sides = [a, b, c]
    
    # 2. Sort the list in ascending order.
    # This ensures that sides[0] and sides[1] are the shorter sides (legs)
    # and sides[2] is the longest side (potential hypotenuse).
    sides.sort()
    
    # 3. Apply the Pythagorean theorem.
    # Check if the square of the longest side equals the sum of the squares of the other two sides.
    # We use **2 for squaring.
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False