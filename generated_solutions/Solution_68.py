def pluck(nodes: list[int]) -> list[int]:
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node
    that has the smallest index.

    The plucked node should be returned in a list, [ smallest_value, its index ].
    If there are no even values or the given array is empty, return [].

    Args:
        nodes: A list of non-negative integer nodes.

    Returns:
        A list [smallest_even_value, its_index] or an empty list [].
    """
    smallest_even_value = float('inf')  # Initialize with a very large number
    smallest_even_index = -1            # Initialize with an invalid index

    if not nodes:
        return []

    for i, node_value in enumerate(nodes):
        # Check if the node value is even
        if node_value % 2 == 0:
            # If it's strictly smaller than the current smallest_even_value, update
            if node_value < smallest_even_value:
                smallest_even_value = node_value
                smallest_even_index = i
            # If it's equal to the current smallest_even_value, we do nothing
            # because we want the smallest index, and iterating from left to right
            # naturally ensures the first occurrence (smallest index) is captured.

    # If smallest_even_value is still float('inf'), it means no even numbers were found.
    if smallest_even_value == float('inf'):
        return []
    else:
        return [smallest_even_value, smallest_even_index]