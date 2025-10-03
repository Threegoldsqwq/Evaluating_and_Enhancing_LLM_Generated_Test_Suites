def correct_bracketing(brackets: str) -> bool:
    """
    brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    balance = 0
    for char in brackets:
        if char == '<':
            balance += 1
        elif char == '>':
            balance -= 1
        
        # If balance goes negative, it means a closing bracket appeared
        # without a corresponding opening bracket before it.
        if balance < 0:
            return False
            
    # After checking all characters, if balance is 0, all brackets
    # were correctly matched. Otherwise, there are unmatched opening brackets.
    return balance == 0