def triangle_area(side: float, high: float) -> float:
    """
    Given the length of a side (base) and the corresponding height,
    return the area of the triangle.

    The formula for the area of a triangle is:
    Area = 0.5 * base * height

    :param side: The length of the base of the triangle.
    :param high: The perpendicular height corresponding to the given base.
    :return: The calculated area of the triangle.

    >>> triangle_area(5, 3)
    7.5
    >>> triangle_area(10, 4)
    20.0
    >>> triangle_area(7.5, 2)
    7.5
    >>> triangle_area(0, 5)
    0.0
    >>> triangle_area(5, 0)
    0.0
    """
    if side < 0 or high < 0:
        raise ValueError("Side and high must be non-negative values.")
    return 0.5 * side * high