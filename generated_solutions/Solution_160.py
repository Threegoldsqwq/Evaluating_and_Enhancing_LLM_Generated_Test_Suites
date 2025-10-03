def evaluate_expression(operator, operand):
    """
    Given two lists operator, and operand, builds an algebraic expression
    and returns its evaluation.

    The basic algebra operations supported:
    Addition ( + )
    Subtraction ( - )
    Multiplication ( * )
    Floor division ( // )
    Exponentiation ( ** )

    Args:
        operator (list[str]): A list of strings representing algebraic operations.
                              e.g., ['+', '*', '-']
        operand (list[int]): A list of non-negative integers.
                             e.g., [2, 3, 4, 5]

    Returns:
        int: The result of evaluating the algebraic expression.

    Example:
        operator=['+', '*', '-']
        operand=[2, 3, 4, 5]
        Expression: 2 + 3 * 4 - 5
        Result: 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.
    """
    
    # Initialize a list to hold the components of the expression string.
    expression_parts = []
    
    # The expression always starts with the first operand.
    # Convert it to a string to be joined later.
    expression_parts.append(str(operand[0]))
    
    # Iterate through the operators and the corresponding subsequent operands.
    # Since len(operator) == len(operand) - 1, this loop covers all operators
    # and all operands from the second one to the last.
    for i in range(len(operator)):
        # Add the current operator.
        expression_parts.append(operator[i])
        # Add the next operand, converted to string.
        expression_parts.append(str(operand[i+1]))
        
    # Join all parts with spaces to form the complete algebraic expression string.
    # For example, ['2', '+', '3', '*', '4', '-', '5'] becomes "2 + 3 * 4 - 5".
    expression_string = " ".join(expression_parts)
    
    # Use Python's built-in eval() function to evaluate the expression string.
    # eval() correctly handles operator precedence (e.g., multiplication before addition).
    # Given the problem constraints (simple operations, non-negative integers),
    # using eval() is safe and efficient for this specific problem.
    return eval(expression_string)