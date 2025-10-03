def parse_nested_parens(paren_string: str) -> list[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    >>> parse_nested_parens('()')
    [1]
    >>> parse_nested_parens('((()))')
    [3]
    >>> parse_nested_parens('')
    []
    >>> parse_nested_parens('()()()')
    [1, 1, 1]
    >>> parse_nested_parens('((())) (()) ()')
    [3, 2, 1]
    """
    results = []
    
    # Split the input string into individual groups of parentheses.
    # Using .split() without arguments handles multiple spaces and leading/trailing spaces correctly.
    groups = paren_string.split() 

    for group in groups:
        current_depth = 0  # Tracks the current nesting level
        max_depth = 0      # Stores the maximum nesting level found so far for the current group

        for char in group:
            if char == '(':
                current_depth += 1
                # Update max_depth if the current_depth is greater
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                # For a closing parenthesis, we simply decrease the current_depth.
                # We don't update max_depth here because deeper nesting is found with '('.
                current_depth -= 1
        
        results.append(max_depth)
        
    return results