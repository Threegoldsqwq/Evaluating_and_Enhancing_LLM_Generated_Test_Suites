import math

def closest_integer(s: str) -> int:
    """
    Takes a string representing a number and returns the closest integer to it.
    If the number is equidistant from two integers, it rounds away from zero.

    Args:
        s: A string representing a number (e.g., "10", "15.3", "-14.5").

    Returns:
        The closest integer according to the specified rounding rules.
    """
    f_num = float(s)

    # Get the integer less than or equal to f_num
    floor_val = math.floor(f_num)
    # Get the integer greater than or equal to f_num
    ceil_val = math.ceil(f_num)

    # Calculate the fractional part of the number
    # This tells us how far f_num is from floor_val.
    # For example:
    # 15.3 - 15.0 = 0.3
    # 14.5 - 14.0 = 0.5
    # -14.5 - (-15.0) = 0.5
    # -14.7 - (-15.0) = 0.3
    fractional_part = f_num - floor_val

    if fractional_part < 0.5:
        # The number is closer to the lower integer
        return int(floor_val)
    elif fractional_part > 0.5:
        # The number is closer to the upper integer
        return int(ceil_val)
    else:  # fractional_part == 0.5, equidistant case (e.g., X.5)
        # Round away from zero
        if f_num >= 0:
            # For positive numbers, rounding away from zero means rounding up.
            # Example: 14.5 -> 15 (ceil_val)
            return int(ceil_val)
        else:
            # For negative numbers, rounding away from zero means rounding down (more negative).
            # Example: -14.5 -> -15 (floor_val)
            return int(floor_val)