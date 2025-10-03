def fruit_distribution(fruits_str: str, total_fruits: int) -> int:
    """
    Calculates the number of mango fruits in a basket given the distribution
    of apples and oranges and the total number of fruits.

    Args:
        fruits_str (str): A string representing the number of apples and oranges,
                          e.g., "5 apples and 6 oranges".
        total_fruits (int): The total number of fruits in the basket.

    Returns:
        int: The number of mango fruits in the basket.

    Examples:
        fruit_distribution("5 apples and 6 oranges", 19) == 8
        fruit_distribution("0 apples and 1 oranges", 3) == 2
        fruit_distribution("2 apples and 3 oranges", 100) == 95
        fruit_distribution("100 apples and 1 oranges", 120) == 19
    """
    # Split the input string by spaces to get individual words/numbers
    parts = fruits_str.split()

    # The number of apples is the first element in the split list
    num_apples = int(parts[0])

    # The number of oranges is the fourth element in the split list
    num_oranges = int(parts[3])

    # Calculate the number of mangoes
    num_mangoes = total_fruits - num_apples - num_oranges

    return num_mangoes