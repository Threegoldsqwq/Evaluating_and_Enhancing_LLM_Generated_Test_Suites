def select_words(s: str, n: int) -> list[str]:
    """
    Returns a list of all words from string s that contain exactly n consonants,
    in order these words appear in the string s.

    Args:
        s (str): The input string containing letters and spaces.
        n (int): The natural number representing the exact count of consonants required.

    Returns:
        list[str]: A list of words meeting the criteria, in their original order.
    """
    # 1. Handle empty string case
    if not s:
        return []

    # 2. Define a set of vowels for efficient lookup (case-insensitive)
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # 3. Split the string into words.
    # s.split() handles multiple spaces and leading/trailing spaces correctly.
    words = s.split()

    result_words = []

    # 4. Iterate through each word
    for word in words:
        consonant_count = 0
        # Iterate through each character in the current word
        for char in word:
            # Convert character to lowercase for case-insensitive comparison
            lower_char = char.lower()
            
            # 5. Check if the character is a consonant
            # Since the input contains only letters and spaces, we only need to check
            # if it's not a vowel.
            if lower_char not in vowels:
                consonant_count += 1
        
        # 6. If the consonant count matches n, add the word to the result list
        if consonant_count == n:
            result_words.append(word)
            
    # 7. Return the final list of words
    return result_words