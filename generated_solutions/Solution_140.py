import re

def fix_spaces(text: str) -> str:
    """
    Replaces spaces in the text:
    - If more than 2 consecutive spaces, replaces them with a hyphen.
    - Otherwise, replaces all spaces with underscores.

    Args:
        text: The input string.

    Returns:
        The string with spaces fixed according to the rules.
    """
    # Step 1: Replace sequences of 3 or more spaces with a hyphen.
    # We do this first because it's the more specific rule and
    # "consumes" the long runs of spaces before single-space replacement.
    processed_text = re.sub(r' {3,}', '-', text)

    # Step 2: Replace any remaining single spaces (which now only include
    # original single spaces or pairs of spaces that weren't caught by the
    # first rule) with underscores.
    # This will turn ' ' into '_' and '  ' into '__'.
    result = re.sub(r' ', '_', processed_text)

    return result