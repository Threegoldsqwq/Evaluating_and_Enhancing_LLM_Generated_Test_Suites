def vowels_count(word: str) -> int:
    """
    Counts the number of vowels in a string, following specific rules.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is a vowel only when it is at the end of the word.
    The check is case-insensitive.

    Args:
        word: The input string.

    Returns:
        The number of vowels in the string.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    >>> vowels_count("")
    0
    >>> vowels_count("rhythm")
    0
    >>> vowels_count("fly")
    1
    >>> vowels_count("aeiouAEIOU")
    10
    >>> vowels_count("yearly")
    3
    >>> vowels_count("symphony")
    2
    >>> vowels_count("y")
    1
    >>> vowels_count("PytHon")
    1
    """
    count = 0
    # Define standard vowels for quick lookup (case-insensitive)
    standard_vowels = {'a', 'e', 'i', 'o', 'u'}

    # Handle empty string edge case
    if not word:
        return 0

    # Iterate through the word, excluding the last character.
    # Any 'y' encountered here is NOT a vowel by definition.
    for i in range(len(word) - 1):
        char = word[i].lower()
        if char in standard_vowels:
            count += 1

    # Check the last character separately due to the special rule for 'y'.
    last_char = word[-1].lower()
    if last_char in standard_vowels:
        count += 1
    elif last_char == 'y':
        # 'y' is a vowel only if it is at the end of the word
        count += 1

    return count

# --- Add more test cases ---
if __name__ == "__main__":
    test_cases = [
        # Provided examples
        ("abcde", 2),
        ("ACEDY", 3),

        # Edge cases
        ("", 0),                  # Empty string
        ("a", 1),                 # Single standard vowel
        ("y", 1),                 # Single 'y' word (y is at the end)
        ("b", 0),                 # Single consonant
        ("yyyyy", 1),             # Multiple 'y's, only last one counts
        ("BY", 1),                # 'y' at end
        ("rhythm", 0),            # 'y' not at end, no standard vowels
        ("strength", 0),          # No vowels at all

        # Words with standard vowels only
        ("aeiouAEIOU", 10),       # All standard vowels, mixed case
        ("beautiful", 5),         # Multiple standard vowels
        ("queue", 4),             # Specific vowel sequence

        # Words with 'y' rule
        ("happy", 2),             # 'a', 'y'
        ("yearly", 3),            # 'e', 'a', 'y' (first 'y' is not a vowel)
        ("symphony", 2),          # 'o', 'y' (middle 'y' is not a vowel)
        ("MYTH", 1),              # 'y' at end
        ("CRY", 1),               # 'y' at end
        ("TYPE", 1),              # 'e' (y not at end)
        ("gym", 0),               # 'y' not at end
        ("Glyph", 0),             # 'y' not at end

        # Mixed cases
        ("PytHon", 1),            # 'o'
        ("xylophone", 4),         # 'o', 'o', 'e' (y not at end)
        ("BYSTANDER", 2),         # 'a', 'e' (y not at end)
        ("eYe", 2),               # 'e', 'e' (y not at end)
    ]

    print("Running test cases for vowels_count:")
    for word, expected in test_cases:
        result = vowels_count(word)
        assert result == expected, f"FAIL: Input: '{word}', Expected: {expected}, Got: {result}"
        print(f"PASS: '{word}' -> Expected: {expected}, Got: {result}")

    print("\nAll test cases passed!")

    # Example from problem description via direct call
    print(f'\nvowels_count("abcde") -> {vowels_count("abcde")}')
    print(f'vowels_count("ACEDY") -> {vowels_count("ACEDY")}')