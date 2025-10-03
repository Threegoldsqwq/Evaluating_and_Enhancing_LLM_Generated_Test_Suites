def get_row(lst: list[list[int]], x: int) -> list[tuple[int, int]]:
    """
    Finds occurrences of integer x in a 2D ragged list (nested list)
    and returns their coordinates as a list of (row, column) tuples.

    The coordinates are sorted according to the following rules:
    1. Primarily by row in ascending order.
    2. Secondarily by column in descending order.

    Args:
        lst: A nested list of integers, where each sublist represents a row.
             Rows may have different lengths (ragged array).
        x: The integer value to search for within the list.

    Returns:
        A list of (row, column) tuples, representing the coordinates
        of all occurrences of x, sorted as specified.
        Returns an empty list if x is not found or the input list is empty.

    Examples:
        >>> get_row([
        ...   [1,2,3,4,5,6],
        ...   [1,2,3,4,1,6],
        ...   [1,2,3,4,5,1]
        ... ], 1)
        [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

        >>> get_row([], 1)
        []

        >>> get_row([[], [1], [1, 2, 3]], 3)
        [(2, 2)]

        >>> get_row([[10, 20], [30, 10, 40], [50, 60]], 10)
        [(0, 0), (1, 1)]

        >>> get_row([[1, 2], [3, 4]], 5)
        []
    """
    coordinates = []

    # Iterate through each row with its index
    for row_idx, row_list in enumerate(lst):
        # Iterate through each item in the row with its column index
        for col_idx, item in enumerate(row_list):
            if item == x:
                # If the item matches x, add its (row, column) coordinate
                coordinates.append((row_idx, col_idx))

    # Sort the collected coordinates based on the specified rules:
    # The key function returns a tuple (row, -column).
    # - Sorting by `row` (coord[0]) in ascending order is default.
    # - Sorting by `-column` (-coord[1]) effectively sorts by `column`
    #   in descending order, because a larger positive column value will
    #   result in a smaller negative value, thus coming earlier in an
    #   ascending sort.
    coordinates.sort(key=lambda coord: (coord[0], -coord[1]))

    return coordinates