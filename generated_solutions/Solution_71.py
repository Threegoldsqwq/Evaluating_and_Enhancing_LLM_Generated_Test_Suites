import math

def triangle_area(a: float, b: float, c: float) -> float:
    """
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1.
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    """
    
    # 1. Check for valid side lengths (must be positive)
    if a <= 0 or b <= 0 or c <= 0:
        return -1
        
    # 2. Check the triangle inequality theorem:
    # The sum of any two sides must be strictly greater than the third side.
    if not (a + b > c and a + c > b and b + c > a):
        return -1
        
    # If the triangle is valid, proceed to calculate the area using Heron's formula.
    
    # 3. Calculate the semi-perimeter (s)
    s = (a + b + c) / 2
    
    # 4. Calculate the area using Heron's formula
    # The term inside the square root must be non-negative.
    # Due to the triangle inequality checks, (s-a), (s-b), and (s-c) will be non-negative,
    # so their product with s will also be non-negative.
    area_squared = s * (s - a) * (s - b) * (s - c)
    
    # In very rare cases due to floating point inaccuracies, area_squared might be slightly negative
    # when it should be exactly zero (e.g., for degenerate triangles if `>` was `>=`).
    # However, our strict inequality check (a+b>c) prevents degenerate triangles from being valid,
    # so area_squared should always be positive for valid triangles.
    area = math.sqrt(area_squared)
    
    # 5. Round the area to 2 decimal points
    rounded_area = round(area, 2)
    
    return rounded_area