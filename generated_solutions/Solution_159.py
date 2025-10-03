def eat(number: int, need: int, remaining: int) -> list[int]:
    """
    Simulates a hungry rabbit eating carrots.

    Args:
        number (int): The number of carrots the rabbit has already eaten.
        need (int): The number of additional carrots the rabbit needs to eat.
        remaining (int): The number of carrots currently available in stock.

    Returns:
        list[int]: An array containing two integers:
                   [total_carrots_eaten, carrots_left_in_stock].
    """
    # Determine how many carrots the rabbit actually eats from the remaining stock.
    # The rabbit will eat either the 'need' amount or all 'remaining' carrots,
    # whichever is less, because it cannot eat more than what's available.
    carrots_eaten_now = min(need, remaining)

    # Calculate the total number of carrots the rabbit has eaten after this meal.
    total_carrots_eaten = number + carrots_eaten_now

    # Calculate the number of carrots left in the stock.
    carrots_left_in_stock = remaining - carrots_eaten_now

    return [total_carrots_eaten, carrots_left_in_stock]