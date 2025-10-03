def _parse_to_float(value):
    """
    Helper function to convert an integer, float, or string representing
    a real number into a float for comparison.
    Handles comma as a decimal separator in strings.
    """
    if isinstance(value, (int, float)):
        return float(value)
    elif isinstance(value, str):
        # Replace comma with period for float conversion
        standardized_string = value.replace(',', '.')
        try:
            return float(standardized_string)
        except ValueError:
            # This case implies the string is not a valid number,
            # which the problem statement assumes won't happen.
            # For robust production code, this would need more specific error handling.
            raise ValueError(f"Cannot convert '{value}' to a real number.")
    else:
        # Handle unexpected types, though problem implies only int, float, str
        raise TypeError(f"Unsupported type for comparison: {type(value)}")

def compare_one(v1, v2):
    """
    Compares two values (integers, floats, or strings representing real numbers)
    and returns the larger variable in its original type.
    Returns None if the values are numerically equal.

    Args:
        v1: The first value (int, float, or str).
        v2: The second value (int, float, or str).

    Returns:
        The larger variable in its original type, or None if equal.
    """
    f1 = _parse_to_float(v1)
    f2 = _parse_to_float(v2)

    if f1 == f2:
        return None
    elif f1 > f2:
        return v1
    else:  # f2 > f1
        return v2