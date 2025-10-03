def is_nested(bracket_string: str) -> bool:
    """
    Checks if there is a valid subsequence of brackets where at least one bracket is nested.
    A nested bracket subsequence implies a structure like `[A]` where `A` is a non-empty
    valid bracket sequence. The simplest such structure is `[[]]`.

    The function determines if there exist four indices `i < k < l < j` in the input string
    such that:
    - bracket_string[i] == '['  (outer opening bracket)
    - bracket_string[k] == '['  (inner opening bracket)
    - bracket_string[l] == ']'  (inner closing bracket)
    - bracket_string[j] == ']'  (outer closing bracket)

    This forms the subsequence `bracket_string[i]bracket_string[k]bracket_string[l]bracket_string[j]`,
    which is `[[]]`. This subsequence is valid and contains a nested bracket.

    A state machine is used to efficiently find this pattern in a single pass.

    Args:
        bracket_string: A string containing only square brackets '[' and ']'.

    Returns:
        True if such a nested subsequence exists, False otherwise.
    """
    
    # State definitions:
    # 0: Initial state, looking for the first '[' (for s[i])
    # 1: Found the first '[', looking for the second '[' (for s[k])
    # 2: Found the second '[', looking for the first ']' (for s[l])
    # 3: Found the first ']', looking for the second ']' (for s[j])
    
    state = 0

    for char in bracket_string:
        if char == '[':
            if state == 0:
                state = 1  # Transition: Found outer opening bracket
            elif state == 1:
                state = 2  # Transition: Found inner opening bracket
            # If state is 2 or 3 and we encounter ']', it means we already have the
            # necessary opening brackets, and this new '[' doesn't prevent forming
            # `[[]]`. We continue looking for the closing brackets.
            # Example: "[[[ ] ] ]" - after s[0], s[1], s[2], state is 2, then remains 2.
            # Example: "[ [ ] [ ] ]" - after s[0], s[1], s[2], state is 3. New '[' at s[3] doesn't change state.
            
        elif char == ']':
            if state == 3:
                # Transition: Found the outer closing bracket after all previous parts.
                # The pattern `[[]]` is complete.
                return True
            elif state == 2:
                state = 3  # Transition: Found inner closing bracket
            # If state is 0 or 1 and we encounter ']', it's not the required bracket
            # for the `[[]]` pattern at this stage, so we ignore it and stay in the current state.
            
    return False