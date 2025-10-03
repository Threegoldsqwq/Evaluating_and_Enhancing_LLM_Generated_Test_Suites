def get_closest_vowel(word: str) -> str:
    """
    Finds the closest vowel that stands between two consonants from the right side of the word.
    Vowels in the beginning and ending do not count.

    Args:
        word: The input string containing English letters only.

    Returns:
        The closest vowel (from the right) that meets the condition, or an empty string
        if no such vowel is found.
    """
    VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    # Helper function to check if a character is a consonant.
    # Since the input is guaranteed to be English letters only,
    # a character is a consonant if it's not a vowel.
    def is_consonant(char: str) -> bool:
        return char not in VOWELS

    # We need to iterate from right to left.
    # The vowel cannot be at index 0 or len(word) - 1.
    # So, the possible indices for the vowel are from len(word) - 2 down to 1.
    # The `range` function (start, stop, step) is inclusive for start and exclusive for stop.
    # So, range(len(word) - 2, 0, -1) will iterate len(word) - 2, len(word) - 3, ..., 1.
    for i in range(len(word) - 2, 0, -1):
        current_char = word[i]
        left_char = word[i - 1]
        right_char = word[i + 1]

        # Check if the current character is a vowel
        if current_char in VOWELS:
            # Check if its left and right neighbors are consonants
            if is_consonant(left_char) and is_consonant(right_char):
                return current_char # Found the closest one from the right

    # If the loop completes, no such vowel was found
    return ""