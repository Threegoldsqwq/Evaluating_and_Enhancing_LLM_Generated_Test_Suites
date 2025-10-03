def count_upper(s: str) -> int:
    """
    Given a string s, count the number of uppercase vowels at even indices.

    An uppercase vowel is one of 'A', 'E', 'I', 'O', 'U'.
    Even indices are 0, 2, 4, etc.

    For example:
    count_upper('aBCdEf') returns 1 ( 'E' at index 4)
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    count_upper('AEIOU') returns 3 ( 'A' at index 0, 'I' at index 2, 'U' at index 4)
    """
    count = 0
    uppercase_vowels = {'A', 'E', 'I', 'O', 'U'}

    for index, char in enumerate(s):
        # Check if the index is even
        if index % 2 == 0:
            # Check if the character is an uppercase vowel
            if char in uppercase_vowels:
                count += 1
    return count