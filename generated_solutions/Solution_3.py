def below_zero(operations: list) -> bool:
    """
    Detects if at any point the bank account balance falls below zero.

    The account starts with a zero balance. Each operation in the list
    is either a deposit (positive number) or a withdrawal (negative number).

    Args:
        operations: A list of integers representing deposits and withdrawals.

    Returns:
        True if the balance ever falls below zero, False otherwise.

    Examples:
        >>> below_zero([1, 2, 3])
        False
        >>> below_zero([1, 2, -4, 5])
        True
        >>> below_zero([-10, 5, 5])
        True
        >>> below_zero([5, -2, -3, 1])
        False
        >>> below_zero([])
        False
        >>> below_zero([10])
        False
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False