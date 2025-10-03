import math

def mean_absolute_deviation(numbers: list[float]) -> float:
    """
    Calculates the Mean Absolute Deviation (MAD) around the mean for a
    given list of input numbers.

    Mean Absolute Deviation is the average absolute difference between each
    element and the dataset's mean.

    MAD = average | x - x_mean |

    Args:
        numbers: A list of numerical values (float or int).

    Returns:
        The Mean Absolute Deviation as a float.

    Raises:
        ValueError: If the input list is empty, as MAD is undefined for an
                    empty dataset.

    Examples:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
        >>> mean_absolute_deviation([1, 2, 3, 4])
        1.0
        >>> mean_absolute_deviation([5.0])
        0.0
        >>> mean_absolute_deviation([10.0, 10.0, 10.0])
        0.0
        >>> mean_absolute_deviation([1.0, 5.0, 2.0, 8.0, 4.0])
        2.08
    """
    if not numbers:
        raise ValueError("Input list cannot be empty. Mean Absolute Deviation is undefined for an empty dataset.")

    n = len(numbers)

    # Step 1: Calculate the mean of the dataset
    data_mean = sum(numbers) / n

    # Step 2: Calculate the absolute difference between each element and the mean
    # Sum these absolute differences
    sum_abs_differences = sum(abs(x - data_mean) for x in numbers)

    # Step 3: Calculate the average of these absolute differences
    # This is the Mean Absolute Deviation
    mad = sum_abs_differences / n

    return mad