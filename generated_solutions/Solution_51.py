def remove_vowels(text: str) -> str:
    """
    remove_vowels is a function that takes string and returns string without vowels.
        >>> remove_vowels('')
        ''
        >>> remove_vowels("abcdef\\nghijklm")
        'bcdf\\nghjklm'
        >>> remove_vowels('abcdef')
        'bcdf'
        >>> remove_vowels('aaaaa')
        ''
        >>> remove_vowels('aaBAA')
        'B'
        >>> remove_vowels('zbcd')
        'zbcd'
    """
    # Define a string containing all lowercase vowels
    vowels = "aeiou"
    
    # Use a generator expression to iterate through each character in the input string.
    # For each character, convert it to lowercase and check if it's NOT in the 'vowels' string.
    # If it's not a vowel (case-insensitive), include it in the new list of characters.
    # Finally, join all the selected characters back into a single string.
    return "".join(char for char in text if char.lower() not in vowels)