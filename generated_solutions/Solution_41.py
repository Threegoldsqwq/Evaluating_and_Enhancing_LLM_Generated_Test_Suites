def count_collisions(n: int) -> int:
    """
    Calculates the total number of collisions between two sets of cars.

    There are 'n' cars driving left-to-right (LTR) and 'n' cars driving
    right-to-left (RTL) on an infinitely long, straight road. All cars
    move at the same speed. The two sets of cars start very far apart,
    implying all LTR cars are initially to the left of all RTL cars.

    Crucially, cars continue moving in their trajectory as if they did not
    collide (i.e., they pass through each other). A collision is defined
    as an LTR car hitting an RTL car.

    Args:
        n: The number of cars in each set (e.g., n=3 means 3 LTR cars and 3 RTL cars).
           Must be a non-negative integer.

    Returns:
        The total number of collision events.
    
    Raises:
        ValueError: If n is a negative number.
    """
    if n < 0:
        raise ValueError("The number of cars (n) cannot be negative.")
    
    # Due to the rule that cars continue moving in their trajectory as if they
    # did not collide (i.e., they pass through each other), each car maintains
    # its original speed and direction.
    #
    # Consider any single LTR car. It starts to the left of all RTL cars and
    # moves right. Every RTL car starts to the right of all LTR cars and moves left.
    # Therefore, every LTR car will eventually cross paths with every single
    # RTL car. Each such crossing constitutes one collision event.
    #
    # With 'n' LTR cars and 'n' RTL cars, there are 'n * n' unique pairs of
    # (LTR car, RTL car). Each of these pairs will have exactly one collision.
    return n * n