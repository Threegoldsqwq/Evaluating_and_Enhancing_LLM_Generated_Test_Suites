def prod_signs(arr: list[int]) -> int | None:
    """
    Calculates the sum of magnitudes of integers multiplied by the product of all signs.

    Args:
        arr: A list of integers.

    Returns:
        The sum of magnitudes multiplied by the product of signs,
        or None if the input array is empty.
    """
    if not arr:
        return None

    sum_magnitudes = 0
    product_signs = 1
    has_zero = False  # Flag to track if any zero is present in the array

    for num in arr:
        # Accumulate the sum of magnitudes
        sum_magnitudes += abs(num)

        # Determine the sign contribution to the product_signs
        if num == 0:
            has_zero = True
            # If we encounter a zero, the overall product of signs will be zero.
            # We can effectively "short-circuit" the sign calculation part for remaining numbers
            # because multiplying by zero will make the product zero regardless.
            # However, we still need to sum magnitudes for all numbers.
        elif num < 0:
            product_signs *= -1
            # If num > 0, product_signs remains unchanged (effectively multiplied by 1)

    # If any zero was found, the total product of signs is 0.
    # Otherwise, it's the accumulated product_signs.
    final_product_of_signs = 0 if has_zero else product_signs

    return sum_magnitudes * final_product_of_signs