def minSubArraySum(nums: list[int]) -> int:
    """
    Finds the minimum sum of any non-empty sub-array of nums.

    Args:
        nums: A list of integers. Assumed to be non-empty based on examples.

    Returns:
        The minimum sum found among all non-empty sub-arrays.
    """
    # Handle the case of an empty array if it were possible, though examples
    # imply non-empty. For a non-empty array, nums[0] is safe.
    if not nums:
        # Depending on problem requirements, could raise an error or return
        # a specific value like 0 or float('inf').
        # For this problem context, an empty input is usually not expected.
        raise ValueError("Input array cannot be empty.")

    # Initialize min_so_far with the first element, as any single element
    # is a valid non-empty sub-array.
    min_so_far = nums[0]
    # current_min stores the minimum sum of a sub-array ending at the current position.
    current_min = nums[0]

    # Iterate from the second element
    for i in range(1, len(nums)):
        # Calculate the minimum sum ending at the current position.
        # It's either the current element itself (starting a new sub-array)
        # or the current element added to the previous current_min (extending the sub-array).
        current_min = min(nums[i], current_min + nums[i])

        # Update the overall minimum sum found so far.
        min_so_far = min(min_so_far, current_min)

    return min_so_far