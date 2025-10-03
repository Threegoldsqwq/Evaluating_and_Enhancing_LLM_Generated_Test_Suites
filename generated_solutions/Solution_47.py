def median(l):
    """
    Return median of elements in the list l.
    The median is the middle number in a sorted, ascending or descending, list of numbers.
    If the list has an odd number of elements, the median is the middle element.
    If the list has an even number of elements, the median is the average of the two middle elements.

    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    8.0
    >>> median([1])
    1
    >>> median([1, 2])
    1.5
    >>> median([])
    Traceback (most recent call last):
    ...
    ValueError: Input list cannot be empty for median calculation.
    """
    if not l:
        raise ValueError("Input list cannot be empty for median calculation.")

    sorted_l = sorted(l)
    n = len(sorted_l)

    if n % 2 == 1:
        # Odd number of elements: return the middle element
        return sorted_l[n // 2]
    else:
        # Even number of elements: return the average of the two middle elements
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2.0